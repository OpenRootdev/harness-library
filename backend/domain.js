import { randomUUID, createHash } from 'node:crypto';
import { z } from 'zod';

export const TYPES = ['Skill', 'MCP server', 'CLI', 'API', 'Library', 'Plugin', 'Workflow', 'Harness', 'Other'];
export const CATEGORIES = ['Creative', '3D & Blender', 'Coding', 'Research', 'Data', 'Operations', 'Other'];
export class Problem extends Error { constructor(status, message) { super(message); this.status = status; } }
export const digest = value => createHash('sha256').update(value).digest('hex');
export const plain = (max, min = 0) => z.string().trim().min(min).max(max).refine(v => !/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/.test(v), 'Unsupported control character');
export const webURL = z.string().max(2048).url().refine(s => {
  const u = new URL(s); return u.protocol === 'https:' && !u.username && !u.password;
}, 'Use a public HTTPS URL without credentials');
const optionalURL = z.union([z.literal(''), webURL]).default('');
export const profileSchema = z.object({
  handle: z.string().regex(/^[a-z][a-z0-9-]{2,31}$/).refine(v => !['admin','api','account','toolindex','support','moderation','oauth','tools'].includes(v), 'Reserved handle'),
  displayName: plain(80, 1), bio: plain(1000).default(''), website: optionalURL,
  avatar: optionalURL, discoverable: z.boolean().default(true)
}).strict();
export const toolSchema = z.object({
  name: plain(100, 2), summary: plain(300, 10), type: z.enum(TYPES), category: z.enum(CATEGORIES),
  repository: webURL, version: plain(80, 1), license: plain(250, 1),
  installation: plain(8000, 10), manualSetup: plain(4000).default(''), pricing: plain(1000).default(''),
  imageUrl: optionalURL, imageAlt: plain(150).default(''), imageSource: optionalURL
}).strict().superRefine((v, ctx) => {
  if (v.imageUrl && (!v.imageAlt || !v.imageSource)) ctx.addIssue({code: 'custom', message: 'Images need alt text and a source URL'});
});

export const nowISO = () => new Date().toISOString();
export function verified(user) { if (!user.email_verified) throw new Problem(403, 'Verify your email before publishing a profile or submitting a tool.'); }
export async function quota(tx, key, maximum) {
  const id = digest(key + ':' + nowISO().slice(0, 10));
  const row = await tx.get('quotas', id) || {count: 0};
  if (row.count >= maximum) throw new Problem(429, 'Daily limit reached. Please try tomorrow.');
  return () => tx.set('quotas', id, {count: row.count + 1, expiresAt: Date.now() + 172800000, purgeAt: new Date(Date.now() + 172800000)});
}

