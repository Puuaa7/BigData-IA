# Resumen completo Python — para estudiar

> Resumen de los 4 temas de teoría + la parte "solo Python" de estadística (ML).
> Esto es para estudiar. La chuleta de 1 A4 para el examen es `00_chuleta_A4.html` / `.pdf`.

---

## 1. Tipos y operadores

| Tipo | Ejemplo | Convertir |
|---|---|---|
| `int` | `25` | `int("25")` → 25 |
| `float` | `1.75` | `float("1.5")` → 1.5 |
| `str` | `"Hola"` | `str(25)` → `"25"` |
| `bool` | `True` / `False` | `bool(0)` → False |
| `NoneType` | `None` (ausencia de valor, NO es 0 ni "") | |

`type(x)` dice el tipo. Tipado **dinámico** (no declaras tipo) y **fuerte** (`"5" + 5` → `TypeError`).

| Op | Qué hace | Ejemplo → resultado |
|---|---|---|
| `/` | división decimal (siempre float) | `7 / 2` → `3.5` · `4 / 2` → `2.0` |
| `//` | división entera | `7 // 2` → `3` |
| `%` | resto | `7 % 2` → `1` (par si `n % 2 == 0`) |
| `**` | potencia | `2 ** 3` → `8` · `9 ** 0.5` → `3.0` (raíz) |
| `+=  -=  *=  /=` | actualizar | `x += 1` es `x = x + 1` |
| `== != > < >= <=` | comparar → bool | `=` asigna, `==` compara |
| `and or not` | lógicos | `and`: las dos · `or`: al menos una |

Con textos: `"ab" + "cd"` → `"abcd"`, `"ab" * 3` → `"ababab"`, `len("hola")` → 4, `"@" in pwd` → bool.
f-string: `f"Media: {media}"`, con decimales `f"{media:.2f}"`.

---

## 2. Datos compuestos

| | Símbolo | Ordenado | Modificable | Duplicados | Acceso |
|---|---|---|---|---|---|
| `list` | `[1, 2]` | sí | sí | sí | `l[0]` |
| `tuple` | `(1, 2)` | sí | **no** | sí | `t[0]` |
| `dict` | `{"k": v}` | sí | sí | claves no | `d["k"]` |
| `set` | `{1, 2}` | **no** | sí | **no** | solo `in` |

Ojo: `{}` vacío es un **dict**. Un set vacío es `set()`.

**Listas**
```python
l = [7, 8, 9]
l[0]        # 7 (primero)      l[-1]  # 9 (último)
l[len(l)]   # IndexError! el último índice es len(l) - 1
l[1:3]      # [8, 9]  (desde 1 hasta ANTES de 3)   l[:2] -> [7, 8]
l[1] = 10   # cambiar
l.append(5) # añadir al final
len(l) sum(l) min(l) max(l)
l.count(8)  # cuántas veces aparece 8
x in l      # True/False
sorted(l)   # DEVUELVE lista nueva ordenada (l no cambia)
l.sort()    # ordena l y devuelve None
copia = l.copy()   # copia real;  b = l  NO copia (son la misma lista)
[0] * 3     # [0, 0, 0]
```

**Diccionarios**
```python
alumno = {"nombre": "Ana", "edad": 16}
alumno["edad"]        # leer (KeyError si no existe)
alumno["edad"] = 17   # modificar (si existe) o añadir (si no existe)
"nombre" in alumno    # mira las CLAVES
len(alumno)           # nº de claves
alumno.keys()  alumno.values()  alumno.items()
```

**Conjuntos**: `s.add(x)`, `x in s`, `set(lista)` quita duplicados (pierde el orden).

---

## 3. Condicionales

