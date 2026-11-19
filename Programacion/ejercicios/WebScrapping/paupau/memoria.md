# Memoria · Proyecto de obtención de datos y EDA

**Tema:** comparativa de tres marcas españolas de streetwear: Cold Culture, Scuffers y Milfshakes
**Integrantes:** _[Nombre 1]_ · _[Nombre 2]_
**Entrega:** 30/11/2026 · **Exposición:** 02/12/2026

> Documento vivo: se actualiza a medida que avanza el proyecto.

---

## 1. Elección del tema

Elegimos tres marcas españolas de ropa streetwear que compiten por el mismo público joven y venden casi solo online. Queremos comparar objetivamente sus precios, la composición de sus catálogos y la calidad de sus materiales.

Las tres tiendas usan **Shopify**, así que los datos tienen la misma estructura y se pueden comparar directamente.

### Preguntas de investigación
1. **Precio:** ¿qué marca es más cara en cada categoría (sudaderas, camisetas, pantalones, accesorios)?
2. **Catálogo:** ¿cuántos productos tiene cada marca por categoría y en qué se especializa cada una?
3. **Materiales:** ¿un precio más alto se corresponde con mejores materiales (más % de algodón, más gramaje)?
4. **Descuentos:** ¿qué marca hace más rebajas, cuánto descuenta y en qué categorías?
5. **Agotados:** ¿los productos más caros se agotan antes o después? ¿Qué tallas se agotan más?
6. **Colores:** ¿qué paleta de colores domina en cada marca?
7. **Outfit completo:** ¿cuánto cuesta vestirse de arriba abajo con cada marca?
8. **Lanzamientos:** ¿con qué frecuencia lanza productos cada marca (ritmo de drops)?

### Alcance
- Productos publicados en la tienda online oficial de cada marca en la fecha de obtención.
- No se incluyen tiendas físicas, revendedores ni datos de ventas reales (no son públicos).

---

## 2. Fuentes de datos

| Fuente | Tipo | URL | Qué aporta |
|---|---|---|---|
| Catálogo Shopify | **API JSON** | `https://{tienda}/products.json` | Título, categoría (`product_type`), tags, variantes (tallas/colores), precio, precio tachado, disponibilidad, fechas |
| Ficha de producto | **Web scraping HTML** | `https://{tienda}/products/{handle}` | Composición (materiales) y gramaje, que no vienen en la API |

Tiendas:
- Scuffers → `https://scuffers.com`
- Milfshakes → `https://milfshakes.es`
- Cold Culture → `https://coldcultureworldwide.com`

### robots.txt (consultado el 19/11/2026)
- **Scuffers y Milfshakes:** permiten `/products/` y `/collections/`. Prohíben `cart`, `account`, `checkout`, `orders` y URLs de colección con `sort_by` o filtros combinados. No accedemos a ninguna ruta prohibida.
- **Cold Culture:** la tienda está protegida con **contraseña** (vende por *drops*). Accedemos con la contraseña de acceso a la tienda. _[Indicar de dónde se obtuvo la contraseña]_. La contraseña no se publica en el repositorio (se guarda en un archivo `.env` excluido con `.gitignore`).

---

## 3. Procedimiento de obtención

### Scuffers (19/11/2026)
1. Exploración manual en el navegador de `products.json` y de las fichas de producto.
2. Petición a `products.json?limit=250&page=N`; 250 es el máximo de productos por página en Shopify. La página 1 devolvió 250 productos, así que el catálogo tiene más páginas.
3. Paginación hasta recibir una página vacía, con 3 s de pausa entre peticiones: 7 páginas con datos (la 8 vino vacía) y **1.698 productos** en total, sin ningún 429 (≈24 s).
4. Guardado del JSON original en `data/raw/scuffers_products_20261119.json` (≈12 MB), con la fuente y la fecha de obtención.
   - 1.698 productos únicos (sin duplicados por `id`), 8.895 variantes (tallas), publicados entre 2024 y 2026; 1.350 con al menos una talla disponible.
5. Conversión a dos tablas (sin limpiar) en `data/raw/`:
   - `scuffers_productos_20261119.csv` → 1 fila = 1 producto (id, título, handle, product_type, tags, fecha de publicación, nº de tallas, nº de imágenes).
   - `scuffers_variantes_20261119.csv` → 1 fila = 1 talla (id de producto, talla, precio, precio tachado, disponible).
6. Web scraping de las fichas `scuffers.com/products/{handle}` con `curl_cffi` + BeautifulSoup: se extrae el texto de `div.metafield-rich_text_field`. Probado con 3 productos (status 200, descripción correcta).
7. Scraping de una **muestra aleatoria de 400 productos** (`random.seed(42)`), con 3 s de pausa, guardando cada fila al momento en `data/raw/scuffers_descripciones_20261119.csv` (columnas: `handle`, `status`, `descripcion`). Celda reanudable: si se corta, salta los productos ya hechos. Resultado: **400 filas** (400 productos distintos), todas con status 200 y sin ningún 429. Solo 2 sin descripción. 389 descripciones (97 %) incluyen un porcentaje de composición ("100% cotton"…). **Ninguna indica el gramaje (GSM)**, así que esa variable no se podrá analizar en Scuffers.

