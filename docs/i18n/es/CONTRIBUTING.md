# Lista de requisitos

Un directorio abierto de habilidades, servidores MCP, CLI, API, bibliotecas, complementos, flujos de trabajo y harnesses para agentes de IA. Cada ficha enlaza al origen y explica configuración, licencia o condiciones y alcance de la revisión.

## Cuentas y propuestas

Crea una cuenta, verifica tu correo y elige un identificador de creador. Personaliza nombre, biografía, web y avatar opcional. Tú decides si el perfil es público e indexable.

Guarda un borrador privado en la interfaz y solicita revisión. Las imágenes son opcionales. Consulta estado y comentarios en tu cuenta. Solo se publican revisiones aprobadas; los cambios se revisan de nuevo mientras sigue visible la versión anterior.

Conecta un agente al endpoint MCP. La primera vez, el navegador abre el acceso o registro y una pantalla de permisos explícitos. El agente puede gestionar perfil, borradores y solicitudes de revisión, pero no aprobar ni publicar propuestas.

[UI](https://toolindex.org/account/) · [MCP](https://toolindex.org/developers/) · [Guide](https://toolindex.org/submit/)

## Lista de requisitos

Describe la tarea, origen o documentación oficial, tipo, categoría, versión, licencia o condiciones, instalación o conexión, autenticación y costes. Nunca incluyas secretos.

[JSON example](../../listing.example.json)

## Revisión y propiedad

Solo el propietario edita o retira una propuesta. Solo un revisor verificado y configurado expresamente puede publicarla. La evidencia pública tiene un alcance concreto y no garantiza todos los modelos o plataformas. Los rechazos y propuestas pendientes son privados.

## Contribuciones al código

La interfaz y MCP no requieren issues ni pull requests. Las contribuciones al código siguen siendo bienvenidas. Las fichas iniciales y registros de revisión e insignias permanecen en el repositorio; no modifiques los registros de los mantenedores al proponer una herramienta.

```sh
python scripts/catalog.py validate
python -m unittest discover -s tests -v
python scripts/validate_i18n.py
npm ci --prefix backend
npm test --prefix backend
```

[README.md](README.md) · [Backend](../../../backend/README.md) · [Badge program](docs/badge-program.md)
