# Ventas01Good: auditoría de ventas

Pregunta: ¿qué categorías generan más ingresos del 1 al 7 de octubre de 2026?

Proyecto local con procesamiento en Node.js y dashboard en React y Next.js. Se ha adaptado la implementación existente de Ventas01; las entradas se copiaron de Ventas01Papeleo y se conservan intactas.

## Ejecutar

Desde Ventas01Good:

```powershell
node scripts/procesar.mjs
node scripts/verificar.mjs
cd dashboard
npm.cmd ci
npm.cmd run dev
```

La instalación con `npm.cmd ci` solo es necesaria en una copia nueva o cuando cambian las dependencias. Abre la URL que indique el servidor. `npm.cmd` evita el bloqueo de scripts `.ps1` de PowerShell sin cambiar la política del equipo.

## Estructura

- `datos/`: fuentes CSV y JSON originales.
- `scripts/procesar.mjs`: lectura, validación, deduplicación, cruce y cálculo.
- `scripts/verificar.mjs`: comprobaciones con los datos y ejemplos independientes.
- `salida/`: resumen, informe de calidad y operaciones válidas enriquecidas.
- `dashboard/app/page.jsx`: interfaz y lectura de los JSON.
- `dashboard/app/globals.css`: estilos y barras.
- `dashboard/public/datos/`: copias de resultados que puede leer el navegador.
- `EXPLICACION.md`: explicación del proceso y de las herramientas.

## Reglas y trazabilidad

Se utilizan los cinco campos del CSV y el ID, nombre y categoría del catálogo. Cada ingreso es unidades por precio histórico en EUR; ingreso no equivale a beneficio. Un Map relaciona cada producto con su ID; un ID repetido del catálogo detiene el proceso.

Los campos vacíos se rechazan, las unidades deben ser enteros positivos y los precios finitos no negativos. Las fechas deben ser días reales dentro del periodo. Una referencia de producto inexistente se excluye sin inventar categoría.

Se detectan primero todas las versiones de cada venta_id. Un ID con datos contradictorios excluye todas sus filas como incidencias. En los IDs sin conflicto se conserva la primera copia y se excluyen las posteriores. IDs distintos nunca se deduplican por tener el mismo importe. Cada fila se clasifica una sola vez; los informes incluyen ID, fila CSV y motivo. La primera venta está en la fila 2.

## Resultados comprobados

| Indicador | Valor |
| --- | ---: |
| Filas de entrada | 70 |
| Operaciones válidas | 60 |
| Unidades totales | 150 |
| Ingresos EUR | 2343 |
| Duplicados excluidos | 5 |
| Incidencias excluidas | 5 |

Control: 70 = 60 + 5 + 5.

| Categoría | Ingresos EUR |
| --- | ---: |
| Papelería | 72 |
| Hogar | 1088 |
| Tecnología | 308 |
| Deporte | 875 |

La suma de categorías es 2343 EUR. Hogar es la categoría con más ingresos. Usamos barras desde cero y con una escala común para comparar magnitudes.

Comprobación manual: V001 = 1 × 5 = 5; V002 = 2 × 2 = 4; V003 = 3 × 12 = 36; V004 = 4 × 25 = 100. Suma: 145 EUR, usando una sola copia por operación. El verificador contrasta este subconjunto, los totales, la conservación de filas y dos ejecuciones ignorando únicamente la fecha de generación. También comprueba conflictos, IDs distintos, fechas imposibles y fuera del periodo, vacíos, unidades fraccionarias, precios negativos e infinitos, precio cero y catálogo duplicado.

Copias excluidas: V003 (fila 62), V011 (63), V021 (64), V036 (65), V049 (66).

| Venta | Fila | Incidencia y tratamiento |
| --- | ---: | --- |
| V061 | 67 | Unidades vacías: excluida |
| V062 | 68 | Precio vacío: excluida |
| V063 | 69 | Producto P99 inexistente: excluida |
| V064 | 70 | Unidades negativas: excluida |
| V065 | 71 | Precio «gratis» no numérico: excluida |

## Actualización y publicación

1. Ejecutar `node scripts/procesar.mjs` desde Ventas01Good.
2. El script regenera salida y las copias de dashboard/public/datos.
3. En local, recargar el panel o pulsar Actualizar datos cuando el proceso haya terminado.
4. Para la web publicada, subir los nuevos archivos a GitHub y desplegar otra versión en Vercel. Seleccionar `Ventas01Good/dashboard` como raíz de la aplicación si el repositorio contiene esta ruta; si el repositorio empieza dentro de Ventas01Good, seleccionar `dashboard`.

El botón vuelve a leer los JSON: no procesa las fuentes. No hay streaming ni ingestión continua. Los indicadores y gráficos proceden de los JSON; la búsqueda solo filtra la tabla.

Pendiente de realizar con el alumno: configurar GitHub y Vercel, comprobar la URL pública, tomar una captura, revisión con un compañero y redactar respuestas individuales con sus propias palabras. No se ha publicado el proyecto ni se atribuyen respuestas al alumno.

## Limitaciones

Validación local realizada: `node scripts/verificar.mjs` supera las comprobaciones, `npm.cmd run build` compila correctamente y el servidor de producción en el puerto 3001 responde HTTP 200. Los tres JSON servidos contienen 2343 EUR, 60 operaciones, 150 unidades, 5 duplicados, 5 incidencias y 60 ventas para la tabla. Las huellas SHA256 de ambas fuentes coinciden con las de Ventas01Papeleo. No se ha realizado revisión visual automatizada.

Datos sintéticos pequeños cargados en memoria. El lector solo admite este CSV controlado sin comillas, comas internas ni saltos dentro de campos. El caso no tiene costes, impuestos, descuentos ni devoluciones. Estos precios son enteros; para otros importes decimales debe definirse una política monetaria y considerar céntimos o aritmética decimal. La comprobación HTTP y la compilación no sustituyen una revisión visual en el navegador.
