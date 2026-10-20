# Découverte et indexation

Adresses actuelles depuis le `2026-10-20` : [OpenRootdev/harness-library](https://github.com/OpenRootdev/harness-library) et [annuaire](https://openrootdev.github.io/harness-library/). Les notes historiques ci-dessous décrivent le déplacement précédent.

L'annuaire public publie du HTML complet à des URLs stables. Les moteurs de recherche, les navigateurs sans JavaScript et les agents peuvent lire directement l'installation, les prérequis, l'origine, la distribution et le périmètre d'examen de chaque harness approuvé. JavaScript améliore uniquement le filtrage, la copie et la navigation historique par fragments d'URL.

## Ressources publiques

- [Annuaire](https://openrootdev.github.io/harness-library/) et [guide de soumission](https://openrootdev.github.io/harness-library/submit/).
- [Sitemap](https://openrootdev.github.io/harness-library/sitemap.xml) : uniquement les pages HTML canoniques. Les contrôles quotidiens des badges ne fabriquent pas de dates de modification du contenu.
- [llms.txt](https://openrootdev.github.io/harness-library/llms.txt) : un guide compact reliant les pages d'installation en Markdown et les données.
- [llms-full.txt](https://openrootdev.github.io/harness-library/llms-full.txt) : texte public regroupé.
- [catalog.json](https://openrootdev.github.io/harness-library/catalog.json) : fiches examinées, URLs canoniques, installation, configuration manuelle et preuves au périmètre défini.
- Chaque page HTML canonique possède un `index.md` correspondant, lié avec `rel="alternate" type="text/markdown"`.

Chaque page HTML dispose d'un titre, d'une description et d'une URL canonique uniques, de métadonnées d'aperçu social et de JSON-LD cohérent. Les données structurées décrivent l'annuaire, le mainteneur et les harnesses réels ; elles n'inventent ni évaluations, ni téléchargements, ni compatibilité universelle. Les chemins inconnus renvoient le statut 404 de GitHub Pages avec la page d'erreur noindex. Les anciens liens de fiches par fragments restent pris en charge.

## Configuration du propriétaire

1. Ajoutez une **propriété avec préfixe d'URL** pour `https://openrootdev.github.io/harness-library/` dans [Google Search Console](https://search.google.com/search-console). Cela limite la propriété au projet. Utilisez la méthode de vérification fournie pour votre compte ; un fichier HTML de vérification peut être placé dans `site/` une fois son nom exact et son contenu fournis.
2. Soumettez `sitemap.xml` dans cette propriété. Inspectez les URLs de l'accueil, du guide de soumission et des harnesses ; demandez l'indexation lorsque l'outil le permet. Une soumission est une indication de découverte, pas une promesse d'indexation.
3. Ajoutez le même site à [Bing Webmaster Tools](https://www.bing.com/webmasters/) et soumettez le sitemap. Si le compte propose l'importation depuis Google Search Console, la propriété vérifiée peut être réutilisée.
4. Consultez à nouveau les rapports d'indexation après le déploiement. Corrigez les problèmes d'exploration ou de contenu signalés en vous fondant sur des preuves. Ne considérez pas une recherche `site:` ou un score Lighthouse comme une preuve de couverture d'indexation ou de classement.

La vérification nécessite le compte du propriétaire ou l'artefact de vérification qu'il fournit. Ne publiez pas de jetons de vérification devinés. Si un fichier HTML de vérification est ajouté, excluez-le du sitemap et conservez-le lors des générations.

## Notifications de changements publiés

Après le déploiement d'un push normal, le workflow Pages notifie [IndexNow](https://www.indexnow.org/documentation) avec les URLs canoniques du sitemap généré. Les actualisations quotidiennes des badges omettent cette notification. Cette migration modifie les cinq pages ; pour un annuaire plus grand, limitez les soumissions aux pages modifiées. Google utilise Search Console et l'exploration habituelle ; aucune soumission à Google n'est effectuée via IndexNow.

Le projet héberge `indexnow-key.txt` et fournit son `keyLocation` exact. Cela limite la propriété à `/harness-library/`, évitant les projets sans rapport sur l'hôte partagé. La clé doit être servie publiquement pour la vérification du protocole ; ce n'est pas un identifiant de compte webmaster. Aucun accès connecté, service payant ou dépendance supplémentaire n'est nécessaire. Une panne temporaire de l'API n'annule pas un déploiement réussi du site.

Pour une modification volontaire du contenu hors workflow, générez d'abord le site, puis exécutez `python scripts/notify_indexnow.py --dry-run` pour inspecter la liste des URLs, ou `python scripts/notify_indexnow.py` pour l'envoyer. HTTP 200 signifie reçu ; HTTP 202 signifie reçu, avec validation de la clé en attente. Aucun des deux ne prouve l'indexation ni le classement. Évitez les soumissions répétées lorsque le contenu n'a pas changé.

## GitHub Pages et robots.txt

Les règles robots sont lues à la **racine de l’hôte**, `https://openrootdev.github.io/robots.txt`, et non dans `/harness-library/robots.txt`. Un fichier local au projet ne contrôle pas l’exploration de l’hôte partagé. Le fichier du projet indique seulement le sitemap actuel. Soumettez le sitemap via les comptes webmaster.

Si le propriétaire ajoute ensuite un dépôt pour le site racine ou un domaine personnalisé, vérifiez le fichier robots faisant autorité avant de déployer des restrictions. Ne modifiez jamais à la légère les règles d'autres projets sur le même hôte.

## Migration vers l'organisation

Le dépôt et l'annuaire ont été transférés à [Kaelux Labs](https://github.com/OpenRootdev/harness-library) le 10 octobre 2026. GitHub redirige l'ancienne URL du dépôt. Un petit [dépôt Pages du compte](https://github.com/Ker102/ker102.github.io) conserve les anciennes pages de l'annuaire avec des redirections instantanées et des liens canoniques, et continue de servir les images des badges existants. Son `robots.txt` à la racine de l'hôte autorise l'exploration et pointe vers le sitemap actuel.

Les liens retour des badges utilisant l'ancienne ou l'actuelle URL de l'annuaire restent admissibles. Modifier ces liens ne relance pas une mise en avant existante de 14 jours ; les dates de l'enregistrement initial restent la référence.

## Découverte par les agents

Les agents peuvent utiliser du HTML ordinaire, le catalogue JSON ou les versions Markdown. `llms.txt` est une proposition pratique, pas un facteur de classement Google ni une obligation. Google indique que ses fonctions de recherche par IA suivent les mêmes pratiques fondamentales de SEO que la recherche ordinaire. Le texte explorable, les liens clairs, les preuves exactes et le contenu utile comptent ; aucune configuration ne garantit l'inclusion ou les citations.

Références primaires : [SEO JavaScript de Google](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics), [sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), [spécification robots](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec), [fonctions IA](https://developers.google.com/search/docs/appearance/ai-features), [proposition llms.txt](https://llmstxt.org/).
