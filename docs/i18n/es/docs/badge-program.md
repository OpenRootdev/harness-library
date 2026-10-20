# Listed in Harness Library: impulso comunitario gratuito de 14 días

El programa recompensa a quienes facilitan el descubrimiento de harnesses reutilizables. No hay pagos ni obligación de usar Harneloop.

1. Consigue la aprobación de tu ficha.
2. Copia el fragmento de la insignia desde su página de detalle en el directorio y colócalo dentro de las primeras **30 líneas** del README de la rama predeterminada del repositorio de origen.
3. Mantén la imagen enlazada a tu ficha exacta. La siguiente ejecución de verificación concede un único **período de 14 días**, que comienza en la primera comprobación satisfactoria en UTC.

Ejemplo:

```md
[![Listed in Harness Library](https://openrootdev.github.io/harness-library/badges/your-slug.svg)](https://openrootdev.github.io/harness-library/harnesses/your-slug/)
```

Se admite el Markdown exacto o una imagen HTML enlazada equivalente. El texto alternativo de la imagen debe ser «Listed in Harness Library». Los ejemplos dentro de bloques de código o comentarios HTML no cuentan.

Los enlaces de vuelta `https://openrootdev.github.io/harness-library/#your-slug` emitidos anteriormente siguen siendo válidos y llevan a la página correspondiente. Usa la URL real de la página para las nuevas insignias.

Las fichas activas aparecen antes que las normales, y dentro de cada grupo se ordenan alfabéticamente. Los filtros de búsqueda y categoría siguen aplicándose. El directorio muestra una etiqueta **Community boost** y su fecha de caducidad en la página de detalle. Se trata de una posición promocional; el estado de revisión y las afirmaciones de calidad siguen siendo independientes.

El flujo de trabajo diario de la rama main de confianza lee únicamente metadatos públicos del README en GitHub. Registra la concesión inicial, la caducidad, la presencia más reciente de la insignia y la hora de comprobación en `data/boosts.json`. No ejecuta código del repositorio de un harness. Quitar la insignia detiene el impulso tras la siguiente comprobación. Volver a colocarla solo puede restaurar el tiempo restante del período original. Las concesiones caducadas nunca se renuevan automáticamente. Los envíos duplicados, los cambios de slug o las transferencias de repositorio no dan derecho al mismo harness a una segunda recompensa inicial; los mantenedores revisan su identidad.

Si GitHub no está disponible temporalmente, no se concede ningún impulso nuevo. Las insignias ya comprobadas siguen siendo elegibles durante un máximo de 48 horas sin una nueva comprobación y nunca después de su caducidad original. Tanto la generación estática como el navegador vuelven a comprobar las marcas de tiempo. Los registros requieren aprobación de un mantenedor; cambiar un campo JSON en un envío no puede conceder un impulso.

La insignia puede permanecer tras la caducidad. Cualquier política nueva se debatiría públicamente; no hay promoción recurrente oculta ni posiciones de pago.

Las insignias emitidas antes de la migración a Kaelux Labs en `https://ker102.github.io/harness-library/` siguen siendo válidas. La migración no reinicia el período original de 14 días. Actualiza tanto la imagen como el enlace de vuelta a la nueva dirección canónica cuando te resulte conveniente.
