# Cómo funciona, paso a paso

## 1. Lo que proporcionó el profesor

En Ventas01Papeleo tienes el enunciado, el diccionario de datos, dos archivos con datos y un script incompleto con TODO. Los datos incluyen errores a propósito. La tarea consiste en completar el proceso y enseñar resultados fiables en una web.

El script inicial ya sabía abrir archivos, separar las líneas del CSV y convertir el JSON en objetos JavaScript. También tenía funciones para guardar resultados, pero todavía no las usaba. No calculaba ingresos ni creaba el dashboard.

## 2. El recorrido de los datos

Piensa en una hoja de tickets y un catálogo:

```text
ventas.csv + productos.json
             ↓
    scripts/procesar.mjs
             ↓
  revisar → separar errores → cruzar → sumar
             ↓
    salida/*.json y copias públicas
             ↓
    dashboard: cifras, barras y tabla
```

El CSV llega como texto: `"2"` todavía no es el número `2`. Primero comprobamos que no está vacío y después usamos Number para convertirlo. JavaScript convierte un texto vacío en cero; por eso no podemos confiar solo en la conversión.

## 3. El script por bloques

Abre scripts/procesar.mjs y sigue este orden:

1. **Índice de productos.** Map funciona como una agenda: P02 → bolígrafo, Papelería. has comprueba si existe, set guarda y get busca. Un catálogo con dos productos para el mismo ID sería ambiguo y detiene el proceso.
2. **Lectura del CSV.** split separa líneas y campos. Object.fromEntries forma un objeto con los nombres de la cabecera. Guardamos también el número de fila para poder localizar errores.
3. **Versiones por ID.** Un Map contiene un Set de versiones para cada venta_id. Set guarda valores sin repetir. Dos versiones diferentes del mismo ID son un conflicto. Revisamos todas antes de aceptar alguna para evitar elegir por orden de aparición.
4. **Duplicados.** Una firma representa todos los campos originales. Si ya vimos esa firma y no hay conflicto, apartamos la copia.
5. **Validación.** Revisamos campos vacíos, fecha real y dentro del periodo, unidades enteras positivas, precio finito no negativo y producto existente. continue significa «esta fila ya está clasificada; pasa a la siguiente».
6. **Cruce.** Buscamos el producto por producto_id, añadimos nombre y categoría y calculamos ingreso = unidades × precio. V002 da 2 × 2 = 4 EUR.
7. **Sumas.** Otro Map acumula ingresos por categoría. reduce recorre una lista acumulando un total: empezamos en cero y sumamos unidades o ingresos de cada venta válida.
8. **Guardado.** JSON.stringify convierte objetos en texto JSON. mkdir crea la carpeta si falta y writeFile escribe el resultado. Las fuentes no se sobrescriben.

La función procesar recibe datos y devuelve resultados; no escribe archivos. main abre las fuentes, llama a procesar y guarda lo que devuelve. Separarlo permite comprobar las reglas con ejemplos sin modificar las fuentes.

## 4. Los tres resultados

- resumen.json: cifras finales y categorías, periodo, moneda y fecha de generación.
- calidad.json: cuántas filas se aceptaron, cuántas se excluyeron y los motivos.
- ventas.json: cada operación válida con su nombre, categoría e ingreso; sirve para la tabla y el gráfico diario.

El enunciado exige los dos primeros. El tercero permite ver de dónde salen las cifras.

## 5. La web

React construye la interfaz con componentes. Next.js organiza la aplicación y proporciona el servidor y la compilación.

- app/page.jsx: la página principal. fetch pide los archivos JSON al servidor.
- useState: guarda en memoria los datos, un error o el texto buscado; al cambiar, React actualiza la pantalla.
- useEffect: inicia la carga al abrir la página.
- app/layout.jsx: envoltorio de todas las páginas, idioma y metadatos.
- app/globals.css: colores, tamaños, distribución y barras.
- public/datos: archivos públicos accesibles en /datos/resumen.json, etc.

El navegador no puede leer libremente la carpeta datos de tu disco. Por eso el proceso coloca copias de los resultados dentro de public. La web no necesita una base de datos para esta práctica.

## 6. El comando que crea muchas carpetas

No sabemos qué comando exacto ejecutó el profesor. Si estaba creando una aplicación Next.js, probablemente era:

```powershell
npx.cmd create-next-app@latest dashboard
```

Es una herramienta que prepara un proyecto: crea carpetas, archivos de configuración y normalmente instala dependencias. No lo ejecutes ahora dentro de este proyecto: dashboard ya está preparado.

La diferencia entre comandos:

| Comando | Qué hace |
| --- | --- |
| node scripts/procesar.mjs | Ejecuta nuestro programa de datos |
| npx.cmd create-next-app@latest dashboard | Genera una aplicación nueva |
| npm.cmd install | Instala los paquetes declarados en package.json y puede actualizar el archivo de versiones |
| npm.cmd ci | Instala exactamente las versiones del package-lock.json; reconstruye node_modules |
| npm.cmd run dev | Arranca la web local en desarrollo |
| npm.cmd run build | Compila la aplicación para producción |
| npm.cmd run start | Sirve la aplicación ya compilada |

package.json es la lista de ingredientes y comandos del proyecto. package-lock.json fija las versiones concretas. node_modules contiene el código descargado: cada paquete puede necesitar otros paquetes, por eso aparecen muchas carpetas. No debes editarlas ni subirlas a GitHub. .next contiene archivos generados por Next.js; tampoco se edita ni se sube. .gitignore indica a Git que ignore estas carpetas.

En este equipo usamos npm.cmd y npx.cmd porque PowerShell bloquea los scripts npm.ps1. No hace falta cambiar la seguridad de Windows.

## 7. Localhost, GitHub y Vercel

localhost es tu propio ordenador. npm run dev pone en marcha un servidor; abrir su URL no publica la página en Internet. Hay que dejar el terminal funcionando. Ctrl+C lo detiene.

Git guarda versiones del código. GitHub aloja el repositorio. Vercel construye y publica la aplicación y da una URL para que otras personas la vean. Instalar dependencias no conecta automáticamente esas cuentas.

Si llegan nuevas ventas, el proceso no se ejecuta solo: hay que regenerar los JSON. En Internet hay que subir el cambio y publicar otra versión. El botón Actualizar datos únicamente vuelve a leer los resultados disponibles.

## 8. Qué deberías poder explicar

Por qué V002 produce 4 EUR; por qué una copia no se suma dos veces; por qué V061 queda fuera; cómo se relacionan los archivos por producto_id; por qué 70 = 60 + 5 + 5; y qué pasos actualizan la web.

No hace falta memorizar toda la sintaxis de golpe. Podemos repasar cada bloque con una venta concreta.
