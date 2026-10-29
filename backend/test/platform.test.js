import test from 'node:test';
import assert from 'node:assert/strict';
import { once } from 'node:events';
import { createHash } from 'node:crypto';
import { MemoryStore } from '../store.js';
import { domain, digest } from '../domain.js';
import { oauthProvider } from '../oauth.js';
import { createApp } from '../server.js';

const origin='https://toolindex.org';
const alice={uid:'alice',email:'alice@example.test',email_verified:true};
const bob={uid:'bob',email:'bob@example.test',email_verified:true};
const admin={uid:'admin',email:'reviewer@example.test',email_verified:true,admin:true};
const profile={handle:'alice-tools',displayName:'Alice <script> $&',bio:'Useful tools',website:'https://example.org/',avatar:'',discoverable:true};
const tool={name:'Example tool $1',summary:'A focused example for agents.',type:'CLI',category:'Coding',repository:'https://example.org/docs',version:'1.0',license:'MIT',installation:'Install the complete package.',manualSetup:'None',pricing:'Free',imageUrl:'',imageAlt:'',imageSource:''};
async function fixture() {const store=new MemoryStore(),api=domain(store,{listings:[]},origin);await api.saveProfile(alice,profile);return {store,api};}

test('pending tools and revisions do not enter public catalog until reviewer approval',async()=>{
  const {api}=await fixture();const d=await api.saveTool(alice,tool);await api.submit(alice,d.id,d.revision);
  assert.equal((await api.catalog()).listings.length,0);
  await assert.rejects(api.review(bob,d.id,d.revision,'publish','Reviewed package scope'),{status:403});
  await api.review(admin,d.id,d.revision,'publish','Reviewed package scope');
  assert.equal((await api.catalog()).listings[0].name,tool.name);
  const edited=await api.saveTool(alice,{...tool,name:'Updated name'},d.id,d.revision);
  assert.equal((await api.catalog()).listings[0].name,tool.name);
  await assert.rejects(api.saveTool(alice,tool,d.id,d.revision),{status:409});
  await api.submit(alice,d.id,edited.revision);
  await assert.rejects(api.review(admin,d.id,d.revision,'publish','Outdated review'),{status:409});
  await api.review(admin,d.id,edited.revision,'reject','Explain the installation first');
  assert.equal((await api.catalog()).listings[0].name,tool.name);
  await api.withdraw(alice,d.id);assert.equal((await api.catalog()).listings.length,0);
});
test('owner boundaries, verified email, handles and public projection',async()=>{
  const {api,store}=await fixture();const d=await api.saveTool(alice,tool);
  await assert.rejects(api.saveTool(bob,tool,d.id,d.revision));
  await assert.rejects(api.submit(bob,d.id,d.revision),{status:404});
  await assert.rejects(api.withdraw(bob,d.id),{status:404});
  assert.equal((await api.mine(bob)).length,0);
  await assert.rejects(api.saveProfile({...bob,email_verified:false},{...profile,handle:'bob-tools'}),{status:403});
  await assert.rejects(api.saveProfile(bob,profile),{status:409});
  await assert.rejects(api.saveProfile(alice,{...profile,handle:'new-handle'}),{status:409});
  const p=await api.publishedProfile(profile.handle);assert.ok(!JSON.stringify(p).includes(alice.email));assert.ok(!p.uid);
  await api.saveProfile(alice,{...profile,discoverable:false});assert.equal((await api.publishedProfiles()).length,0);
  assert.equal((await store.list('submissions')).length,1);
});
test('unsafe URLs, HTML strings, optional image provenance and bounded daily creation',async()=>{
  const {api}=await fixture();
  for(const repository of ['javascript:alert(1)','http://example.com','https://user:secret@example.org'])await assert.rejects(api.saveTool(alice,{...tool,repository}));
  await assert.rejects(api.saveTool(alice,{...tool,imageUrl:'https://example.org/logo.png'}));
  for(let i=0;i<10;i++)await api.saveTool(alice,{...tool,name:'Example '+i});
  await assert.rejects(api.saveTool(alice,tool),{status:429});
});

