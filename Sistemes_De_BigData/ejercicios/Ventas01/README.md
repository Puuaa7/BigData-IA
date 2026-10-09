# Ventas01: auditoría de ventas

Pregunta: ¿qué categorías generan más ingresos entre el 1 y el 7 de octubre de 2026?
Usamos React, Next.js y JavaScript. La página y el layout están en `dashboard/app/*.jsx`.
`README.md` sustituye al antiguo `LEEME.md`. No se han configurado GitHub ni Vercel.

## Ejecutar en localhost

Desde `Sistemes_De_BigData/ejercicios/Ventas01`:

```powershell
node scripts/procesar.mjs
node scripts/verificar.mjs
cd dashboard
npm run dev
```

Abre la dirección que muestre Next.js (normalmente http://localhost:3000).
Si ya tienes el servidor abierto, recarga la página.
Las dependencias ya están instaladas; en una copia nueva ejecuta primero `npm install` dentro de `dashboard`.

## Archivos y actualización

- Fuentes intactas: `datos/ventas.csv` y `datos/productos.json`.
- Proceso: `scripts/procesar.mjs`.
- Resultados: `salida/resumen.json`, `salida/calidad.json` y `salida/ventas.json`.
- Copias para el navegador: `dashboard/public/datos/`, generadas en la misma ejecución.
- `ventas.json` contiene las operaciones válidas enriquecidas para mostrar la tabla.

Para actualizar: ejecuta `node scripts/procesar.mjs` desde Ventas01 y pulsa **Actualizar datos** en la página o recarga el navegador. El botón lee los JSON con `cache: no-store`; no ejecuta el procesamiento. No hay ingestión continua. Los tres archivos deben terminar de generarse antes de actualizar la página.

## Campos, cálculos y limpieza

Se utilizan venta_id, fecha, producto_id, unidades y precio_unitario del CSV; nombre y categoria del catálogo. El cruce se realiza por producto_id mediante un Map. Un ID repetido en el catálogo detiene el proceso para evitar relaciones ambiguas.

Cada ingreso es unidades × precio histórico de la venta, en EUR. Se suman ingresos por categoría y unidades de operaciones válidas. Ingreso no significa beneficio.

Los campos obligatorios vacíos se excluyen antes de aceptar conversiones numéricas. Se exigen unidades enteras positivas, precio finito no negativo, fecha real YYYY-MM-DD dentro del periodo y producto existente. Una copia exacta repite todos los campos; IDs distintos nunca se deduplican por tener el mismo importe.

Se buscan contradicciones antes de aceptar operaciones. Si un ID presenta versiones distintas, todas sus filas son incidencias de conflicto, incluidas sus posibles copias: no elegimos una versión. En IDs sin conflicto, las copias posteriores se cuentan como duplicados; la primera fila se valida. Cada fila ocupa una sola categoría de recuento. Los informes conservan ID, número de fila CSV (primera venta: fila 2) y motivo.

## Resultados y verificaciones realizadas

| Indicador | Resultado |
| --- | ---: |
| Filas de entrada | 70 |
| Operaciones válidas | 60 |
| Unidades | 150 |
| Ingresos EUR | 2343 |
| Copias excluidas | 5 |
| Incidencias excluidas | 5 |
| Filas en conflicto | 0 |

Control: **70 = 60 + 5 + 5**.

| Categoría | Ingresos EUR |
| --- | ---: |
| Papelería | 72 |
| Hogar | 1088 |
| Tecnología | 308 |
| Deporte | 875 |

Suma de categorías: **72 + 1088 + 308 + 875 = 2343 EUR**, igual al total.
Las barras parten de cero y usan la misma escala para comparar categorías. Las cifras del dashboard proceden de los JSON, no de constantes escritas en la interfaz.

Comprobación manual (una copia por operación):

| Venta | Cálculo | Ingreso EUR |
| --- | --- | ---: |
| V001 | 1 × 5 | 5 |
| V002 | 2 × 2 | 4 |
| V003 | 3 × 12 | 36 |
| V004 | 4 × 25 | 100 |

**5 + 4 + 36 + 100 = 145 EUR**. El script de verificación selecciona estas operaciones entre las válidas y obtiene 145 EUR.

Copias excluidas: V003 (fila 62), V011 (63), V021 (64), V036 (65), V049 (66).

| Incidencia | Fila CSV | Tratamiento |
| --- | ---: | --- |
| V061 | 67 | Unidades vacías: excluida |
| V062 | 68 | Precio vacío: excluida |
| V063 | 69 | P99 no existe: excluida |
| V064 | 70 | Unidades negativas: excluida |
| V065 | 71 | Precio «gratis» no numérico: excluida |

El proceso se ejecutó dos veces y las métricas y recuentos coinciden; solo puede variar generado_en. `node scripts/verificar.mjs` comprueba totales, conservación de filas, categorías, suma manual y repetibilidad. Añade ejemplos independientes para conflictos, IDs distintos con datos iguales, fechas imposibles/fuera de periodo, vacíos, unidades fraccionarias, precio infinito/negativo/cero y catálogo duplicado. No modifica las fuentes para probar estos casos.

Las huellas SHA256 de las fuentes coinciden con las previas a los cambios:

- ventas.csv: `493010a84e84d5fea3ef19d02e0ebe9697f91eec349b303fe0c737c99f0ecd06`
- productos.json: `82de3c13418ed305e77ec7d15c11c5479edb8327da0a1c8669738f58b0c010ec`

## Cierre individual: Pau Mas

- Incidencia: V061 tiene unidades vacías; se registra su fila y motivo y no participa en métricas. No se convierte el vacío en cero.
- Copias: se comparan todos los campos originales, incluido venta_id; se conserva una sola operación si no hay conflicto.
- Comprobación: contraste manual de V001–V004, suma de categorías, control de las 70 filas y repetición del proceso.
- Actualización: generar de nuevo los JSON y recargar los datos del navegador; no es automático ni streaming.

## Limitaciones y evidencias pendientes

Datos sintéticos pequeños, cargados en memoria. El lector CSV solo admite el formato controlado sin comillas, comas internas ni saltos dentro de campos. Los números usan la aritmética de JavaScript; estos datos tienen precios enteros. Para importes monetarios arbitrarios con decimales convendría definir una política de precisión y trabajar en céntimos o con aritmética decimal.

La revisión por un compañero, la captura del dashboard y la comprobación de una URL pública quedan pendientes. La publicación y los enlaces de entrega se dejan para otra etapa por petición del alumno. No se afirma haber realizado esas evidencias.

## Validación de la aplicación

`npm run lint` y `npm run build` finalizan correctamente. El servidor existente en http://localhost:3000 responde HTTP 200; sus tres endpoints JSON devuelven 2343 EUR, 60 operaciones, 150 unidades, 5 duplicados, 5 incidencias y 60 filas para la tabla. Esta comprobación HTTP no sustituye a la captura ni a una revisión visual en el navegador.

## Interfaz y gráficos

El panel incluye barras por categoría, barras de ingresos diarios calculadas desde las ventas válidas y una barra de distribución de calidad (válidas, duplicados e incidencias). Todos los importes y recuentos proceden de los JSON. Los gráficos incluyen etiquetas numéricas y las barras parten de cero. La tabla permite buscar por ID, nombre de producto o categoría; la búsqueda solo filtra la tabla, no cambia los indicadores ni los gráficos. El diseño se adapta a pantallas pequeñas.
