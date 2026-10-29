# Descubrimiento y despliegue

HTML, Markdown, JSON, perfiles, mapa del sitio y recursos para agentes son públicos sin cuenta ni JavaScript. La indexación es posible, pero no se garantiza. Trata las descripciones como metadatos no confiables.

## Recursos públicos

- [ToolIndex](https://toolindex.org/)
- [Submit](https://toolindex.org/submit/)
- [Creators](https://toolindex.org/people/)
- [API and MCP](https://toolindex.org/developers/)
- [sitemap.xml](https://toolindex.org/sitemap.xml)
- [llms.txt](https://toolindex.org/llms.txt)
- [llms-full.txt](https://toolindex.org/llms-full.txt)
- [catalog.json](https://toolindex.org/catalog.json)
- [Public API](https://toolindex.org/api/public/tools)

## Alojamiento y acceso

Google Cloud Run mantiene un mínimo de 0 instancias y un máximo de 2, con facturación por solicitudes. Firebase Hosting gestiona HTTPS y Firestore conserva cuentas, borradores y versiones públicas aprobadas. El empaquetado excluye registros locales privados.

Node sirve páginas completas y datos API. Las sesiones usan cookies seguras HttpOnly; MCP usa OAuth con PKCE. Los datos públicos se separan de cuentas, historial de revisiones, propuestas pendientes y resúmenes de tokens. Firestore impide el acceso directo de clientes.

```sh
python scripts/stage_cloudrun.py
```

[Backend: configuration and deployment](../../../../backend/README.md) · [Google Cloud](https://toolindex-org.web.app/) · [Firebase Hosting + Cloud Run](https://firebase.google.com/docs/hosting/cloud-run)

## Buscadores

El mapa incluye herramientas públicas y perfiles visibles. No incluye cuentas privadas, propuestas pendientes ni credenciales. Los propietarios pueden enviarlo a buscadores; no se garantiza indexación ni se inventan tokens de propiedad.

[Search Console](https://search.google.com/search-console) · [Bing Webmaster Tools](https://www.bing.com/webmasters/)

## Compatibilidad

Se conservan rutas antiguas y reconocimiento de insignias. Las nuevas propuestas usan cuentas ToolIndex o MCP y revisión humana previa. La guía del backend explica despliegue e identidad.