export function domain(store, baseCatalog, origin) {
  const publicProfile = p => ({handle: p.handle, displayName: p.displayName, bio: p.bio, website: p.website, avatar: p.avatar, url: origin + '/people/' + p.handle + '/'});
  return {
    async profile(user) { return await store.get('profiles', user.uid) || null; },
    async saveProfile(user, input) {
      verified(user); const p = profileSchema.parse(input);
      await store.atomic(async tx => {
        const old = await tx.get('profiles', user.uid), handle = await tx.get('handles', p.handle);
        if (old && old.handle !== p.handle) throw new Problem(409, 'Your profile handle cannot be changed.');
        if (handle && handle.uid !== user.uid) throw new Problem(409, 'That handle is already in use.');
        tx.set('handles', p.handle, {uid: user.uid}); tx.set('profiles', user.uid, {...p, updatedAt: nowISO()});
        if (p.discoverable) tx.set('publicProfiles', p.handle, publicProfile(p));
        else tx.delete('publicProfiles', p.handle);
      }); return p;
    },
    async publishedProfiles(after, limit = 50) {
      return (await store.list('publicProfiles', {after, limit})).map(({_key, ...p}) => p);
    },
    async publishedProfile(handle) { const p = await store.get('publicProfiles', handle); if (!p) throw new Problem(404, 'Profile not found'); return p; },
    async catalog() {
      const rows = await store.list('publicTools');
      return {...baseCatalog, generated_at: nowISO(), listings: [...baseCatalog.listings, ...rows.map(({_key, ...e}) => e)], page_limit: 1000};
    },
    async publicPage({after, limit = 50, query = ''} = {}) {
      // Advance across the underlying stream, even when a search page has no matches.
      const block = await store.list('publicTools', {after, limit: 100});
      const base = baseCatalog.listings.filter(e => !after || e.id > after);
      const candidates = [...base, ...block.map(({_key,...e})=>e)].sort((a,b)=>a.id.localeCompare(b.id));
      const scanned = candidates.slice(0,limit);
      const q = query.toLowerCase();
      return {tools: scanned.filter(e=>[e.name,e.summary,e.type,e.category].join(' ').toLowerCase().includes(q)),
        next: scanned.length && (candidates.length > limit || block.length === 100) ? scanned.at(-1).id : null};
    },
    async mine(user) { return (await store.list('submissions', {filters: [['ownerUid', user.uid]], limit: 100})).map(({_key, ...e}) => e); },
    async saveTool(user, input, id, expectedRevision) {
      verified(user); const data = toolSchema.parse(input);
      const profile = await store.get('profiles', user.uid);
      if (!profile) throw new Problem(409, 'Create your profile first.');
      const key = id || (data.name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 60) || 'tool') + '-' + randomUUID().slice(0, 8);
      return store.atomic(async tx => {
        const row = await tx.get('submissions', key);
        if (id && (!row || row.ownerUid !== user.uid)) throw new Problem(404, 'Submission not found');
        if (row && row.revision !== expectedRevision) throw new Problem(409, 'This submission changed. Reload before saving.');
        const count = !row ? await quota(tx, 'submissions:' + user.uid, 10) : null;
        const saved = {id: key, ownerUid: user.uid, author: profile.handle, data, revision: (row?.revision || 0) + 1,
          status: 'draft', createdAt: row?.createdAt || nowISO(), updatedAt: nowISO(), reviewNote: ''};
        tx.set('submissions', key, saved);
        tx.set('submissionRevisions', key + '-r' + saved.revision, {...saved});
        count?.(); return saved;
      });
    },
    async submit(user, id, revision) {
      verified(user); return store.atomic(async tx => {
        const row = await tx.get('submissions', id);
        if (!row || row.ownerUid !== user.uid) throw new Problem(404, 'Submission not found');
        if (row.revision !== revision || !['draft','rejected'].includes(row.status)) throw new Problem(409, 'Reload this submission before requesting review.');
        row.status = 'submitted'; row.submittedAt = nowISO(); tx.set('submissions', id, row); return row;
      });
    },
    async withdraw(user, id) {
      return store.atomic(async tx => {
        const row = await tx.get('submissions', id);
        if (!row || row.ownerUid !== user.uid) throw new Problem(404, 'Submission not found');
        row.status = 'withdrawn'; row.updatedAt = nowISO(); tx.set('submissions', id, row); tx.delete('publicTools', id); return row;
      });
    },
    async queue() { return (await store.list('submissions', {filters: [['status','submitted']], limit: 100})).map(({_key,...e}) => e); },
    async review(reviewer, id, revision, decision, evidence) {
      if (!reviewer.admin) throw new Problem(403, 'Reviewer access required');
      const message = plain(4000, 5).parse(evidence);
      if (!['publish','reject'].includes(decision)) throw new Problem(400, 'Unknown review decision');
      return store.atomic(async tx => {
        const row = await tx.get('submissions', id);
        if (!row || row.status !== 'submitted' || row.revision !== revision) throw new Problem(409, 'This review is out of date. Reload the queue.');
        row.status = decision === 'publish' ? 'published' : 'rejected'; row.reviewNote = message; row.reviewedAt = nowISO();
        tx.set('submissions', id, row);
        tx.set('reviewEvents', id + '-r' + revision + '-' + randomUUID().slice(0,8), {id, revision, reviewerUid: reviewer.uid, decision, evidence: message, reviewedAt: row.reviewedAt});
        if (decision === 'publish') tx.set('publicTools', id, {
          id, name: row.data.name, summary: row.data.summary, type: row.data.type, category: row.data.category,
          repository: row.data.repository, version: row.data.version, license: row.data.license,
          distribution: {kind: 'focused-repository', url: row.data.repository, label: 'Source or documentation', scope: row.data.installation},
          installation: [{title: 'Installation or connection', body: row.data.installation}],
          manual_setup: [row.data.manualSetup || 'None declared.'], pricing: row.data.pricing,
          author: row.author, url: origin + '/tools/' + id + '/',
          ...(row.data.imageUrl ? {image: {url: row.data.imageUrl, alt: row.data.imageAlt, source: row.data.imageSource}} : {}),
          review: {status: 'setup-reviewed', reviewed_at: nowISO().slice(0,10), evidence: message, built_with_harneloop: false},
          publishedAt: nowISO(), revision
        });
        return row;
      });
    }
  };
}
