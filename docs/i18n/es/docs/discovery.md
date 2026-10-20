# Descubrimiento e indexación

Sede actual desde `2026-10-20`: [OpenRootdev/harness-library](https://github.com/OpenRootdev/harness-library) y el [directorio](https://openrootdev.github.io/harness-library/). Las notas históricas siguientes describen el traslado anterior.

El directorio público publica HTML completo en URLs estables. Los buscadores, los navegadores con JavaScript desactivado y los agentes pueden leer directamente la instalación, los requisitos previos, el origen, la distribución y el alcance de revisión de cada harness aprobado. JavaScript solo mejora el filtrado, la copia y la navegación por fragmentos de URL heredados.

## Recursos públicos

- [Directorio](https://openrootdev.github.io/harness-library/) y [guía de envío](https://openrootdev.github.io/harness-library/submit/).
- [Sitemap](https://openrootdev.github.io/harness-library/sitemap.xml): solo páginas HTML canónicas. Las comprobaciones diarias de insignias no inventan fechas de modificación del contenido.
- [llms.txt](https://openrootdev.github.io/harness-library/llms.txt): una guía compacta con enlaces a páginas de instalación en Markdown y datos.
- [llms-full.txt](https://openrootdev.github.io/harness-library/llms-full.txt): texto público combinado.
- [catalog.json](https://openrootdev.github.io/harness-library/catalog.json): fichas revisadas, URLs canónicas de páginas, instalación, configuración manual y evidencia con alcance definido.
- Cada página HTML canónica tiene un `index.md` correspondiente, enlazado con `rel="alternate" type="text/markdown"`.

Cada página HTML tiene un título, una descripción y una URL canónica únicos, metadatos de vista previa social y JSON-LD coherente. Los datos estructurados describen el directorio, el mantenedor y los harnesses reales; no inventan valoraciones, descargas ni compatibilidad universal. Las rutas desconocidas devuelven el estado 404 de GitHub Pages mediante la página de error noindex. Los antiguos enlaces de fichas con fragmentos siguen siendo compatibles.

## Configuración del propietario

1. Añade una **propiedad de prefijo de URL** para `https://openrootdev.github.io/harness-library/` en [Google Search Console](https://search.google.com/search-console). Esto limita la propiedad al proyecto. Usa el método de verificación proporcionado para tu cuenta; se puede colocar un archivo HTML de verificación en `site/` una vez que se disponga de su nombre y contenido exactos.
2. Envía `sitemap.xml` en esa propiedad. Inspecciona las URLs de inicio, de la guía de envío y de los harnesses; solicita la indexación cuando la herramienta lo permita. El envío es una pista para el descubrimiento, no una promesa de indexación.
3. Añade el mismo sitio a [Bing Webmaster Tools](https://www.bing.com/webmasters/) y envía el sitemap. Si la cuenta ofrece importar desde Google Search Console, puedes reutilizar la propiedad verificada.
4. Vuelve a consultar los informes de indexación tras el despliegue. Corrige los problemas de rastreo o contenido basándote en evidencia. No consideres una búsqueda `site:` ni una puntuación de Lighthouse como prueba de cobertura de indexación o posicionamiento.

La verificación requiere la cuenta del propietario o el artefacto de verificación que esta proporcione. No publiques tokens de verificación inventados. Si se añade un archivo HTML de verificación, mantenlo fuera del sitemap y consérvalo en las compilaciones.

## Notificaciones de cambios publicados

Después de desplegarse un push normal, el flujo de trabajo de Pages notifica a [IndexNow](https://www.indexnow.org/documentation) con las URLs canónicas del sitemap generado. Las actualizaciones diarias de insignias omiten esta notificación. Esta migración cambia las cinco páginas; para un directorio mayor, limita los envíos a las páginas modificadas. Google usa Search Console y el rastreo habitual; no se le envía información mediante IndexNow.

El proyecto aloja `indexnow-key.txt` y proporciona su `keyLocation` exacta. Esto limita la propiedad a `/harness-library/`, evitando proyectos ajenos en el host compartido. La clave debe servirse públicamente para la verificación del protocolo; no es una credencial de una cuenta de webmaster. No se necesita inicio de sesión, servicio de pago ni dependencia adicional. Un fallo temporal de la API no revierte un despliegue satisfactorio del sitio.

Para una actualización deliberada del contenido fuera del flujo de trabajo, genera primero el sitio y ejecuta después `python scripts/notify_indexnow.py --dry-run` para inspeccionar la lista de URLs, o `python scripts/notify_indexnow.py` para enviarla. HTTP 200 significa recibido; HTTP 202 significa recibido con validación de clave pendiente. Ninguno demuestra indexación ni posicionamiento. Evita envíos repetidos cuando el contenido no haya cambiado.

## GitHub Pages y robots.txt

Las reglas de robots se leen desde la **raíz del host**, `https://openrootdev.github.io/robots.txt`, no desde `/harness-library/robots.txt`. Un archivo del proyecto no controla el rastreo del host compartido. El archivo del proyecto solo indica el sitemap actual. Envía el sitemap mediante las cuentas de webmaster.

Si el propietario añade posteriormente un repositorio para el sitio raíz o un dominio personalizado, comprueba el archivo robots autoritativo antes de desplegar restricciones. Nunca cambies sin cuidado las reglas para otros proyectos del mismo host.

## Migración a la organización

El repositorio y el directorio se trasladaron a [Kaelux Labs](https://github.com/OpenRootdev/harness-library) el 10 de octubre de 2026. GitHub redirige la URL del repositorio anterior. Un pequeño [repositorio de Pages de la cuenta](https://github.com/Ker102/ker102.github.io) conserva las páginas del antiguo directorio con redirecciones instantáneas y enlaces canónicos, y sigue sirviendo las imágenes de insignias existentes. Su `robots.txt` en la raíz del host permite el rastreo y enlaza el sitemap actual.

Los enlaces de vuelta de insignias que usen la URL antigua o la actual del directorio siguen siendo elegibles. Cambiarlos no reinicia un impulso existente de 14 días; las fechas del registro original siguen siendo autoritativas.

## Descubrimiento por agentes

Los agentes pueden usar HTML normal, el catálogo JSON o las versiones Markdown. `llms.txt` es una propuesta de conveniencia, no un factor de posicionamiento de Google ni un requisito. Google afirma que sus funciones de búsqueda con IA usan las mismas prácticas fundamentales de SEO que la búsqueda normal. Importan el texto rastreable, los enlaces de página claros, la evidencia precisa y el contenido útil; ninguna configuración garantiza la inclusión ni las citas.

Referencias primarias: [SEO de JavaScript de Google](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics), [sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap), [especificación de robots](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec), [funciones de IA](https://developers.google.com/search/docs/appearance/ai-features), [propuesta llms.txt](https://llmstxt.org/).
