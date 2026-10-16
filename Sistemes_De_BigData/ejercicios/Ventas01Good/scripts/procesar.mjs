import { readFile, mkdir, writeFile } from 'node:fs/promises';
import { pathToFileURL } from 'node:url';

const raiz = new URL('../', import.meta.url);
const periodo = { desde: '2026-10-01', hasta: '2026-10-07' };

// Función separada para comprobar las reglas sin modificar los archivos originales.
export function procesar(texto, productos) {
  const indiceProductos = new Map();
  for (const producto of productos) {
    if (!producto.producto_id || !producto.nombre || !producto.categoria) throw new Error('Producto incompleto');
    if (indiceProductos.has(producto.producto_id)) throw new Error(`ID repetido en catálogo: ${producto.producto_id}`);
    indiceProductos.set(producto.producto_id, producto);
  }
  // Este lector solo sirve para el CSV controlado, sin comillas ni comas internas.
  const lineas = texto.trimEnd().split(/\r?\n/);
  const columnas = lineas.shift().split(',');
  const obligatorios = ['venta_id', 'fecha', 'producto_id', 'unidades', 'precio_unitario'];
  if (columnas.join(',') !== obligatorios.join(',')) throw new Error('Cabecera incorrecta');
  const filas = lineas.map((linea, i) => {
    const campos = linea.split(',');
    return {
      venta: Object.fromEntries(columnas.map((campo, j) => [campo, campos[j] ?? ''])),
      firma: JSON.stringify(campos), estructuraValida: campos.length === columnas.length, fila_csv: i + 2,
    };
  });
  // Buscamos todas las versiones antes de aceptar ventas: un conflicto excluye todo el ID.
  const versiones = new Map();
  for (const { venta, firma } of filas) {
    if (!venta.venta_id.trim()) continue;
    if (!versiones.has(venta.venta_id)) versiones.set(venta.venta_id, new Set());
    versiones.get(venta.venta_id).add(firma);
  }
  const vistas = new Set();
  const duplicados = [], incidencias = [], ventasValidas = [];
  for (const { venta, firma, estructuraValida, fila_csv } of filas) {
    const registro = { venta_id: venta.venta_id, fila_csv };
    if (versiones.get(venta.venta_id)?.size > 1) {
      incidencias.push({ ...registro, motivo: 'Conflicto: mismo ID con datos distintos' });
      continue;
    }
    if (venta.venta_id.trim() && vistas.has(firma)) {
      duplicados.push({ ...registro, motivo: 'Copia exacta de una operación anterior' });
      continue;
    }
    vistas.add(firma);
    const motivos = [];
    if (!estructuraValida) motivos.push('Número de campos incorrecto');
    for (const campo of obligatorios) {
      if (!venta[campo].trim()) motivos.push(`Campo obligatorio vacío: ${campo}`);
    }
    const fecha = new Date(`${venta.fecha}T00:00:00Z`);
    if (!/^\d{4}-\d{2}-\d{2}$/.test(venta.fecha) || !Number.isFinite(fecha.getTime()) ||
        fecha.toISOString().slice(0, 10) !== venta.fecha || venta.fecha < periodo.desde || venta.fecha > periodo.hasta) {
      motivos.push('Fecha inválida o fuera del periodo');
    }
    // Los vacíos ya se han registrado: nunca los aceptamos como cero.
    const unidades = Number(venta.unidades), precio = Number(venta.precio_unitario);
    if (venta.unidades.trim() && (!Number.isInteger(unidades) || unidades <= 0)) motivos.push('Unidades: entero mayor que cero');
    if (venta.precio_unitario.trim() && (!Number.isFinite(precio) || precio < 0)) motivos.push('Precio: número finito mayor o igual que cero');
    const producto = indiceProductos.get(venta.producto_id);
    if (!producto) motivos.push('Producto inexistente en el catálogo');
    const ingreso = unidades * precio;
    if (!Number.isFinite(ingreso)) motivos.push('Ingreso no finito');
    if (motivos.length) {
      incidencias.push({ ...registro, motivo: motivos.join('; ') });
      continue;
    }
    ventasValidas.push({ ...venta, ...producto, unidades, precio_unitario: precio, ingreso });
  }
  const categorias = new Map();
  for (const venta of ventasValidas) categorias.set(venta.categoria, (categorias.get(venta.categoria) ?? 0) + venta.ingreso);
  const resumen = {
    periodo, moneda: 'EUR', generado_en: new Date().toISOString(), operaciones_validas: ventasValidas.length,
    unidades_totales: ventasValidas.reduce((suma, venta) => suma + venta.unidades, 0),
    ingresos_totales: ventasValidas.reduce((suma, venta) => suma + venta.ingreso, 0),
    ingresos_por_categoria: [...categorias].map(([categoria, ingresos]) => ({ categoria, ingresos })),
  };
  const calidad = {
    filas_entrada: filas.length, operaciones_validas: ventasValidas.length,
    copias_duplicadas_excluidas: duplicados.length, incidencias_excluidas: incidencias.length,
    conflictos_excluidos: incidencias.filter((fila) => fila.motivo.startsWith('Conflicto:')).length,
    duplicados, incidencias,
  };
  if (filas.length !== ventasValidas.length + duplicados.length + incidencias.length) throw new Error('Los recuentos no cuadran');
  return { resumen, calidad, ventasValidas };
}

async function main() {
  const texto = await readFile(new URL('datos/ventas.csv', raiz), 'utf8');
  const productos = JSON.parse(await readFile(new URL('datos/productos.json', raiz), 'utf8'));
  const { resumen, calidad, ventasValidas } = procesar(texto, productos);
  // Copias para el navegador: al ejecutar de nuevo, también se actualiza el dashboard.
  for (const carpeta of ['salida/', 'dashboard/public/datos/']) {
    await mkdir(new URL(carpeta, raiz), { recursive: true });
    for (const [nombre, datos] of Object.entries({ resumen, calidad, ventas: ventasValidas })) {
      await writeFile(new URL(`${carpeta}${nombre}.json`, raiz), JSON.stringify(datos, null, 2) + '\n');
    }
  }
  console.log(resumen);
  console.log(`Control: ${calidad.filas_entrada} = ${calidad.operaciones_validas} válidas + ${calidad.copias_duplicadas_excluidas} duplicados + ${calidad.incidencias_excluidas} incidencias`);
}
if (process.argv[1] && pathToFileURL(process.argv[1]).href === import.meta.url) await main();
