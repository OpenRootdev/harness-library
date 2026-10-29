'use strict';
(() => {
  const host=document.querySelector('[data-account-page]'); if(!host)return;
  const mode=host.dataset.accountPage, status=document.getElementById('account-status');
  const say=(message,error=false)=>{status.textContent=message;status.classList.toggle('error',error);};
  const el=(tag,text,cls)=>{const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(cls)n.className=cls;return n;};
  async function api(url,method='GET',body){const r=await fetch(url,{method,credentials:'same-origin',headers:body?{'Content-Type':'application/json'}:{},...(body?{body:JSON.stringify(body)}:{})});const d=await r.json();if(!r.ok){const e=new Error(d.error||'Request failed');e.status=r.status;throw e;}return d;}
  function safeNext(value){try{if(!value?.startsWith('/'))return '/account/';const url=new URL(value,location.origin);return url.origin===location.origin?url.pathname+url.search+url.hash:'/account/';}catch{return '/account/';}}
  function signIn(){location.assign('/account/sign-in/?next='+encodeURIComponent(location.pathname+location.search));}
  async function firebase(action,body){const config=await api('/api/config');if(!config.apiKey)throw new Error('Account service is being configured. Please try again shortly.');if(action==='sendOobCode')body.continueUrl=config.publicOrigin+'/account/sign-in/';const r=await fetch('https://identitytoolkit.googleapis.com/v1/accounts:'+action+'?key='+encodeURIComponent(config.apiKey),{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});const d=await r.json();if(!r.ok){const code=d.error?.message||'';throw new Error(code.startsWith('EMAIL_EXISTS')?'An account already exists. Sign in or reset your password.':code.startsWith('WEAK_PASSWORD')?'Choose a stronger password of at least 10 characters.':code.includes('EXPIRED')?'This link expired. Request a new one.':code.includes('INVALID_OOB_CODE')?'This link was already used or is invalid.':'Could not complete authentication. Check your details or try password recovery.');}return d;}
  function fields(form){return Object.fromEntries(new FormData(form));}
  async function attempt(fn){try{await fn();}catch(e){if(e.status===401&&mode!=='auth'&&mode!=='email-action'){signIn();return;}say(e.message,true);}}

  if(mode==='auth'){
    let socialBusy=false;
    api('/api/config').then(async config=>{
      if(!config.signInProviders?.length)return;
      const social=await import('/social-auth.js'), connect=social.prepareSocialSignIn(config);
      const box=document.getElementById('social-sign-in');
      for(const [providerId,label]of [['google.com','Google'],['github.com','GitHub']]){
        if(!config.signInProviders.includes(providerId))continue;
        const button=el('button','Continue with '+label,'button');button.type='button';
        button.onclick=async()=>{
          if(socialBusy)return;socialBusy=true;say('Opening '+label+' sign-in...');
          try{
            await connect(providerId,async idToken=>{await api('/api/account/session','POST',{idToken});});
            location.assign(safeNext(new URLSearchParams(location.search).get('next')));
          }catch(error){say(error.status?error.message:social.socialError(error),true);}
          finally{socialBusy=false;}
        };
        box.append(button);
      }
      box.hidden=false;
    }).catch(()=>say('Social sign-in could not load. You can still sign in with email.',true));
    document.getElementById('auth-form').addEventListener('submit',e=>{e.preventDefault();attempt(async()=>{
      if(socialBusy)return;
      const form=e.currentTarget, data=fields(form), action=e.submitter?.value||'signin';
      if(action==='reset'){if(!data.email||!form.elements.email.validity.valid)throw new Error('Enter your email address first.');await firebase('sendOobCode',{requestType:'PASSWORD_RESET',email:data.email});say('If an account uses this address, a password reset email will arrive.');return;}
      say(action==='signup'?'Creating your account...':'Signing in...');
      const d=await firebase(action==='signup'?'signUp':'signInWithPassword',{email:data.email,password:data.password,returnSecureToken:true});
      // Tokens stay in this function only. The persistent browser session is an HttpOnly cookie.
      const account=await firebase('lookup',{idToken:d.idToken});
      if(!account.users?.[0]?.emailVerified)await firebase('sendOobCode',{requestType:'VERIFY_EMAIL',idToken:d.idToken});
      await api('/api/account/session','POST',{idToken:d.idToken});
      form.reset();location.assign(safeNext(new URLSearchParams(location.search).get('next')));
    });});
    return;
  }
  if(mode==='email-action'){
    const params=new URLSearchParams(location.search), code=params.get('oobCode'), action=params.get('mode');
    // Remove the one-time code from browser history and any later referrers.
    history.replaceState({},'',location.pathname);
    attempt(async()=>{
      if(!code)throw new Error('No verification code. Open the link from your account email.');
      if(action==='verifyEmail'){await firebase('update',{oobCode:code});say('Email verified. Sign in again to refresh your account.');}
      else if(action==='resetPassword'){
        await firebase('resetPassword',{oobCode:code});say('Choose a new password.');
        const f=document.getElementById('password-reset-form');f.hidden=false;f.addEventListener('submit',e=>{e.preventDefault();attempt(async()=>{await firebase('resetPassword',{oobCode:code,newPassword:fields(f).password});f.hidden=true;f.reset();say('Password updated. You can sign in now.');});});
      }else throw new Error('Unsupported account action.');
    });return;
  }
  if(mode==='consent'){
    const request=new URLSearchParams(location.search).get('request');
    attempt(async()=>{
      await api('/api/me');const d=await api('/api/account/consent/'+encodeURIComponent(request));
      const box=document.getElementById('consent-details');box.append(el('h2',d.clientName),el('p','Redirect after approval: '+new URL(d.redirectUri).origin));
      const ul=el('ul');const labels={'tools:read':'Read published tools and your private submissions','tools:write':'Save, edit, submit for review and withdraw your tools','profile:write':'Customize your creator profile'};d.scopes.forEach(s=>ul.append(el('li',labels[s]||s)));box.append(ul);
      document.getElementById('consent-actions').hidden=false;
      for(const [id,allow] of [['allow-agent',true],['deny-agent',false]])document.getElementById(id).addEventListener('click',()=>attempt(async()=>{document.getElementById('consent-actions').hidden=true;const result=await api('/api/account/consent/'+encodeURIComponent(request),'POST',{allow});location.assign(result.redirect);}));
    });return;
  }
  if(mode==='review'){
    attempt(async()=>{
      const me=await api('/api/me');if(!me.user.admin)throw new Error('Reviewer access required.');
      const {submissions}=await api('/api/review'), box=document.getElementById('review-queue');
      if(!submissions.length)box.append(el('p','No submissions are waiting for review.'));
      submissions.forEach(row=>{
        const article=el('article',undefined,'submission-row');article.append(el('h2',row.data.name),el('p','Submitted by @'+row.author+' · revision '+row.revision));
        for(const [key,value] of Object.entries(row.data)){article.append(el('h3',key),el('p',value||'None declared.','preserve-lines'));}
        const form=el('form'), label=el('label','Public review scope, or private rejection feedback'), input=el('textarea');input.required=true;input.minLength=5;input.maxLength=4000;input.rows=4;label.append(input);form.append(label);
        for(const [value,text] of [['publish','Approve and publish'],['reject','Return with feedback']]){const b=el('button',text,value==='publish'?'button':'');b.value=value;form.append(b);}
        form.addEventListener('submit',e=>{e.preventDefault();attempt(async()=>{await api('/api/review/'+row.id,'POST',{revision:row.revision,decision:e.submitter.value,evidence:input.value});article.remove();say('Review saved.');});});article.append(form);box.append(article);
      });
    });return;
  }

  let current;
  async function load(){
    current=await api('/api/me');const p=current.profile, form=document.getElementById('profile-form');
    if(p){for(const key of ['handle','displayName','bio','website','avatar'])form.elements[key].value=p[key]||'';form.elements.handle.readOnly=true;form.elements.discoverable.checked=p.discoverable;
      const link=document.getElementById('profile-link');link.replaceChildren();if(p.discoverable){const a=el('a','View public profile →');a.href='/people/'+p.handle+'/';link.append(a);}}
    document.getElementById('verification-panel').hidden=current.user.verified;
    const box=document.getElementById('my-submissions');box.replaceChildren();
    if(!current.submissions.length)box.append(el('p','Your drafts and review updates will appear here.'));
    current.submissions.forEach(row=>{
      const section=el('article',undefined,'submission-row');section.append(el('h3',row.data.name),el('p',row.status+' · revision '+row.revision));if(row.reviewNote)section.append(el('p',row.reviewNote));
      const edit=el('button','Edit draft');edit.type='button';edit.onclick=()=>{const f=document.getElementById('tool-form');for(const [k,v]of Object.entries(row.data))f.elements[k].value=v;f.elements.id.value=row.id;f.elements.revision.value=row.revision;f.scrollIntoView({behavior:'smooth',block:'start'});f.elements.name.focus({preventScroll:true});};section.append(edit);
      if(['draft','rejected'].includes(row.status)){const submit=el('button','Request review');submit.type='button';submit.onclick=()=>attempt(async()=>{await api('/api/me/tools/'+row.id+'/submit','POST',{revision:row.revision});say('Submitted for review.');await load();});section.append(submit);}
      if(row.status!=='withdrawn'){const withdraw=el('button','Withdraw');withdraw.type='button';withdraw.onclick=()=>{if(confirm('Withdraw this tool and remove its public listing, if any?'))attempt(async()=>{await api('/api/me/tools/'+row.id+'/withdraw','POST',{});await load();say('Tool withdrawn.');});};section.append(withdraw);}box.append(section);
    });
    const agents=document.getElementById('agent-connections');agents.replaceChildren();
    if(!current.connections.length)agents.append(el('p','No agents connected yet.'));
    current.connections.forEach(c=>{const row=el('div',undefined,'submission-row'),revoke=el('button','Revoke access');revoke.type='button';revoke.onclick=()=>attempt(async()=>{await api('/api/me/connections/'+encodeURIComponent(c.id),'DELETE');await load();say('Agent access revoked.');});row.append(el('strong',c.clientName),el('p',c.scopes.join(', ')),revoke);agents.append(row);});
    if(current.user.admin&&!document.getElementById('review-link')){const a=el('a','Open review queue');a.id='review-link';a.href='/account/review/';host.prepend(a);}
  }
  document.getElementById('profile-form').addEventListener('submit',e=>{e.preventDefault();attempt(async()=>{const d=fields(e.currentTarget);d.discoverable=e.currentTarget.elements.discoverable.checked;await api('/api/me/profile','PUT',d);await load();say('Profile saved.');});});
  document.getElementById('tool-form').addEventListener('submit',e=>{e.preventDefault();attempt(async()=>{const f=e.currentTarget,d=fields(f),id=d.id,revision=Number(d.revision);delete d.id;delete d.revision;const saved=await api(id?'/api/me/tools/'+id:'/api/me/tools',id?'PUT':'POST',id?{data:d,revision}:d);f.elements.id.value=saved.id;f.elements.revision.value=saved.revision;await load();say('Draft saved. Choose Request review when it is ready.');});});
  document.getElementById('new-draft').onclick=()=>{document.getElementById('tool-form').reset();document.querySelector('#tool-form [name=id]').value='';document.querySelector('#tool-form [name=revision]').value='';};
  document.getElementById('sign-out').onclick=()=>attempt(async()=>{await api('/api/account/logout','POST',{});location.assign('/');});
  document.getElementById('send-verification').onclick=()=>location.assign('/account/sign-in/?next=%2Faccount%2F');
  attempt(load);
})();
