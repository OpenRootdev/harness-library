# Informations à fournir

Un répertoire ouvert de compétences, serveurs MCP, CLI, API, bibliothèques, extensions, workflows et harnesses pour les agents IA. Chaque fiche renvoie à sa source et décrit la configuration, la licence ou les conditions et la portée de la revue.

## Comptes et propositions

Créez un compte, vérifiez votre adresse et choisissez un identifiant. Personnalisez nom, biographie, site et avatar facultatif. Vous décidez si le profil est public et indexable.

Enregistrez un brouillon privé dans l’interface, puis demandez une revue. Les images sont facultatives. Consultez état et retours dans votre compte. Seules les versions approuvées sont publiques ; une modification exige une nouvelle revue, sans masquer la version déjà approuvée.

Connectez un agent au point MCP. Au premier usage, le navigateur ouvre la connexion ou création du compte puis un écran de consentement explicite. L’agent gère profil, brouillons et demandes de revue ; il ne peut ni approuver ni publier.

[UI](https://toolindex.org/account/) · [MCP](https://toolindex.org/developers/) · [Guide](https://toolindex.org/submit/)

## Informations à fournir

Décrivez tâche, source ou documentation officielle, type, catégorie, version, licence ou conditions, installation ou connexion, authentification et coûts. Ne transmettez jamais de secrets.

[JSON example](../../listing.example.json)

## Revue et propriété

Seul le propriétaire peut modifier ou retirer une proposition. Seul un réviseur vérifié et explicitement configuré peut publier. Les preuves publiques ont une portée limitée et ne garantissent pas tous les modèles ou plateformes. Les refus et propositions en attente restent privés.

## Contributions au code

L’interface et MCP n’exigent ni issue ni pull request. Les contributions au code restent bienvenues. Fiches initiales, revues et badges restent versionnés ; ne modifiez pas les registres des mainteneurs lors d’une proposition.

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/validate_i18n.py
npm ci --prefix backend
npm test --prefix backend
```

[README.md](README.md) · [Backend](../../../backend/README.md) · [Badge program](docs/badge-program.md)
