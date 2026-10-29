import { initializeApp } from 'https://www.gstatic.com/firebasejs/13.1.0/firebase-app.js';
import { initializeAuth, inMemoryPersistence, browserPopupRedirectResolver, GoogleAuthProvider, GithubAuthProvider, signInWithPopup, signOut } from 'https://www.gstatic.com/firebasejs/13.1.0/firebase-auth.js';

// Provider tokens stay in memory. The server session remains the HttpOnly cookie.
export function prepareSocialSignIn(config) {
  const auth = initializeAuth(initializeApp({apiKey:config.apiKey,authDomain:config.authDomain,projectId:config.projectId},'toolindex-social'), {
    persistence:inMemoryPersistence,popupRedirectResolver:browserPopupRedirectResolver
  });
  return async (providerId, consumeToken) => {
    if (!config.signInProviders.includes(providerId)) throw new Error('This sign-in method is unavailable.');
    const provider = providerId==='google.com' ? new GoogleAuthProvider() : new GithubAuthProvider();
    if (providerId==='github.com') provider.addScope('user:email');
    const result = await signInWithPopup(auth,provider);
    try { await consumeToken(await result.user.getIdToken()); }
    finally { await signOut(auth); }
  };
}

export function socialError(error) {
  const code=error.code || '';
  if (code==='auth/popup-closed-by-user' || code==='auth/cancelled-popup-request') return 'Sign-in cancelled. You can try again.';
  if (code==='auth/popup-blocked') return 'Allow the sign-in popup, then choose your provider again.';
  if (code==='auth/account-exists-with-different-credential') return 'This email already uses another sign-in method. Use that method to keep your existing account.';
  if (code==='auth/unauthorized-domain' || code==='auth/operation-not-allowed' || code==='auth/invalid-oauth-client-id') return 'This sign-in provider is being configured. Please use email sign-in for now.';
  return 'Could not complete provider sign-in. Please try again or use email sign-in.';
}