async function oauthFixture(){
  const store=new MemoryStore(),p=oauthProvider(store,origin,async uid=>({uid,disabled:false}));
  const client=await p.clientsStore.registerClient({client_id:'client-one',client_name:'Test agent',token_endpoint_auth_method:'none',redirect_uris:['http://localhost:9876/callback']});
  const verifier='v'.repeat(64),challenge=createHash('sha256').update(verifier).digest('base64url');
  let request;await p.authorize(client,{redirectUri:client.redirect_uris[0],codeChallenge:challenge,scopes:['tools:read','tools:write'],state:'test-state',resource:new URL(origin+'/mcp')},{redirect:(_,url)=>request=new URL(url,origin).searchParams.get('request')});
  return {store,p,client,request,verifier,challenge};
}
test('OAuth code is bound to client, exact redirect, resource, user consent and one exchange',async()=>{
  const {p,client,request,challenge}=await oauthFixture();
  const redirect=new URL(await p.consent(alice,request,true)),code=redirect.searchParams.get('code');
  assert.equal(redirect.searchParams.get('state'),'test-state');assert.equal(redirect.searchParams.get('iss'),origin+'/');
  await assert.rejects(p.consent(alice,request,true),{status:400});
  assert.equal(await p.challengeForAuthorizationCode(client,code),challenge);
  await assert.rejects(p.challengeForAuthorizationCode({...client,client_id:'other'},code));
  await assert.rejects(p.exchangeAuthorizationCode(client,code,undefined,'http://localhost:9876/other'));
  await assert.rejects(p.exchangeAuthorizationCode(client,code,undefined,client.redirect_uris[0],new URL('https://other.example/mcp')));
  const tokens=await p.exchangeAuthorizationCode(client,code,undefined,client.redirect_uris[0]);
  await assert.rejects(p.exchangeAuthorizationCode(client,code,undefined,client.redirect_uris[0]));
  assert.equal((await p.verifyAccessToken(tokens.access_token)).extra.uid,alice.uid);
  await assert.rejects(p.verifyAccessToken('some-firebase-token'));
});
test('refresh tokens rotate, scope expansion fails, reuse revokes the entire grant',async()=>{
  const {p,client,request}=await oauthFixture();const code=new URL(await p.consent(alice,request,true)).searchParams.get('code');
  const t=await p.exchangeAuthorizationCode(client,code,undefined,client.redirect_uris[0]);
  await assert.rejects(p.exchangeRefreshToken(client,t.refresh_token,['profile:write']));
  const next=await p.exchangeRefreshToken(client,t.refresh_token,['tools:read']);assert.notEqual(next.refresh_token,t.refresh_token);
  await assert.rejects(p.exchangeRefreshToken(client,t.refresh_token));
  await assert.rejects(p.verifyAccessToken(next.access_token));
});
test('OAuth grants belong to their user, revoke access and reject unsafe redirects',async()=>{
  const {p,client,request}=await oauthFixture();
  for(const uri of ['http://evil.example/cb','https://example.org/cb#fragment','https://user:pass@example.org/cb'])await assert.rejects(p.clientsStore.registerClient({...client,redirect_uris:[uri]}));
  const code=new URL(await p.consent(alice,request,true)).searchParams.get('code'),t=await p.exchangeAuthorizationCode(client,code,undefined,client.redirect_uris[0]);
  const [grant]=await p.grants(alice);assert.equal((await p.grants(bob)).length,0);
  await assert.rejects(p.revokeGrant(bob,grant.id),{status:404});
  await p.revokeToken(client,{token:t.access_token});await assert.rejects(p.verifyAccessToken(t.access_token));
});

