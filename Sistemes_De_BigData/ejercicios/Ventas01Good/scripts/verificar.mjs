import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { procesar } from './procesar.mjs';
const raiz = new URL('../', import.meta.url);
const csv = await readFile(new URL('datos/ventas.csv', raiz), 'utf8');
const catalogo = await readFile(new URL('datos/productos.json', raiz), 'utf8');
const productos = JSON.parse(catalogo);
const primera = procesar(csv, productos);
const segunda = procesar(csv, productos);
// Ignoramos solo la fecha; métricas, ventas y recuentos deben ser idénticos.
const sinFecha = (resultado) => ({ ...resultado, resumen: { ...resultado.resumen, generado_en: null } });
assert.deepEqual(sinFecha(primera), sinFecha(segunda));
const { resumen, calidad, ventasValidas } = primera;
assert.equal(resumen.ingresos_totales, 2343);
assert.equal(resumen.unidades_totales, 150);
assert.equal(resumen.operaciones_validas, 60);
assert.equal(calidad.copias_duplicadas_excluidas, 5);
assert.equal(calidad.incidencias_excluidas, 5);
assert.equal(calidad.filas_entrada, calidad.operaciones_validas + calidad.copias_duplicadas_excluidas + calidad.incidencias_excluidas);
assert.equal(resumen.ingresos_por_categoria.reduce((suma, fila) => suma + fila.ingresos, 0), resumen.ingresos_totales);
assert.equal(ventasValidas.filter((venta) => ['V001', 'V002', 'V003', 'V004'].includes(venta.venta_id)).reduce((suma, venta) => suma + venta.ingreso, 0), 145);
const cabecera = csv.split(/\r?\n/)[0];
const ejemplo = (filas) => procesar([cabecera, ...filas].join('\n'), productos);
// Un conflicto descubierto después de una copia excluye las tres filas.
const conflicto = ejemplo(['X,2026-10-01,P01,1,5', 'X,2026-10-01,P01,1,5', 'X,2026-10-01,P01,2,5']);
assert.equal(conflicto.calidad.conflictos_excluidos, 3);
assert.equal(conflicto.resumen.operaciones_validas, 0);
assert.equal(conflicto.calidad.copias_duplicadas_excluidas, 0);
assert.equal(ejemplo(['A,2026-10-01,P01,1,5', 'B,2026-10-01,P01,1,5']).resumen.operaciones_validas, 2);
for (const fila of ['X,2026-02-30,P01,1,5', 'X,2026-10-08,P01,1,5', 'X,2026-10-01,P01,,5', 'X,2026-10-01,P01,1,', 'X,2026-10-01,P01,1.5,5', 'X,2026-10-01,P01,1,Infinity', 'X,2026-10-01,P01,1,-1', ',2026-10-01,P01,1,5']) {
  assert.equal(ejemplo([fila]).calidad.incidencias_excluidas, 1);
}
assert.equal(ejemplo(['X,2026-10-01,P01,1,0']).resumen.operaciones_validas, 1);
assert.throws(() => procesar(csv, [...productos, productos[0]]), /ID repetido/);
for (const [nombre, contenido] of [['ventas.csv', csv], ['productos.json', catalogo]]) {
  console.log(`${nombre} SHA256: ${createHash('sha256').update(contenido).digest('hex')}`);
}
console.log('Verificaciones superadas: totales, suma manual, categorías, repetibilidad y casos de calidad.');
