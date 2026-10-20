<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="Harness Library"></p>
<h1 align="center">Harness Library</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">Découvrez, installez et partagez des harnesses réutilisables pour agents.</p>
<p align="center"><a href="https://openrootdev.github.io/harness-library/">Parcourir la bibliothèque</a> · <a href="https://github.com/OpenRootdev/harness-library/issues/new?template=submit-harness.yml">Proposer un harness</a> · <a href="CONTRIBUTING.md">Guide de soumission</a></p>

Un annuaire ouvert d'instructions, de compétences, d'outils et de workflows qui aident un agent à bien accomplir une tâche précise. Un harness peut se limiter à quelques fichiers ou comprendre un ensemble d'outils plus vaste. Chaque fiche explique comment l'installer, ce qu'il faut configurer manuellement et quelle partie du dépôt source est nécessaire.

Les premières entrées sont [Smooth Motion Graphics](https://github.com/Ker102/smooth-motion-graphics) et [ViperMesh for Blender](https://github.com/OpenRootdev/vipermesh-blender). Le dépôt et les versions publiées existants de ViperMesh sont référencés sans modification. Harneloop est facultatif ; les harnesses créés avec lui peuvent afficher cette attribution après examen.

## Voir un harness en action

La vidéo explicative de Harneloop présente le style d'animation du [harness Smooth Motion Graphics](https://openrootdev.github.io/harness-library/harnesses/smooth-motion-graphics/) de la bibliothèque : scènes lisibles, connexions courbes et transitions calmes. Elle explique aussi comment Harneloop construit et améliore les unités de harness.

<p align="center"><a href="https://harneloop.kaelux.dev/media/harneloop-how-it-works.mp4"><img src="https://harneloop.kaelux.dev/media/harneloop-video-poster.png" alt="Voir la démonstration silencieuse d'animation graphique de Harneloop" width="860"></a></p>
<p align="center"><a href="https://harneloop.kaelux.dev/media/harneloop-how-it-works.mp4">Voir la vidéo complète · 3:40 · Sans son, avec explications à l'écran</a></p>

La vidéo est hébergée séparément. Consultez le paquet d'installation propre au harness et son moteur de rendu d'exemple depuis sa fiche.

## Proposer un harness

**Les nouvelles propositions sont les bienvenues.** Nous recherchons des harnesses utiles pour le développement, la recherche, les données, la création, Blender et les opérations. Quelques compétences peuvent suffire ; l'utilisation de Harneloop n'est pas obligatoire.

1. [Ouvrez le court formulaire GitHub](https://github.com/OpenRootdev/harness-library/issues/new?template=submit-harness.yml) en indiquant votre dépôt et la tâche qu'il aide un agent à accomplir.
2. Ajoutez des étapes d'installation claires, la catégorie, la licence, le périmètre de version/distribution et toute configuration manuelle. Les nombres de composants et les preuves de tests sont facultatifs.
3. Un mainteneur examine la configuration, vous contacte dans votre issue si nécessaire et publie les entrées approuvées.

**Aucun fork, aucune pull request ni aucun compte Harness Library n'est nécessaire.** Le formulaire nécessite un compte GitHub. Vous pouvez aussi envoyer une PR ajoutant un fichier JSON dans `data/listings/`. Consultez le [guide public de soumission](https://openrootdev.github.io/harness-library/submit/), [CONTRIBUTING.md](CONTRIBUTING.md) et [le modèle](../../../docs/listing.example.json).

Un dépôt mixte doit fournir un paquet ciblé ou une branche dédiée au harness. Les auteurs des soumissions ne définissent pas les labels de vérification ou de promotion. Les mainteneurs examinent la configuration, le périmètre et les preuves éventuelles avant de publier la fiche. « Artifacts checked » signifie que les artefacts documentés ont été inspectés ; cela ne garantit pas le fonctionnement avec tous les modèles, plateformes ou cas d'usage.

## Programme gratuit de badges

Ajoutez le badge exact « Listed in Harness Library » et le lien retour vers la fiche dans les 30 premières lignes de votre README source. Après vérification, votre fiche bénéficie d'**une seule mise en avant communautaire de 14 jours**, clairement signalée dans l'annuaire. Cette mise en avant modifie l'ordre d'affichage, pas le statut de l'examen. Elle est gratuite, facultative et expire automatiquement. Retirer puis remettre le badge ne la relance pas. [Politique et vérification](docs/badge-program.md).

## Développement

Aucune dépendance frontend ni aucun service backend n'est nécessaire. Python 3.11+ exécute le validateur et le générateur ; l'interface utilise simplement HTML, CSS et JavaScript.

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/catalog.py build
python -c "import shutil; shutil.copytree('dist', '.preview/harness-library', dirs_exist_ok=True)"
python -m http.server 4201 --directory .preview
```

Ouvrez `http://localhost:4201/harness-library/`. La copie de prévisualisation sert correctement le chemin de base de production ; actualisez-la après chaque nouvelle génération. Les chemins des ressources et de navigation correspondent volontairement à l'URL du projet GitHub Pages.

`site/layout.html`, `site/style.css` et `scripts/publishing.py` génèrent des pages HTML complètes pour l'annuaire, chaque harness, le guide de soumission et la page de présentation. JavaScript ajoute progressivement la recherche, les filtres et la copie ; le contenu d'installation et la navigation restent utilisables sans lui. Les générations publient aussi un sitemap, des versions Markdown des pages, `llms.txt` et le catalogue JSON examiné. Consultez [Découverte et indexation](docs/discovery.md) pour la configuration du propriétaire et les détails d'exploration.

`python scripts/catalog.py refresh` vérifie les badges des participants volontaires en lisant le contenu public des README GitHub. Il n'exécute jamais de code soumis. GitHub Pages publie la branche main examinée ; un workflow quotidien actualise les enregistrements des badges et régénère le site. Les contrôles des PR externes disposent de permissions en lecture seule.

Les données sources et les enregistrements d'examen se trouvent dans ce dépôt. Le code source et les ressources des versions publiées des harnesses se trouvent dans leurs propres dépôts. Le framework Harneloop n'installe aucune vidéo, dépendance ou trace de développement privée des harnesses.
