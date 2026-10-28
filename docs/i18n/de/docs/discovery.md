# Auffindbarkeit und Bereitstellung

ToolIndex veröffentlicht vollständiges HTML, Markdown-Spiegel und einen geprüften JSON-Katalog. Suchmaschinen und Agenten lesen Installation oder Zugang, Quellen, Lizenzen und Prüfumfang ohne JavaScript.

## Öffentliche Ressourcen

- [ToolIndex](https://toolindex.org/)
- [submit/](https://toolindex.org/submit/)
- [sitemap.xml](https://toolindex.org/sitemap.xml)
- [llms.txt](https://toolindex.org/llms.txt)
- [llms-full.txt](https://toolindex.org/llms-full.txt)
- [catalog.json](https://toolindex.org/catalog.json)

## Google-Cloud-Hosting

Cloud Run betreibt die Website in europe-west1 mit mindestens 0 und höchstens 2 Instanzen und anfragebasierter Abrechnung. Firebase Hosting übernimmt HTTPS und die Weiterleitung. DNS wird mit Firebase Hosting eingerichtet, nicht mit GitHub Pages. Das Staging-Skript kopiert nur öffentliche Ausgabe und Containerkonfiguration; verwende den ausgegebenen Pfad für PUBLIC_CONTEXT. Die Bereitstellung erfordert autorisierten Zugriff auf Google Cloud und Firebase CLI.

```sh
python scripts/stage_cloudrun.py
gcloud run deploy toolindex --source PUBLIC_CONTEXT --project toolindex-org --region europe-west1 --min 0 --max 2 --min-instances 0 --max-instances 2 --cpu-throttling --memory 512Mi --execution-environment gen2 --service-account toolindex-runtime@toolindex-org.iam.gserviceaccount.com --build-service-account projects/toolindex-org/serviceAccounts/toolindex-build@toolindex-org.iam.gserviceaccount.com --allow-unauthenticated
firebase deploy --only hosting --project toolindex-org
```

[Google Cloud](https://toolindex-org.web.app/) · [Firebase Hosting + Cloud Run](https://firebase.google.com/docs/hosting/cloud-run)

## Suchmaschinen

Bestätige die URL-Präfix-Property toolindex.org mit dem vom Eigentümer bereitgestellten Nachweis und reiche sitemap.xml in Search Console und Bing Webmaster Tools ein. Keine Tokens erfinden oder Einreichung als Indexierungsnachweis behandeln. Die robots.txt im Stammverzeichnis erlaubt Crawling. Optionale IndexNow-Meldungen werden erst nach Veröffentlichung der passenden Eigentumsdatei und Seiten gesendet.

[Search Console](https://search.google.com/search-console) · [Bing Webmaster Tools](https://www.bing.com/webmasters/) · [IndexNow](https://www.indexnow.org/documentation)

## Kompatibilität und Prüfung

Alte /harnesses/-Seiten leiten auf /tools/ weiter. Ursprüngliche Badge-URLs und Beschriftungen bleiben gültig, ohne den einmaligen 14-Tage-Boost zurückzusetzen. GitHub leitet das frühere Repository auf OpenRootdev/toolindex um. Prüfungen bleiben begrenzte Nachweise. CI führt eingereichten Werkzeugcode niemals aus und installiert keine seiner Abhängigkeiten.
