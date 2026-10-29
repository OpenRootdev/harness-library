import { FieldPath, getFirestore } from 'firebase-admin/firestore';

export class FirestoreStore {
  constructor() { this.db = getFirestore(); }
  async get(collection, id) { return (await this.db.collection(collection).doc(id).get()).data(); }
  async list(collection, { filters = [], limit = 1000, after } = {}) {
    let q = this.db.collection(collection);
    for (const [field, value] of filters) q = q.where(field, '==', value);
    q = q.orderBy(FieldPath.documentId()).limit(limit);
    if (after) q = q.startAfter(after);
    return (await q.get()).docs.map(d => ({ ...d.data(), _key: d.id }));
  }
  async atomic(fn) {
    return this.db.runTransaction(t => fn({
      get: async (c, id) => (await t.get(this.db.collection(c).doc(id))).data(),
      set: (c, id, value) => t.set(this.db.collection(c).doc(id), value),
      delete: (c, id) => t.delete(this.db.collection(c).doc(id))
    }));
  }
}

// Used only by isolated tests; production never falls back to process memory.
export class MemoryStore {
  constructor() { this.docs = new Map(); this.queue = Promise.resolve(); }
  async get(c, id) { return structuredClone(this.docs.get(`${c}/${id}`)); }
  async list(c, { filters = [], limit = 1000, after } = {}) {
    return [...this.docs].filter(([key]) => key.startsWith(c + '/')).sort(([a], [b]) => a.localeCompare(b))
      .map(([key, value]) => ({ ...structuredClone(value), _key: key.slice(c.length + 1) }))
      .filter(d => (!after || d._key > after) && filters.every(([k, v]) => d[k] === v)).slice(0, limit);
  }
  atomic(fn) {
    const op = this.queue.then(async () => {
      const copy = new Map(this.docs);
      const result = await fn({ get: async (c, id) => structuredClone(copy.get(`${c}/${id}`)),
        set: (c, id, v) => copy.set(`${c}/${id}`, structuredClone(v)), delete: (c, id) => copy.delete(`${c}/${id}`) });
      this.docs = copy; return result;
    });
    this.queue = op.catch(() => {}); return op;
  }
}
