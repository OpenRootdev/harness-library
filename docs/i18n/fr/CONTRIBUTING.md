# Proposer un harness

ToolIndex accueille tous les outils utilisables par les agents IA : compétences, serveurs MCP, CLI, API, bibliothèques, extensions, workflows et harnesses. Les services hébergés et commerciaux sont acceptés si leur accès, leurs tarifs, leur authentification et leurs conditions sont clairs. Chaque fiche renvoie directement au dépôt source ou à la documentation officielle.

Le logo ou une image personnalisée sont facultatifs. Indiquez leur source et un texte alternatif ; sinon la fiche affiche des initiales neutres. Choisissez un type d’outil et expliquez son installation ou l’accès au service. Les sources hors GitHub sont acceptées ; seuls les README GitHub permettent actuellement la vérification automatique des badges.

**Les nouvelles propositions sont les bienvenues.** Nous recherchons des configurations d'agents pratiques et réutilisables, y compris de petits dossiers de compétences. Harneloop est facultatif.

La démarche la plus simple ne nécessite ni fork ni pull request :

1. [Ouvrez le formulaire de soumission GitHub](https://github.com/OpenRootdev/toolindex/issues/new?template=submit-tool.yml). Indiquez le dépôt, le nom et la tâche/catégorie.
2. Expliquez l'installation, la distribution ciblée, la version/licence et les connexions manuelles. Les détails supplémentaires de composition et les preuves de tests sont facultatifs.
3. Les mainteneurs examinent votre issue, y demandent les précisions manquantes si nécessaire et publient les entrées approuvées. Les modifications ultérieures peuvent être soumises dans une autre issue ou PR.

Seul un compte GitHub est nécessaire pour utiliser le formulaire. Le [guide du site](https://toolindex.org/submit/) explique la même procédure.

Pour une PR, copiez `docs/listing.example.json` vers `data/listings/your-slug.json`. Utilisez le même slug en minuscules pour le nom de fichier et `id`. Exécutez `python scripts/catalog.py validate` et les tests décrits dans le README.

Informations obligatoires :

- Nom, bref résumé, catégorie, dépôt source, licence et version ou révision fixée.
- URL de distribution ciblée, son contenu et indication de la présence éventuelle de contenu sans rapport dans le dépôt source. Utilisez un paquet téléchargeable ou une branche dédiée au harness pour les dépôts mixtes ; n'obligez pas les utilisateurs à cloner un grand projet sans rapport.
- Instructions d'installation claires et ordonnées. Précisez le répertoire de travail, les prérequis, l'intégration agent/client et la procédure de démarrage. Ajoutez des liens vers les instructions propres au client lorsque les mécanismes de découverte diffèrent.
- Connexions/configuration manuelles, MCPs ou outils requis, identifiants éventuels et notes complémentaires. Utilisez des listes vides lorsqu'aucun élément n'est requis. Ne soumettez jamais de secrets.

Facultatif : nombres de compétences/références/fichiers, nombre d'outils MCP de premier niveau, outils d'exécution, composition détaillée et attribution « Built with Harneloop » accompagnée de preuves. Distinguez les outils facultatifs des outils requis et les outils de dispatch de premier niveau des opérations en aval.

Catégories autorisées : Creative, 3D & Blender, Coding, Research, Data, Operations, Other. Proposez une nouvelle catégorie dans l'issue si aucune ne convient.

N'ajoutez pas de champs d'examen ou de mise en avant à votre fiche et ne modifiez pas les enregistrements des mainteneurs. Les mainteneurs contrôlent `data/reviews.json` et `data/boosts.json`. L'attribution de l'origine et les affirmations concernant les tests nécessitent des preuves ; un paquet publié ne prouve pas, à lui seul, qu'il fonctionne correctement. Les mainteneurs inspectent les instructions, le périmètre du code source, les licences, les URLs et les artefacts déclarés ; les scripts soumis ne sont jamais exécutés automatiquement.

Gardez les modifications ciblées. Les mises à jour de paquets sources ou des étapes d'installation doivent préciser la version et les changements. Les problèmes d'installation peuvent être signalés dans une issue ordinaire.
