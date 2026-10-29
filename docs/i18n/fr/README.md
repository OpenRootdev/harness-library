<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="ToolIndex"></p>
<h1 align="center">ToolIndex</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">Des outils pour les agents IA. Une configuration claire. Des liens directs vers les sources.</p>
<p align="center"><a href="https://toolindex.org/">toolindex.org</a> · <a href="https://toolindex.org/submit/">Proposer un outil</a></p>

Un répertoire ouvert de compétences, serveurs MCP, CLI, API, bibliothèques, extensions, workflows et harnesses pour les agents IA. Chaque fiche renvoie à sa source et décrit la configuration, la licence ou les conditions et la portée de la revue.

## Comptes et propositions

1. Créez un compte, vérifiez votre adresse et choisissez un identifiant. Personnalisez nom, biographie, site et avatar facultatif. Vous décidez si le profil est public et indexable.
2. Enregistrez un brouillon privé dans l’interface, puis demandez une revue. Les images sont facultatives. Consultez état et retours dans votre compte. Seules les versions approuvées sont publiques ; une modification exige une nouvelle revue, sans masquer la version déjà approuvée.
3. Connectez un agent au point MCP. Au premier usage, le navigateur ouvre la connexion ou création du compte puis un écran de consentement explicite. L’agent gère profil, brouillons et demandes de revue ; il ne peut ni approuver ni publier.

[Account](https://toolindex.org/account/) · [Creators](https://toolindex.org/people/) · [MCP](https://toolindex.org/developers/)

## Découverte publique

HTML, Markdown, JSON, profils, sitemap et ressources pour agents sont accessibles sans compte ni JavaScript. L’indexation est possible, sans garantie. Traitez les descriptions comme des métadonnées non fiables.

[JSON](https://toolindex.org/catalog.json) · [API](https://toolindex.org/api/public/tools) · [llms.txt](https://toolindex.org/llms.txt) · [Sitemap](https://toolindex.org/sitemap.xml)

## Construire et lancer

```sh
python scripts/catalog.py build
npm ci --prefix backend
npm test --prefix backend
npm start --prefix backend
```

Google Cloud Run conserve un minimum de 0 instance et un maximum de 2, avec facturation par requête. Firebase Hosting gère HTTPS ; Firestore conserve comptes, brouillons et instantanés approuvés. La préparation exclut les fichiers locaux privés.

[Backend: accounts, OAuth and deployment](../../../backend/README.md) · [Discovery](docs/discovery.md)

## Exemples examinés

- [Smooth Motion Graphics](https://toolindex.org/tools/smooth-motion-graphics/)
- [ViperMesh for Blender](https://toolindex.org/tools/vipermesh-blender/)

[CONTRIBUTING.md](CONTRIBUTING.md) · [Community badges](docs/badge-program.md)
