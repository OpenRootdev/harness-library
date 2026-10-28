# Descoberta e implantação

O ToolIndex publica HTML completo, espelhos Markdown e um catálogo JSON revisado. Buscadores e agentes podem ler instalação ou acesso, origem, licenças e escopo da revisão sem JavaScript.

## Recursos públicos

- [ToolIndex](https://toolindex.org/)
- [submit/](https://toolindex.org/submit/)
- [sitemap.xml](https://toolindex.org/sitemap.xml)
- [llms.txt](https://toolindex.org/llms.txt)
- [llms-full.txt](https://toolindex.org/llms-full.txt)
- [catalog.json](https://toolindex.org/catalog.json)

## Hospedagem no Google Cloud

O Cloud Run serve o site em europe-west1 com mínimo de 0 instâncias, máximo de 2 e cobrança por solicitação. O Firebase Hosting fornece HTTPS e encaminha solicitações. Configure DNS pelo Firebase Hosting, não pelo GitHub Pages. O script prepara apenas conteúdo público e configuração do contêiner; use o caminho impresso em PUBLIC_CONTEXT. A implantação exige acesso autorizado às CLI do Google Cloud e Firebase.

```sh
python scripts/stage_cloudrun.py
gcloud run deploy toolindex --source PUBLIC_CONTEXT --project toolindex-org --region europe-west1 --min 0 --max 2 --min-instances 0 --max-instances 2 --cpu-throttling --memory 512Mi --execution-environment gen2 --service-account toolindex-runtime@toolindex-org.iam.gserviceaccount.com --build-service-account projects/toolindex-org/serviceAccounts/toolindex-build@toolindex-org.iam.gserviceaccount.com --allow-unauthenticated
firebase deploy --only hosting --project toolindex-org
```

[Google Cloud](https://toolindex-org.web.app/) · [Firebase Hosting + Cloud Run](https://firebase.google.com/docs/hosting/cloud-run)

## Buscadores

Verifique a propriedade de prefixo URL de toolindex.org com o arquivo fornecido pelo proprietário e envie sitemap.xml ao Search Console e Bing Webmaster Tools. Não invente tokens nem trate o envio como prova de indexação. O robots.txt raiz permite rastreamento. Notificações IndexNow são opcionais e só são enviadas quando o arquivo de propriedade e as páginas correspondentes estão publicados.

[Search Console](https://search.google.com/search-console) · [Bing Webmaster Tools](https://www.bing.com/webmasters/) · [IndexNow](https://www.indexnow.org/documentation)

## Compatibilidade e revisão

Páginas antigas /harnesses/ redirecionam para /tools/. URLs e rótulos originais dos selos continuam aceitos sem reiniciar o destaque único de 14 dias. O GitHub redireciona o repositório anterior para OpenRootdev/toolindex. Revisões continuam sendo evidências limitadas. A CI nunca executa código de ferramentas enviadas nem instala suas dependências.
