<p align="center"><img src="../../../site/assets/mark.svg" width="70" alt="Harness Library"></p>
<h1 align="center">Harness Library</h1>
<p align="center"><a href="../../../README.md">English</a> · <a href="README.md">Español</a> · <a href="../zh-CN/README.md">简体中文</a> · <a href="../fr/README.md">Français</a> · <a href="../ja/README.md">日本語</a> · <a href="../de/README.md">Deutsch</a> · <a href="../pt-BR/README.md">Português (Brasil)</a></p>
<p align="center">Descubre, instala y comparte harnesses reutilizables para agentes.</p>
<p align="center"><a href="https://openrootdev.github.io/harness-library/">Explorar la biblioteca</a> · <a href="https://github.com/OpenRootdev/harness-library/issues/new?template=submit-harness.yml">Enviar un harness</a> · <a href="CONTRIBUTING.md">Guía de envío</a></p>

Un directorio abierto de instrucciones, habilidades, herramientas y flujos de trabajo que ayudan a un agente a realizar bien una tarea específica. Un harness puede constar de unos pocos archivos o de una configuración de herramientas más amplia. Cada ficha explica cómo instalarlo, qué configurar manualmente y qué parte del repositorio de origen necesitas.

Las primeras entradas son [Smooth Motion Graphics](https://github.com/Ker102/smooth-motion-graphics) y [ViperMesh for Blender](https://github.com/OpenRootdev/vipermesh-blender). El repositorio existente y las versiones publicadas de ViperMesh se incluyen sin cambios. Harneloop es opcional; los harnesses creados con él pueden mostrar la atribución tras la revisión.

## Ver un harness en acción

El vídeo explicativo de Harneloop muestra el estilo de animación del [harness Smooth Motion Graphics](https://openrootdev.github.io/harness-library/harnesses/smooth-motion-graphics/) de la biblioteca: escenas legibles, conexiones curvas y transiciones suaves. También explica cómo Harneloop construye y mejora unidades de harness.

<p align="center"><a href="https://harneloop.kaelux.dev/media/harneloop-how-it-works.mp4"><img src="https://harneloop.kaelux.dev/media/harneloop-video-poster.png" alt="Ver la demostración silenciosa de gráficos en movimiento de Harneloop" width="860"></a></p>
<p align="center"><a href="https://harneloop.kaelux.dev/media/harneloop-how-it-works.mp4">Ver el vídeo completo · 3:40 · Sin sonido, con explicaciones en pantalla</a></p>

El vídeo se aloja por separado. Consulta el paquete de instalación del propio harness y su renderizador de ejemplo desde su ficha.

## Enviar un harness

**Se aceptan nuevas propuestas.** Buscamos harnesses útiles para programación, investigación, datos, trabajo creativo, Blender y operaciones. Unas pocas habilidades pueden bastar; no es necesario usar Harneloop.

1. [Abre el breve formulario de envío de GitHub](https://github.com/OpenRootdev/harness-library/issues/new?template=submit-harness.yml) e indica tu repositorio y la tarea que ayuda a realizar al agente.
2. Añade pasos de instalación claros, categoría, licencia, alcance de versión/distribución y cualquier configuración manual. Los recuentos de componentes y las pruebas de funcionamiento son opcionales.
3. Un mantenedor revisa la configuración, hace seguimiento en tu issue si es necesario y publica las entradas aprobadas.

**No necesitas un fork, una pull request ni una cuenta de Harness Library.** El formulario requiere una cuenta de GitHub. También puedes enviar una PR que añada un archivo JSON a `data/listings/`. Consulta la [guía pública de envío](https://openrootdev.github.io/harness-library/submit/), [CONTRIBUTING.md](CONTRIBUTING.md) y [la plantilla](../../../docs/listing.example.json).

Un repositorio mixto debe ofrecer un paquete específico o una rama dedicada al harness. Quienes envían propuestas no establecen etiquetas de verificación ni de promoción. Los mantenedores revisan la configuración, el alcance y las pruebas disponibles antes de publicar la ficha. «Artifacts checked» significa que se inspeccionaron los artefactos documentados; no implica que funcione con todos los modelos, plataformas o casos de uso.

## Programa gratuito de insignias

Añade la insignia exacta «Listed in Harness Library» y el enlace de vuelta a la ficha dentro de las primeras 30 líneas del README de origen. Tras la verificación, tu ficha recibe **un único impulso comunitario de 14 días**, claramente identificado en el directorio. El impulso afecta al orden, no al estado de revisión. Es gratuito, opcional y caduca automáticamente. Quitar y volver a añadir la insignia no lo reinicia. [Política y verificación](docs/badge-program.md).

## Desarrollo

No se necesitan dependencias de frontend ni un servicio backend. Python 3.11+ ejecuta el validador y el generador; la interfaz usa HTML, CSS y JavaScript sin frameworks.

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/catalog.py build
python -c "import shutil; shutil.copytree('dist', '.preview/harness-library', dirs_exist_ok=True)"
python -m http.server 4201 --directory .preview
```

Abre `http://localhost:4201/harness-library/`. La copia de vista previa sirve correctamente la ruta base de producción; actualízala después de volver a generar el sitio. Las rutas de recursos y navegación coinciden intencionadamente con la URL del proyecto en GitHub Pages.

`site/layout.html`, `site/style.css` y `scripts/publishing.py` generan páginas HTML completas para el directorio, cada harness, la guía de envío y la página de información. JavaScript añade progresivamente búsqueda, filtros y funciones de copia; el contenido de instalación y la navegación siguen siendo utilizables sin él. Las compilaciones también publican un sitemap, versiones Markdown de las páginas, `llms.txt` y el catálogo JSON revisado. Consulta [Descubrimiento e indexación](docs/discovery.md) para la configuración del propietario y los detalles de rastreo.

`python scripts/catalog.py refresh` verifica las insignias de quienes han optado por participar leyendo el contenido público del README en GitHub. Nunca ejecuta código enviado. GitHub Pages publica la rama main revisada; un flujo de trabajo diario actualiza los registros de insignias y vuelve a generar el sitio. Las comprobaciones de PR externas tienen permisos de solo lectura.

Los datos de origen y los registros de revisión se guardan en este repositorio. El código fuente de los harnesses y los recursos de sus versiones publicadas se guardan en sus propios repositorios. El framework de Harneloop no instala vídeos, dependencias ni rastros privados de desarrollo de los harnesses.
