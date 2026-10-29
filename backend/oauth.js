import { randomBytes } from 'node:crypto';
import { InvalidClientMetadataError, InvalidGrantError, InvalidTokenError, InvalidScopeError, InvalidRequestError } from '@modelcontextprotocol/sdk/server/auth/errors.js';
import { digest, quota, Problem } from './domain.js';

const secret = () => randomBytes(32).toString('base64url');
const clean = v => JSON.parse(JSON.stringify(v));
const live = row => row && row.expiresAt > Date.now();
export const SCOPES = ['tools:read', 'tools:write', 'profile:write'];
export function oauthProvider(store, origin, lookupUser) {
  const resource = origin + '/mcp';
  const checkResource = value => { if (value && String(value) !== resource) throw new InvalidRequestError('Token resource must be ' + resource); };
  const checkScopes = scopes => { if (!scopes.length || scopes.some(s => !SCOPES.includes(s))) throw new InvalidScopeError('Unsupported scope'); };
  function mint(uid, clientId, scopes, grantId) {
    const access = secret(), refresh = secret(), expiresAt = Date.now() + 3600000;
    return {access, refresh, row: {uid, clientId, scopes, grantId, resource, expiresAt, purgeAt: new Date(expiresAt)},
      response: {access_token: access, refresh_token: refresh, expires_in: 3600, token_type: 'Bearer', scope: scopes.join(' ')}};
  }
  function writeTokens(tx, t) {
    tx.set('accessTokens', digest(t.access), t.row);
    tx.set('refreshTokens', digest(t.refresh), {...t.row, used: false, expiresAt: Date.now() + 30 * 86400000, purgeAt: new Date(Date.now() + 31 * 86400000)});
  }
  const provider = {
    clientsStore: {
      getClient: id => store.get('oauthClients', digest(id)),
      async registerClient(client) {
        if (client.token_endpoint_auth_method !== 'none') throw new InvalidClientMetadataError('Use a public PKCE client with token_endpoint_auth_method none');
        if (!client.redirect_uris?.length || client.redirect_uris.length > 10) throw new InvalidClientMetadataError('Register 1 to 10 redirect URIs');
        if (client.client_name && client.client_name.length > 100) throw new InvalidClientMetadataError('Client name is too long');
        for (const uri of client.redirect_uris) {
          const u = new URL(uri), loopback = ['localhost','127.0.0.1','[::1]'].includes(u.hostname);
          if (u.hash || u.username || u.password || !(u.protocol === 'https:' || (u.protocol === 'http:' && loopback))) throw new InvalidClientMetadataError('Use HTTPS or a loopback HTTP redirect without fragments or credentials');
        }
        const saved = clean(client);
        await store.atomic(async tx => { const apply = await quota(tx, 'oauth-registration', 1000); tx.set('oauthClients', digest(client.client_id), saved); apply(); });
        return saved;
      }
    },
    async authorize(client, params, res) {
      checkResource(params.resource);
      const scopes = params.scopes?.length ? params.scopes : SCOPES;
      checkScopes(scopes);
      if (!/^[A-Za-z0-9_-]{43}$/.test(params.codeChallenge)) throw new InvalidRequestError('PKCE S256 is required');
      const requestId = secret();
      await store.atomic(async tx => tx.set('oauthRequests', digest(requestId), {
        clientId: client.client_id, clientName: client.client_name || 'MCP client',
        redirectUri: params.redirectUri, codeChallenge: params.codeChallenge, scopes,
        state: params.state || '', resource, expiresAt: Date.now() + 600000, purgeAt: new Date(Date.now()+600000)
      }));
      res.redirect(302, '/authorize/consent/?request=' + encodeURIComponent(requestId));
    },
    async pending(requestId) {
      const row = await store.get('oauthRequests', digest(requestId));
      if (!live(row)) throw new Problem(400, 'Authorization expired. Reconnect from your agent.');
      return {clientName: row.clientName, redirectUri: row.redirectUri, scopes: row.scopes};
    },
    async consent(user, requestId, allow) {
      const code = secret(), grantId = secret();
      return store.atomic(async tx => {
        const row = await tx.get('oauthRequests', digest(requestId));
        if (!live(row)) throw new Problem(400, 'Authorization expired or already used.');
        const apply = allow ? await quota(tx, 'oauth-grants:' + user.uid, 30) : null;
        const target = new URL(row.redirectUri);
        if (row.state) target.searchParams.set('state', row.state);
        target.searchParams.set('iss', new URL(origin).href);
        if (!allow) target.searchParams.set('error', 'access_denied');
        else {
          tx.set('oauthCodes', digest(code), {...row, uid: user.uid, grantId, expiresAt: Date.now() + 120000, purgeAt: new Date(Date.now()+120000)});
          tx.set('oauthGrants', grantId, {uid: user.uid, clientId: row.clientId, clientName: row.clientName, scopes: row.scopes, revoked: false, createdAt: new Date().toISOString()});
          target.searchParams.set('code', code); apply();
        }
        tx.delete('oauthRequests', digest(requestId)); return target.href;
      });
    },
    async challengeForAuthorizationCode(client, code) {
      const row = await store.get('oauthCodes', digest(code));
      if (!live(row) || row.clientId !== client.client_id) throw new InvalidGrantError('Invalid authorization code');
      return row.codeChallenge;
    },
    async exchangeAuthorizationCode(client, code, _verifier, redirectUri, requestedResource) {
      checkResource(requestedResource);
      return store.atomic(async tx => {
        const row = await tx.get('oauthCodes', digest(code));
        if (!live(row) || row.clientId !== client.client_id || redirectUri !== row.redirectUri) throw new InvalidGrantError('Invalid code or redirect URI');
        const grant = await tx.get('oauthGrants', row.grantId);
        if (!grant || grant.revoked) throw new InvalidGrantError('Grant revoked');
        const t = mint(row.uid, row.clientId, row.scopes, row.grantId);
        tx.delete('oauthCodes', digest(code)); writeTokens(tx, t); return t.response;
      });
    },
    async exchangeRefreshToken(client, token, scopes, requestedResource) {
      checkResource(requestedResource);
      const result = await store.atomic(async tx => {
        const row = await tx.get('refreshTokens', digest(token));
        if (!live(row) || row.clientId !== client.client_id) throw new InvalidGrantError('Invalid refresh token');
        const grant = await tx.get('oauthGrants', row.grantId);
        if (!grant || grant.revoked) throw new InvalidGrantError('Grant revoked');
        if (row.used) { tx.set('oauthGrants', row.grantId, {...grant, revoked: true}); return {reused: true}; }
        const narrowed = scopes || row.scopes;
        if (!narrowed.length || narrowed.some(s => !row.scopes.includes(s))) throw new InvalidScopeError('Cannot expand the granted scopes');
        const t = mint(row.uid, row.clientId, narrowed, row.grantId);
        tx.set('refreshTokens', digest(token), {...row, used: true}); writeTokens(tx, t); return t.response;
      });
      if (result.reused) throw new InvalidGrantError('Refresh token reused. Grant revoked; reconnect your client.');
      return result;
    },
    async verifyAccessToken(token) {
      if (token.length > 200) throw new InvalidTokenError('Invalid token');
      const row = await store.get('accessTokens', digest(token));
      if (!live(row) || row.resource !== resource) throw new InvalidTokenError('Expired or invalid token');
      const grant = await store.get('oauthGrants', row.grantId);
      if (!grant || grant.revoked) throw new InvalidTokenError('Grant revoked');
      const user = await lookupUser(row.uid);
      if (!user || user.disabled) throw new InvalidTokenError('Account unavailable');
      if (user.tokensValidAfterTime && Date.parse(grant.createdAt) < Date.parse(user.tokensValidAfterTime)) throw new InvalidTokenError('Account credentials changed; reconnect.');
      return {token, clientId: row.clientId, scopes: row.scopes, expiresAt: Math.floor(row.expiresAt / 1000), resource: new URL(resource), extra: {uid: row.uid}};
    },
    async revokeToken(client, request) {
      const key = digest(request.token);
      await store.atomic(async tx => {
        const row = await tx.get('refreshTokens', key) || await tx.get('accessTokens', key);
        if (row?.clientId === client.client_id) {
          const grant = await tx.get('oauthGrants', row.grantId);
          if (grant) tx.set('oauthGrants', row.grantId, {...grant, revoked: true});
        }
      });
    },
    async grants(user) { return (await store.list('oauthGrants', {filters: [['uid', user.uid]], limit: 100})).filter(g => !g.revoked).map(g => ({id:g._key, clientName:g.clientName, scopes:g.scopes, createdAt:g.createdAt})); },
    async revokeGrant(user, id) { await store.atomic(async tx => { const g=await tx.get('oauthGrants',id); if (!g || g.uid!==user.uid) throw new Problem(404,'Connection not found'); tx.set('oauthGrants',id,{...g,revoked:true}); }); }
  };
  return provider;
}
