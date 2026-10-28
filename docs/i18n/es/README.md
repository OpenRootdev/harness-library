<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="ToolIndex"></p>
<h1 align="center">ToolIndex</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="../es/README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">Herramientas para agentes de IA. Configuración clara. Enlaces directos al origen.</p>
<p align="center"><a href="https://toolindex.org/">toolindex.org</a> · <a href="https://github.com/OpenRootdev/toolindex/issues/new?template=submit-tool.yml">Enviar una herramienta</a></p>

ToolIndex es un directorio abierto de habilidades, servidores MCP, CLI, API, bibliotecas, complementos, flujos de trabajo y harnesses que pueden usar los agentes de IA. Se aceptan paquetes locales, servicios alojados y herramientas comerciales si explican acceso, precios y condiciones.

## Qué puedes compartir

Herramientas útiles para una tarea concreta, desde una pequeña carpeta de habilidades hasta una API. Cada ficha enlaza directamente al repositorio de origen o a la documentación oficial y explica instalación o conexión, configuración manual, licencia o condiciones, versión y alcance de la revisión.

## Enviar una herramienta

1. Abre el formulario de GitHub con el nombre, tipo, origen y propósito.
2. Describe el paquete o servicio, instalación o acceso, versión, licencia o condiciones, credenciales necesarias y costes. Nunca envíes secretos.
3. El logotipo o una imagen personalizada son opcionales. Si se añaden, indica URL, origen y texto alternativo; en caso contrario se muestran iniciales neutras.
4. Los responsables revisan y publican las propuestas aprobadas. No hacen falta fork, pull request ni cuenta de ToolIndex; el formulario requiere una cuenta de GitHub.

[CONTRIBUTING.md](CONTRIBUTING.md) · [JSON](../../../docs/listing.example.json)

## Ejemplos revisados

Una habilidad de animación de marca y un conector MCP para Blender muestran dos tipos compatibles. Su código y sus versiones siguen en sus propios repositorios.

- [Smooth Motion Graphics](https://toolindex.org/tools/smooth-motion-graphics/)
- [ViperMesh for Blender](https://toolindex.org/tools/vipermesh-blender/)

## Compilar y previsualizar

Python 3.11+ genera el sitio estático. La interfaz usa HTML, CSS y JavaScript; la búsqueda mejora páginas que siguen siendo legibles sin JavaScript.

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/catalog.py build
python -m http.server 4201 --directory dist
```

`http://localhost:4201/`

## Alojamiento en Google Cloud

Cloud Run sirve el sitio con un mínimo de 0 instancias, un máximo de 2 y facturación por solicitudes. Firebase Hosting gestiona HTTPS y reenvía las solicitudes a Cloud Run. El script de preparación incluye solo archivos públicos y excluye los privados. La activación del dominio depende del DNS y del certificado.

`python scripts/stage_cloudrun.py` · [`firebase.json`](../../../firebase.json) · [docs/discovery.md](docs/discovery.md)

## Revisiones e insignias comunitarias

Las revisiones de configuración y artefactos describen pruebas concretas, no compatibilidad universal. Una insignia opcional permite una promoción comunitaria transparente de 14 días. La atribución a Harneloop es opcional; no se requiere ningún framework.

[docs/badge-program.md](docs/badge-program.md)
