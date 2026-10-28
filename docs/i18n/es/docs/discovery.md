# Descubrimiento y despliegue

ToolIndex publica HTML completo, copias Markdown y un catálogo JSON revisado. Buscadores y agentes pueden leer instalación o acceso, origen, licencias y alcance de revisión sin JavaScript.

## Recursos públicos

- [ToolIndex](https://toolindex.org/)
- [submit/](https://toolindex.org/submit/)
- [sitemap.xml](https://toolindex.org/sitemap.xml)
- [llms.txt](https://toolindex.org/llms.txt)
- [llms-full.txt](https://toolindex.org/llms-full.txt)
- [catalog.json](https://toolindex.org/catalog.json)

## Alojamiento en Google Cloud

Cloud Run sirve el sitio en europe-west1 con mínimo de 0 instancias, máximo de 2 y facturación por solicitudes. Firebase Hosting proporciona HTTPS y reenvía a Cloud Run. Configura el DNS con Firebase Hosting, no GitHub Pages. El script prepara solo contenido público y configuración del contenedor; usa la ruta impresa como PUBLIC_CONTEXT. El despliegue requiere acceso autorizado a las CLI de Google Cloud y Firebase.

```sh
python scripts/stage_cloudrun.py
gcloud run deploy toolindex --source PUBLIC_CONTEXT --project toolindex-org --region europe-west1 --min 0 --max 2 --min-instances 0 --max-instances 2 --cpu-throttling --memory 512Mi --execution-environment gen2 --service-account toolindex-runtime@toolindex-org.iam.gserviceaccount.com --build-service-account projects/toolindex-org/serviceAccounts/toolindex-build@toolindex-org.iam.gserviceaccount.com --allow-unauthenticated
firebase deploy --only hosting --project toolindex-org
```

[Google Cloud](https://toolindex-org.web.app/) · [Firebase Hosting + Cloud Run](https://firebase.google.com/docs/hosting/cloud-run)

## Buscadores

Verifica la propiedad de prefijo URL de toolindex.org con el archivo facilitado por su propietario y envía sitemap.xml a Search Console y Bing Webmaster Tools. No inventes tokens ni consideres el envío prueba de indexación. El robots.txt raíz permite el rastreo. Las notificaciones IndexNow son opcionales y solo se envían cuando el archivo de propiedad y las páginas están publicados.

[Search Console](https://search.google.com/search-console) · [Bing Webmaster Tools](https://www.bing.com/webmasters/) · [IndexNow](https://www.indexnow.org/documentation)

## Compatibilidad y revisión

Las rutas antiguas /harnesses/ redirigen a /tools/. Las URL y etiquetas originales de insignias siguen aceptándose sin reiniciar la promoción única de 14 días. GitHub redirige el repositorio anterior a OpenRootdev/toolindex. Las revisiones describen evidencia limitada. CI nunca ejecuta código de herramientas enviadas ni instala sus dependencias.
