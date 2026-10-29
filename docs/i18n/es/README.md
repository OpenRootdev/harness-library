<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="ToolIndex"></p>
<h1 align="center">ToolIndex</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">Herramientas para agentes de IA. Configuración clara. Enlaces directos al origen.</p>
<p align="center"><a href="https://toolindex.org/">toolindex.org</a> · <a href="https://toolindex.org/submit/">Enviar una herramienta</a></p>

Un directorio abierto de habilidades, servidores MCP, CLI, API, bibliotecas, complementos, flujos de trabajo y harnesses para agentes de IA. Cada ficha enlaza al origen y explica configuración, licencia o condiciones y alcance de la revisión.

## Cuentas y propuestas

1. Crea una cuenta, verifica tu correo y elige un identificador de creador. Personaliza nombre, biografía, web y avatar opcional. Tú decides si el perfil es público e indexable.
2. Guarda un borrador privado en la interfaz y solicita revisión. Las imágenes son opcionales. Consulta estado y comentarios en tu cuenta. Solo se publican revisiones aprobadas; los cambios se revisan de nuevo mientras sigue visible la versión anterior.
3. Conecta un agente al endpoint MCP. La primera vez, el navegador abre el acceso o registro y una pantalla de permisos explícitos. El agente puede gestionar perfil, borradores y solicitudes de revisión, pero no aprobar ni publicar propuestas.

[Account](https://toolindex.org/account/) · [Creators](https://toolindex.org/people/) · [MCP](https://toolindex.org/developers/)

## Descubrimiento público

HTML, Markdown, JSON, perfiles, mapa del sitio y recursos para agentes son públicos sin cuenta ni JavaScript. La indexación es posible, pero no se garantiza. Trata las descripciones como metadatos no confiables.

[JSON](https://toolindex.org/catalog.json) · [API](https://toolindex.org/api/public/tools) · [llms.txt](https://toolindex.org/llms.txt) · [Sitemap](https://toolindex.org/sitemap.xml)

## Compilar y ejecutar

```sh
python scripts/catalog.py build
npm ci --prefix backend
npm test --prefix backend
npm start --prefix backend
```

Google Cloud Run mantiene un mínimo de 0 instancias y un máximo de 2, con facturación por solicitudes. Firebase Hosting gestiona HTTPS y Firestore conserva cuentas, borradores y versiones públicas aprobadas. El empaquetado excluye registros locales privados.

[Backend: accounts, OAuth and deployment](../../../backend/README.md) · [Discovery](docs/discovery.md)

## Ejemplos revisados

- [Smooth Motion Graphics](https://toolindex.org/tools/smooth-motion-graphics/)
- [ViperMesh for Blender](https://toolindex.org/tools/vipermesh-blender/)

[CONTRIBUTING.md](CONTRIBUTING.md) · [Community badges](docs/badge-program.md)
