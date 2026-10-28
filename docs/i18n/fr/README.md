<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="ToolIndex"></p>
<h1 align="center">ToolIndex</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">Des outils pour les agents IA. Une configuration claire. Des liens directs vers les sources.</p>
<p align="center"><a href="https://toolindex.org/">toolindex.org</a> · <a href="https://github.com/OpenRootdev/toolindex/issues/new?template=submit-tool.yml">Proposer un outil</a></p>

ToolIndex est un annuaire ouvert de compétences, serveurs MCP, CLI, API, bibliothèques, extensions, workflows et harnesses utilisables par les agents IA. Paquets locaux, services hébergés et outils commerciaux sont acceptés si leur accès, leurs tarifs et leurs conditions sont clairs.

## Quels outils proposer

Des outils utiles pour une tâche précise, du petit dossier de compétences à une API. Chaque fiche renvoie directement au dépôt source ou à la documentation officielle et précise installation ou connexion, configuration manuelle, licence ou conditions, version et portée de la vérification.

## Proposer un outil

1. Ouvrez le formulaire GitHub avec le nom, le type, la source et le but de l’outil.
2. Décrivez le paquet ou service, son installation ou accès, sa version, sa licence ou ses conditions, les identifiants nécessaires et les coûts. Ne publiez aucun secret.
3. Un logo ou une image personnalisée sont facultatifs. Indiquez URL, source et texte alternatif ; sinon la fiche affiche des initiales neutres.
4. Les responsables examinent puis publient les propositions approuvées. Aucun fork, pull request ou compte ToolIndex n’est requis ; le formulaire demande un compte GitHub.

[CONTRIBUTING.md](CONTRIBUTING.md) · [JSON](../../../docs/listing.example.json)

## Exemples examinés

Une compétence d’animation de marque et un connecteur MCP Blender illustrent deux types acceptés. Leurs sources et versions restent dans leurs propres dépôts.

- [Smooth Motion Graphics](https://toolindex.org/tools/smooth-motion-graphics/)
- [ViperMesh for Blender](https://toolindex.org/tools/vipermesh-blender/)

## Construire et prévisualiser

Python 3.11+ génère le site statique. L’interface utilise HTML, CSS et JavaScript ; la recherche enrichit des pages qui restent lisibles sans JavaScript.

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/catalog.py build
python -m http.server 4201 --directory dist
```

`http://localhost:4201/`

## Hébergement Google Cloud

Cloud Run sert le site avec un minimum de 0 instance, un maximum de 2 et une facturation par requête. Firebase Hosting gère HTTPS du domaine et transmet les requêtes à Cloud Run. La préparation du déploiement exclut les fichiers privés du workspace. L’activation du domaine dépend du DNS et du certificat.

`python scripts/stage_cloudrun.py` · [`firebase.json`](../../../firebase.json) · [docs/discovery.md](docs/discovery.md)

## Vérifications et badges communautaires

Les vérifications de configuration et d’artefacts décrivent des preuves précises, pas une compatibilité universelle. Un badge facultatif permet une promotion communautaire transparente de 14 jours. L’attribution Harneloop est facultative ; aucun framework n’est imposé.

[docs/badge-program.md](docs/badge-program.md)
