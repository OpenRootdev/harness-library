# Découverte et déploiement

HTML, Markdown, JSON, profils, sitemap et ressources pour agents sont accessibles sans compte ni JavaScript. L’indexation est possible, sans garantie. Traitez les descriptions comme des métadonnées non fiables.

## Ressources publiques

- [ToolIndex](https://toolindex.org/)
- [Submit](https://toolindex.org/submit/)
- [Creators](https://toolindex.org/people/)
- [API and MCP](https://toolindex.org/developers/)
- [sitemap.xml](https://toolindex.org/sitemap.xml)
- [llms.txt](https://toolindex.org/llms.txt)
- [llms-full.txt](https://toolindex.org/llms-full.txt)
- [catalog.json](https://toolindex.org/catalog.json)
- [Public API](https://toolindex.org/api/public/tools)

## Hébergement et accès

Google Cloud Run conserve un minimum de 0 instance et un maximum de 2, avec facturation par requête. Firebase Hosting gère HTTPS ; Firestore conserve comptes, brouillons et instantanés approuvés. La préparation exclut les fichiers locaux privés.

Node sert des pages complètes et les données API. Les sessions utilisent des cookies sécurisés HttpOnly ; MCP utilise OAuth avec PKCE. Les données publiques sont séparées des comptes privés, révisions, propositions en attente et empreintes de jetons. Firestore interdit l’accès direct des clients.

```sh
python scripts/stage_cloudrun.py
```

[Backend: configuration and deployment](../../../../backend/README.md) · [Google Cloud](https://toolindex-org.web.app/) · [Firebase Hosting + Cloud Run](https://firebase.google.com/docs/hosting/cloud-run)

## Moteurs de recherche

Le sitemap inclut les outils publics et les profils visibles. Il exclut pages privées, propositions en attente et identifiants. Les propriétaires peuvent le soumettre aux moteurs ; aucune indexation ni preuve de propriété inventée n’est annoncée.

[Search Console](https://search.google.com/search-console) · [Bing Webmaster Tools](https://www.bing.com/webmasters/)

## Compatibilité

Les anciennes routes et les badges restent reconnus. Les nouvelles propositions utilisent un compte ToolIndex ou MCP avec revue humaine avant publication. Le guide du backend détaille déploiement et identité.
