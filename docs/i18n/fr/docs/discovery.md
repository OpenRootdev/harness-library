# Découverte et déploiement

ToolIndex publie du HTML complet, des miroirs Markdown et un catalogue JSON examiné. Moteurs de recherche et agents lisent installation ou accès, sources, licences et portée des vérifications sans JavaScript.

## Ressources publiques

- [ToolIndex](https://toolindex.org/)
- [submit/](https://toolindex.org/submit/)
- [sitemap.xml](https://toolindex.org/sitemap.xml)
- [llms.txt](https://toolindex.org/llms.txt)
- [llms-full.txt](https://toolindex.org/llms-full.txt)
- [catalog.json](https://toolindex.org/catalog.json)

## Hébergement Google Cloud

Cloud Run sert le site dans europe-west1 avec un minimum de 0 instance, un maximum de 2 et une facturation par requête. Firebase Hosting fournit HTTPS et transmet les requêtes. Configurez le DNS avec Firebase Hosting, pas GitHub Pages. Le script prépare uniquement le contenu public et la configuration du conteneur ; utilisez le chemin affiché pour PUBLIC_CONTEXT. Le déploiement nécessite un accès autorisé aux CLI Google Cloud et Firebase.

```sh
python scripts/stage_cloudrun.py
gcloud run deploy toolindex --source PUBLIC_CONTEXT --project toolindex-org --region europe-west1 --min 0 --max 2 --min-instances 0 --max-instances 2 --cpu-throttling --memory 512Mi --execution-environment gen2 --service-account toolindex-runtime@toolindex-org.iam.gserviceaccount.com --build-service-account projects/toolindex-org/serviceAccounts/toolindex-build@toolindex-org.iam.gserviceaccount.com --allow-unauthenticated
firebase deploy --only hosting --project toolindex-org
```

[Google Cloud](https://toolindex-org.web.app/) · [Firebase Hosting + Cloud Run](https://firebase.google.com/docs/hosting/cloud-run)

## Moteurs de recherche

Vérifiez la propriété de préfixe URL toolindex.org avec l’artefact fourni par le propriétaire, puis soumettez sitemap.xml dans Search Console et Bing Webmaster Tools. N’inventez aucun jeton et ne prenez pas la soumission pour une preuve d’indexation. Le robots.txt racine autorise l’exploration. Les notifications IndexNow sont facultatives et ne partent qu’après publication du fichier de propriété et des pages correspondantes.

[Search Console](https://search.google.com/search-console) · [Bing Webmaster Tools](https://www.bing.com/webmasters/) · [IndexNow](https://www.indexnow.org/documentation)

## Compatibilité et vérification

Les anciennes pages /harnesses/ redirigent vers /tools/. Les URL et libellés de badges d’origine restent reconnus sans réinitialiser la promotion unique de 14 jours. GitHub redirige l’ancien dépôt vers OpenRootdev/toolindex. Les preuves restent limitées à leur portée. La CI n’exécute jamais le code des outils soumis et n’installe pas leurs dépendances.