async function httpFixture(t,options={}){
  const users={alice,bob,admin};
  const auth={getUser:async uid=>({...users[uid],emailVerified:users[uid]?.email_verified}),verifySessionCookie:async token=>{if(!users[token])throw Error('bad');return users[token];},verifyIdToken:async()=>({...alice,auth_time:Math.floor(Date.now()/1000)}),createSessionCookie:async()=>'alice'};
  const store=new MemoryStore();
  const f=await createApp({store,auth,admins:admin.email,origin,...options});
  const server=f.app.listen(0,'127.0.0.1');await once(server,'listening');t.after(()=>new Promise(resolve=>server.close(resolve)));
  const base='http://127.0.0.1:'+server.address().port;
  const call=async(url,{method='GET',body,user='alice',headers={}}={})=>fetch(base+url,{method,redirect:'manual',headers:{Origin:origin,Cookie:'__session='+user,...(body?{'Content-Type':'application/json'}:{}),...headers},...(body?{body:JSON.stringify(body)}:{})});
  return {...f,store,call,base};
}
test('HTTP: CSRF, unauthorized review, escaped crawlable profiles and pending privacy',async t=>{
  const {call,api}=await httpFixture(t);
  assert.equal((await call('/api/me',{user:'none'})).status,401);
  assert.equal((await call('/api/me/profile',{method:'PUT',body:profile,headers:{Origin:'https://evil.example'}})).status,403);
  assert.equal((await call('/api/me/profile',{method:'PUT',body:profile})).status,200);
  const p=await call('/people/alice-tools/');assert.equal(p.status,200);const html=await p.text();assert.ok(html.includes('Alice &lt;script&gt; $&amp;'));assert.ok(!html.includes('Alice <script>'));assert.ok(html.includes('ProfilePage'));
  const d=await api.saveTool(alice,tool);await api.submit(alice,d.id,d.revision);
  assert.equal((await call('/api/review',{user:'bob'})).status,403);
  assert.equal((await call('/tools/'+d.id+'/')).status,404);
  assert.ok(!(await(await call('/catalog.json')).text()).includes(d.id));
  assert.ok(!(await(await call('/sitemap.xml')).text()).includes(d.id));
  assert.equal((await call('/api/review/'+d.id,{method:'POST',user:'admin',body:{revision:d.revision,decision:'publish',evidence:'Checked installation and license scope'}})).status,200);
  assert.equal((await call('/tools/'+d.id+'/')).status,200);assert.equal((await call('/tools/'+d.id+'/index.md')).status,200);
  const pub=await(await call('/api/public/tools/'+d.id)).json();assert.ok(!pub.ownerUid&&!pub.email&&!pub.reviewNote);
  const home=await(await call('/')).text();assert.ok(home.includes('/tools/'+d.id+'/'));assert.ok(home.includes('Example tool $1'));
});
test('HTTP: complete OAuth PKCE, MCP tools and persisted provider restart',async t=>{
  const {call,store,base}=await httpFixture(t);
  let r=await call('/mcp',{method:'POST',body:{}});assert.equal(r.status,401);assert.ok(r.headers.get('www-authenticate').includes('/.well-known/oauth-protected-resource/mcp'));
  assert.equal((await call('/.well-known/oauth-protected-resource/mcp')).status,200);
  const md=await(await call('/.well-known/oauth-authorization-server')).json();assert.equal(md.issuer,origin+'/');assert.deepEqual(md.token_endpoint_auth_methods_supported,['none']);
  r=await call('/register',{method:'POST',body:{client_name:'Integration agent',redirect_uris:['http://localhost:7777/cb'],token_endpoint_auth_method:'none',grant_types:['authorization_code','refresh_token'],response_types:['code']}});
  assert.equal(r.status,201);const c=await r.json(),verifier='a'.repeat(64),challenge=createHash('sha256').update(verifier).digest('base64url');
  const params=new URLSearchParams({client_id:c.client_id,redirect_uri:c.redirect_uris[0],response_type:'code',code_challenge:challenge,code_challenge_method:'S256',scope:'tools:read tools:write',resource:origin+'/mcp',state:'keep-state'});
  r=await call('/authorize?'+params);assert.equal(r.status,302);const request=new URL(r.headers.get('location'),base).searchParams.get('request');
  r=await call('/api/account/consent/'+request,{method:'POST',body:{allow:true}});assert.equal(r.status,200);const redir=new URL((await r.json()).redirect),code=redir.searchParams.get('code');
  async function token(codeVerifier){return fetch(base+'/token',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams({client_id:c.client_id,grant_type:'authorization_code',code,code_verifier:codeVerifier,redirect_uri:c.redirect_uris[0],resource:origin+'/mcp'})});}
  assert.equal((await token('b'.repeat(64))).status,400);
  const tokenResponse=await token(verifier);assert.equal(tokenResponse.status,200);const tokens=await tokenResponse.json();
  assert.equal((await token(verifier)).status,400);
  const restarted=oauthProvider(store,origin,async uid=>({uid}));assert.equal((await restarted.verifyAccessToken(tokens.access_token)).extra.uid,'alice');
  r=await call('/mcp',{method:'POST',headers:{Authorization:'Bearer '+tokens.access_token,Accept:'application/json, text/event-stream'},body:{jsonrpc:'2.0',id:1,method:'tools/list',params:{}}});assert.equal(r.status,200);const rpc=await r.json();assert.ok(rpc.result.tools.some(x=>x.name==='submit_tool_for_review'));assert.ok(!rpc.result.tools.some(x=>/approve|publish_tool/.test(x.name)));
});
test('HTTP: bounded request rates apply before account authorization or file access',async t=>{
  const {call}=await httpFixture(t,{httpLimit:3});
  assert.equal((await call('/llms.txt')).status,200);
  assert.equal((await call('/api/me',{user:'none'})).status,401);
  assert.equal((await call('/account/sign-in/')).status,200);
  const limited=await call('/api/me',{user:'none'});assert.equal(limited.status,429);
  assert.ok(limited.headers.get('ratelimit'));
});

test('HTTP: only configured social providers are public and private auth returns stay off search engines',async t=>{
  const {call}=await httpFixture(t,{signInProviders:'google.com,unconfigured.example,github.com'});
  const config=await call('/api/config');assert.equal(config.headers.get('cache-control'),'no-store');
  const data=await config.json();assert.deepEqual(data.signInProviders,['google.com','github.com']);assert.ok(!data.clientSecret);
  const page=await call('/account/sign-in/?next=%2Fauthorize%2Fconsent%2F%3Frequest%3Dexample');
  assert.equal(page.headers.get('cache-control'),'private, no-store');
  assert.equal(page.headers.get('x-robots-tag'),'noindex, nofollow');
  assert.ok((await page.text()).includes('id="social-sign-in"'));
  assert.ok(page.headers.get('content-security-policy').includes('https://www.gstatic.com/firebasejs/13.1.0/'));
});