```python
if nota < 5:
    print("Suspenso")
elif nota < 7:          # solo se mira si lo de arriba fue False
    print("Aprobado")
else:
    print("Notable o más")
```
- Se evalúa de arriba a abajo y **solo se ejecuta el primer bloque True**. El orden importa.
- Dos puntos `:` + indentación obligatorios.
- Ternario: `msg = "Mayor" if edad >= 18 else "Menor"`
- match-case (Python ≥ 3.10):
```python
match opcion:
    case "crear":
        ...
    case _:          # por defecto
        ...
```

---

## 4. Bucles

```python
while condicion:          # mientras sea True. ¡Actualiza la variable o es infinito!
    ...
for x in iterable:        # lista, tupla, str (letra a letra), dict (claves), set, range
    ...
```

| range | genera |
|---|---|
| `range(5)` | 0 1 2 3 4 (el final **no** se incluye) |
| `range(1, 6)` | 1 2 3 4 5 |
| `range(2, 11, 2)` | 2 4 6 8 10 |
| `range(10, 0, -1)` | 10 9 … 1 |
| `range(len(l))` | índices de la lista |

```python
for i, nombre in enumerate(nombres):            # 0 Ana, 1 Luis...
for i, nombre in enumerate(nombres, start=1):   # 1 Ana, 2 Luis...
for prod, precio in zip(productos, precios):    # para en la lista más corta
for clave, valor in d.items():
```
- `break` → sale del bucle. `continue` → salta a la siguiente vuelta. `pass` → no hace nada (relleno).
- `for ... else:` el `else` se ejecuta si el bucle **no** terminó con `break`.
- Comprensión: `[n * n for n in range(1, 6)]` → `[1, 4, 9, 16, 25]`
  con filtro: `[n for n in l if n % 2 == 0]`

---

## 5. Patrones que salen siempre

```python
# CONTADOR                       # ACUMULADOR
aprobados = 0                    total = 0
for n in notas:                  for p in precios:
    if n >= 5:                       total += p
        aprobados += 1

# MÁXIMO / MÍNIMO A MANO (empieza con el primer elemento, no con 0)
mayor = l[0]
for x in l:
    if x > mayor:
        mayor = x

# BÚSQUEDA CON BANDERA
encontrado = False
for i, x in enumerate(l):
    if x == buscado:
        encontrado = True
        break
if not encontrado:
    print("No encontrado")

# FRECUENCIAS CON DICCIONARIO
frec = {}
for x in l:
    if x in frec:
        frec[x] += 1
    else:
        frec[x] = 1

# INTERCAMBIAR DOS POSICIONES
aux = l[i]
l[i] = l[j]
l[j] = aux            # (o en una línea: l[i], l[j] = l[j], l[i])

# LISTA NUEVA TRANSFORMADA
resultado = []
for x in l:
    resultado.append(x * 2)
```

**Ordenación a mano** (siempre sobre `l = lista.copy()` para no tocar la original)
```python
# Burbuja: compara VECINOS; en cada pasada el mayor acaba al final
for i in range(len(l) - 1):
    for j in range(len(l) - 1 - i):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

# Intercambio directo: compara la posición i con todas las siguientes
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if l[j] < l[i]:
            l[i], l[j] = l[j], l[i]

# Selección: busca la POSICIÓN del mínimo y hace UN intercambio por pasada
for i in range(len(l) - 1):
    pos_min = i
    for j in range(i + 1, len(l)):
        if l[j] < l[pos_min]:
            pos_min = j
    l[i], l[pos_min] = l[pos_min], l[i]
```

---

## 6. Funciones

```python
def calcular_precio(precio, descuento=0):     # obligatorios primero, con valor por defecto después
    """Docstring: explica qué hace."""
    return precio - precio * descuento / 100

calcular_precio(100)              # posicional, descuento=0  -> 100.0
calcular_precio(100, 15)          # -> 85.0
calcular_precio(descuento=15, precio=100)   # con nombre: el orden da igual
```
- **Definir ≠ llamar**: la función no hace nada hasta que la llamas `f()`.
- **`print` muestra, `return` devuelve**. Sin `return` la función devuelve **`None`**.
  `r = f()` con f que solo hace print → `r` vale `None`.