### Milfshakes
_[Pendiente]_

### Cold Culture
_[Pendiente]_

---

## 4. Dificultades encontradas

| Fecha | Problema | Causa | Solución |
|---|---|---|---|
| 19/11 | El notebook no ejecutaba celdas (pedía `ipykernel`) | VS Code usaba el Python de MSYS64, que no tenía las librerías | Cambiar el kernel a Python 3.14 |
| 19/11 | **Error 429** *Too Many Requests* al pedir `products.json` con `requests`, aunque en el navegador sí cargaba | Shopify limita el número de peticiones y detecta clientes que no son navegadores | 1) Cambiar el `User-Agent` por el de Chrome → no bastó. 2) Esperar sin hacer peticiones. 3) Usar `curl_cffi` con `impersonate="chrome"`, que imita la conexión de un navegador real → **funcionó** (status 200, 250 productos en la página 1) |
| 19/11 | La tienda de Cold Culture redirige a `/password` | Venta por *drops*: la tienda solo se abre en los lanzamientos | Acceso con contraseña. Limitación: puede que solo se vea el drop activo, no el catálogo completo |

---

## 5. Decisiones y cambios de criterio

- **Composición vía scraping:** en el JSON de Scuffers el campo `body_html` casi solo trae medidas, sin materiales. Por eso la composición se obtiene del HTML de cada ficha, y esa parte es nuestro web scraping. Inspeccionando la ficha (p. ej. *Warm Grey Melange Hoodie*) vimos que la descripción con la composición ("100% cotton") está en el elemento `div.metafield-rich_text_field`, en inglés.
- **Variable `grams` descartada:** vale 0 en todos los productos vistos y no aporta información.
- **Categorías a normalizar:** `product_type` está desordenado ("Man Sandals", "Man Wallet 3"…). Habrá que agruparlo en categorías comunes a las tres marcas.
- **`product_type` con estructura:** en Scuffers sigue el patrón *Género + Prenda + Subtipo* ("Man Hoodie Zipped", "Woman Top Basic") → se podrá separar en columnas `genero`, `prenda`, `subtipo`.
- **Color desde el título:** en Scuffers las variantes son solo tallas (opción `Size`), así que el color se extraerá del título del producto ("Rattler **Ecru** Wallet").
- **Dos tablas (productos y variantes):** un producto tiene varias tallas con su disponibilidad; separarlas evita repetir los datos del producto en cada talla.
- **Tags útiles:** incluyen el drop ("drop 8 fw26") y la temporada, que servirán para la pregunta 8.
- **Pausas de 3 s entre peticiones** después del error 429.
- **Muestra aleatoria para el scraping (cambio de criterio):** scrapear las 1.698 fichas con 3 s de pausa llevaría ~1,5 h y cargaría mucho el servidor. Valoramos limitarnos a la ropa (~1 h), reducir la pausa (más riesgo de 429) o hacerlo de noche, y elegimos una **muestra aleatoria simple de 400 productos** (~20 min) con semilla fija (`random.seed(42)`) para que sea reproducible. **Efecto:** las preguntas sobre materiales (3) se responden con esa muestra, no con el catálogo completo. El resto de variables (precio, categoría, disponibilidad, fechas) sí cubren los 1.698 productos de la API.

---

## 6. Herramientas

- Python 3.14 + Jupyter (VS Code)
- `requests`, `curl_cffi` (peticiones HTTP)
- `beautifulsoup4` (parsear HTML)
- `pandas`, `numpy` (tratamiento de datos)
- `matplotlib`, `seaborn` (gráficos)
- Git + GitHub
- _[Si se menciona: asistente de IA usado como apoyo para orientación y depuración]_

---

## 7. Distribución del trabajo

| Integrante | Tareas |
|---|---|
| _[Nombre 1]_ | Obtención de datos de Scuffers… |
| _[Nombre 2]_ | … |

---

## 8. Preparación de datos
_[Pendiente: punto 3 del enunciado]_

## 9. EDA
_[Pendiente: punto 4]_

## 10. Relaciones entre variables y conclusiones
_[Pendiente: punto 5]_

## 11. Limitaciones
- Los datos son una foto del catálogo en la fecha de obtención; el stock y los precios cambian a diario.
- "Agotado" se usa como aproximación de la popularidad, pero también puede deberse a poca producción.
- Cold Culture podría mostrar solo el drop activo, lo que sesga la comparación del número de productos.
