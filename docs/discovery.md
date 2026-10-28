# Discovery and deployment

ToolIndex publishes complete HTML, Markdown mirrors and a reviewed JSON catalog. Search engines and agents can read installation or access instructions, source links, licenses and review scope without JavaScript.

## Public resources

- [ToolIndex](https://toolindex.org/)
- [submit/](https://toolindex.org/submit/)
- [sitemap.xml](https://toolindex.org/sitemap.xml)
- [llms.txt](https://toolindex.org/llms.txt)
- [llms-full.txt](https://toolindex.org/llms-full.txt)
- [catalog.json](https://toolindex.org/catalog.json)

## Google Cloud hosting

Cloud Run serves the site in europe-west1 with minimum 0 instances, maximum 2 and request-based billing. Firebase Hosting provides custom-domain HTTPS and forwards to Cloud Run. Configure domain records using Firebase Hosting, not GitHub Pages. The staging helper builds and copies only public output and container configuration; use its printed path for PUBLIC_CONTEXT. Deployment requires authorized Google Cloud and Firebase CLI access.

```sh
python scripts/stage_cloudrun.py
gcloud run deploy toolindex --source PUBLIC_CONTEXT --project toolindex-org --region europe-west1 --min 0 --max 2 --min-instances 0 --max-instances 2 --cpu-throttling --memory 512Mi --execution-environment gen2 --service-account toolindex-runtime@toolindex-org.iam.gserviceaccount.com --build-service-account projects/toolindex-org/serviceAccounts/toolindex-build@toolindex-org.iam.gserviceaccount.com --allow-unauthenticated
firebase deploy --only hosting --project toolindex-org
```

[Google Cloud](https://toolindex-org.web.app/) · [Firebase Hosting + Cloud Run](https://firebase.google.com/docs/hosting/cloud-run)

## Search engines

Verify the toolindex.org URL-prefix property with the owner’s supplied artifact, then submit sitemap.xml in Search Console and Bing Webmaster Tools. Never invent verification tokens or treat submission as proof of indexing. The root robots.txt allows crawling. IndexNow notifications are optional and are sent only after the matching ownership file and pages are live.

[Search Console](https://search.google.com/search-console) · [Bing Webmaster Tools](https://www.bing.com/webmasters/) · [IndexNow](https://www.indexnow.org/documentation)

## Compatibility and review

Legacy /harnesses/ pages redirect to /tools/. Original badge URLs and labels remain recognized without resetting the one-time 14-day grant. GitHub redirects the former repository to OpenRootdev/toolindex. Review records remain scoped evidence. CI never executes submitted tool code or installs its dependencies.
