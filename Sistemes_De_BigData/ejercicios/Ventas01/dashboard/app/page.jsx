"use client";

import { useEffect, useState } from "react";

async function leerDatos() {
  // Leemos las copias generadas por el script, sin reutilizar datos antiguos.
  const resultados = await Promise.all(["resumen", "calidad", "ventas"].map(async (nombre) => {
    const respuesta = await fetch(`/datos/${nombre}.json`, { cache: "no-store" });
    if (!respuesta.ok) throw new Error("No se pueden cargar los datos. Ejecuta node scripts/procesar.mjs desde Ventas01.");
    return respuesta.json();
  }));
  return { resumen: resultados[0], calidad: resultados[1], ventas: resultados[2] };
}

export default function Home() {
  const [datos, setDatos] = useState(null);
  const [error, setError] = useState("");
  const [busqueda, setBusqueda] = useState("");

  async function cargar() {
    try {
      const nuevosDatos = await leerDatos();
      setError("");
      setDatos(nuevosDatos);
    } catch (error) {
      setError(error.message);
    }
  }

  useEffect(() => {
    let activo = true;
    leerDatos().then((resultado) => { if (activo) setDatos(resultado); })
      .catch((error) => { if (activo) setError(error.message); });
    return () => { activo = false; };
  }, []);
  const euros = (valor) => new Intl.NumberFormat("es-ES", { style: "currency", currency: "EUR" }).format(valor);
  const fecha = (valor) => new Date(`${valor}T00:00:00Z`).toLocaleDateString("es-ES", { timeZone: "Europe/Madrid" });

  return (
    <main className="panel">
      <header className="cabecera">
        <div><p className="etiqueta">VENTAS01 / PANEL DE ANÁLISIS</p><h1>Cada venta, en perspectiva.</h1><p>Ingresos, actividad y calidad de los datos en un solo lugar.</p></div>
        <button onClick={cargar}>Actualizar datos</button>
      </header>
      {error && <p role="alert" className="aviso">{error}</p>}
      {!datos && !error && <p role="status">Cargando resultados…</p>}
      {datos && (() => {
        const { resumen, calidad, ventas } = datos;
        const maximo = Math.max(1, ...resumen.ingresos_por_categoria.map((fila) => fila.ingresos));
        // Sumamos solo ventas válidas. También mostramos los días sin ventas.
        const dias = [];
        for (let dia = new Date(`${resumen.periodo.desde}T00:00:00Z`); dia.toISOString().slice(0, 10) <= resumen.periodo.hasta; dia.setUTCDate(dia.getUTCDate() + 1)) {
          const fechaDia = dia.toISOString().slice(0, 10);
          dias.push({ fecha: fechaDia, ingresos: ventas.filter((venta) => venta.fecha === fechaDia).reduce((suma, venta) => suma + venta.ingreso, 0) });
        }
        const maximoDiario = Math.max(1, ...dias.map((dia) => dia.ingresos));
        const gruposCalidad = [
          { nombre: "Válidas", cantidad: calidad.operaciones_validas, color: "#087c79" },
          { nombre: "Duplicados", cantidad: calidad.copias_duplicadas_excluidas, color: "#b9770e" },
          { nombre: "Incidencias", cantidad: calidad.incidencias_excluidas, color: "#bd4760" },
        ];
        const ventasVisibles = ventas.filter((venta) => `${venta.venta_id} ${venta.nombre} ${venta.categoria}`.toLocaleLowerCase("es").includes(busqueda.toLocaleLowerCase("es")));
        return <>
          <p className="periodo">Periodo: {fecha(resumen.periodo.desde)} – {fecha(resumen.periodo.hasta)} · Generado: {new Date(resumen.generado_en).toLocaleString("es-ES", { timeZone: "Europe/Madrid" })} (Madrid)</p>
          <section className="metricas" aria-label="Indicadores de ventas">
            {[["Ingresos totales (EUR)", euros(resumen.ingresos_totales)], ["Operaciones válidas", resumen.operaciones_validas], ["Unidades vendidas", resumen.unidades_totales], ["Duplicados excluidos", calidad.copias_duplicadas_excluidas], ["Incidencias excluidas", calidad.incidencias_excluidas]].map(([titulo, valor]) => <article className="tarjeta" key={titulo}><h2>{titulo}</h2><strong>{valor}</strong></article>)}
          </section>
          <div className="graficos">
          <section className="bloque">
            <h2>Ingresos por categoría</h2>
            <p>Las barras permiten comparar categorías sobre una misma escala, desde cero.</p>
            {resumen.ingresos_por_categoria.map(({ categoria, ingresos }) => <div className="categoria" key={categoria}><div className="fila"><span>{categoria}</span><strong>{euros(ingresos)}</strong></div><div className="pista"><div className="barra" style={{ width: `${ingresos / maximo * 100}%` }} /></div></div>)}
            <div className="escala"><span>0 EUR</span><span>{euros(maximo)}</span></div>
          </section>
          <section className="bloque">
            <h2>Ingresos por día</h2><p>Actividad diaria de las operaciones válidas, en EUR.</p>
            <div className="grafico-diario" role="img" aria-label={dias.map((dia) => `${fecha(dia.fecha)}: ${euros(dia.ingresos)}`).join('; ')}>
              {dias.map((dia) => <div className="columna-dia" key={dia.fecha}><strong>{euros(dia.ingresos)}</strong><div className="espacio-barra"><div className="barra-dia" title={`${fecha(dia.fecha)}: ${euros(dia.ingresos)}`} style={{ height: `${dia.ingresos / maximoDiario * 100}%` }} /></div><span>{dia.fecha.slice(8)}/{dia.fecha.slice(5, 7)}</span></div>)}
            </div><p className="nota">Escala desde cero · cada barra representa un día.</p>
          </section>
          </div>
          <section className="bloque calidad-visual">
            <div><h2>De la entrada al resultado</h2><p>Cada fila pertenece a un único grupo.</p></div>
            <div className="calidad-contenido"><div className="barra-calidad" role="img" aria-label={gruposCalidad.map((grupo) => `${grupo.nombre}: ${grupo.cantidad}`).join('; ')}>{gruposCalidad.map((grupo) => <div key={grupo.nombre} title={`${grupo.nombre}: ${grupo.cantidad}`} style={{ width: `${grupo.cantidad / Math.max(1, calidad.filas_entrada) * 100}%`, background: grupo.color }} />)}</div><div className="leyenda">{gruposCalidad.map((grupo) => <span key={grupo.nombre}><i style={{ background: grupo.color }} />{grupo.nombre} <strong>{grupo.cantidad}</strong></span>)}</div></div>
          </section>
          <section className="bloque">
            <h2>Ventas válidas</h2><p>Una fila por operación, relacionada con el catálogo de productos.</p>
            <div className="filtros"><label htmlFor="buscar">Buscar por ID, producto o categoría<input id="buscar" type="search" placeholder="Ej.: V003, Taza, Hogar…" value={busqueda} onChange={(evento) => setBusqueda(evento.target.value)} /></label><span aria-live="polite">{ventasVisibles.length} de {ventas.length} operaciones</span></div>
            <div className="tabla"><table><caption>Operaciones incluidas en los indicadores</caption><thead><tr>{["ID", "Fecha", "Producto", "Categoría", "Unidades", "Precio (EUR)", "Ingreso (EUR)"].map((campo) => <th key={campo} scope="col">{campo}</th>)}</tr></thead><tbody>{ventasVisibles.map((venta) => <tr key={venta.venta_id}><td>{venta.venta_id}</td><td>{fecha(venta.fecha)}</td><td>{venta.nombre}</td><td>{venta.categoria}</td><td>{venta.unidades}</td><td>{euros(venta.precio_unitario)}</td><td>{euros(venta.ingreso)}</td></tr>)}</tbody></table></div>
          </section>
          <section className="bloque">
            <h2>Control de calidad</h2><p>{calidad.filas_entrada} filas = {calidad.operaciones_validas} válidas + {calidad.copias_duplicadas_excluidas} duplicados + {calidad.incidencias_excluidas} incidencias. Conflictos excluidos: {calidad.conflictos_excluidos}.</p>
            {[ ["Duplicados", calidad.duplicados], ["Incidencias", calidad.incidencias] ].map(([titulo, registros]) => <details key={titulo}><summary>{titulo} ({registros.length})</summary><ul>{registros.map((fila) => <li key={fila.fila_csv}>{fila.venta_id || "Sin ID"} · fila CSV {fila.fila_csv}: {fila.motivo}</li>)}</ul></details>)}
          </section>
        </>;
      })()}
    </main>
  );
}