- `return` **termina** la función al momento.
- Varios valores: `return a, b` devuelve una **tupla** → `x, y = f()`.
- Variables dentro de la función son **locales** (no existen fuera). Datos entran por parámetros, salen por return.
- `def f(*args)` → `args` es una **tupla**. `def f(**kwargs)` → `kwargs` es un **dict**.
- Anotaciones: `def media(notas: list[float]) -> float:` (solo informativas, no obligan).
- `lambda x: x * 2` → función anónima de una expresión (devuelve sola).

```python
list(map(lambda x: x * 2, l))             # aplica a cada elemento
list(filter(lambda x: x % 2 == 0, l))     # se queda con los que dan True
sorted(personas, key=lambda p: p["edad"]) # ordenar lista de dicts por un campo
sorted(l, reverse=True)                   # de mayor a menor
max(personas, key=lambda p: p["nota"])    # el dict con mayor nota
max(set(l), key=lambda v: l.count(v))     # la moda en una línea
```
Ojo: `map` y `filter` devuelven un objeto "perezoso" → envuélvelos en `list(...)` para verlo.

**Recursividad**: la función se llama a sí misma y **necesita caso base**.
```python
def factorial(n):
    if n == 0:            # caso base
        return 1
    return n * factorial(n - 1)
```

---

## 7. Estadística en Python puro (lo de ML sin pandas)

Datos ejemplo `puntos = [50, 60, 60, 70, 70, 80, 80, 80, 90, 100]` → media 74, mediana 75, moda 80, varianza 204, desv. típica ≈ 14.28.

| Medida | Fórmula | Python puro |
|---|---|---|
| Media | suma / n | `sum(l) / len(l)` |
| Mediana | valor central de la lista **ordenada**; si n par, media de los dos centrales | `o = sorted(l)`; par: `(o[n//2 - 1] + o[n//2]) / 2`; impar: `o[n//2]` |
| Moda | valor más repetido | dict de frecuencias, o `max(set(l), key=l.count)` |
| Desviación | x − media | `[x - media for x in l]` |
| Varianza poblacional | Σ(x − media)² / **n** | `sum((x - m) ** 2 for x in l) / len(l)` |
| Varianza muestral | Σ(x − media)² / **(n − 1)** | (pandas `.var()` usa esta por defecto, `ddof=1`) |
| Desv. estándar | √varianza | `varianza ** 0.5` |
| Min‑max | (x − min) / (max − min) → entre 0 y 1 | |
| z‑score | (x − media) / desv_est | z > 0 encima de la media, z < 0 debajo |

---

## 8. Errores típicos (para preguntas de "¿qué falla?")

| Error | Ejemplo | Resultado |
|---|---|---|
| Falta `:` | `if x > 3` | `SyntaxError` |
| `=` en vez de `==` | `if x = 3:` | `SyntaxError` |
| Mala indentación | cuerpo sin sangrar | `IndentationError` |
| Índice fuera de rango | `l[len(l)]` | `IndexError` |
| Clave inexistente | `d["noexiste"]` | `KeyError` |
| Mezclar tipos | `"Edad: " + 18` | `TypeError` → usa `str(18)` o comas en print |
| Usar el resultado de una función sin return | `total = f() + 1` | `TypeError` (None + int) |
| Parámetro por defecto antes de uno obligatorio | `def f(a=1, b):` | `SyntaxError` |
| while sin actualizar | `while i < 5: print(i)` | bucle infinito |
| Creer que range incluye el final | `range(1, 5)` | llega a 4 |
| Dividir entre 0 | `x / 0` | `ZeroDivisionError` |
| `l.sort()` guardado | `r = l.sort()` | `r` es `None` |
| Recursión sin caso base | | `RecursionError` |
