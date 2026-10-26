# Ejercicios para el examen escrito

## Cómo usar esto (importante)

Que entiendas el código cuando lo lees no significa que te salga escribirlo, y en el examen te van a pedir **escribir**. Lo que funciona es **sacarlo tú de la cabeza**:

1. **Papel y boli**, como en el examen. Nada de ordenador mientras lo haces.
2. Puedes mirar **solo la chuleta A4** (lo mismo que tendrás en el examen).
3. Si te atascas más de 3–4 min: mira la chuleta, **cierra la chuleta**, y vuelve a escribirlo.
4. Al acabar, compara con `03_soluciones.py` (o pásalo al ordenador y ejecútalo).
5. Los que fallen: **márcalos y repítelos al día siguiente** sin mirar.

⭐ = imprescindible. Si vas justo de tiempo, haz solo los ⭐.

**Plan sugerido**
- **Lunes**: Bloque A (predecir salida) + Bloque B (errores). Son rápidos y te entrenan a "ejecutar en la cabeza".
- **Martes mañana**: Bloque C (escribir funciones).
- **Martes tarde**: Bloque D (estadística) + Bloque E (simulacro). Repite los que fallaste el lunes.
- **Miércoles antes del examen**: rehaz solo los ⭐ que fallaste.

---

## Bloque A — ¿Qué imprime? (escribe la salida exacta)

**A1 ⭐**
```python
print(7 / 2, 7 // 2, 7 % 2, 2 ** 3, 10 / 5)
```

**A2 ⭐**
```python
x = "5"
y = 5
print(x * 2, y * 2)
```

**A3 ⭐**
```python
print(list(range(10, 0, -3)))
print(list(range(2, 9, 2)))
```

**A4 ⭐**
```python
nums = [4, 7, 0, 9, 2]
for n in nums:
    if n == 0:
        continue
    if n > 8:
        break
    print(n)
```

**A5 ⭐**
```python
def doble(x):
    print(x * 2)

r = doble(3)
print(r)
```

**A6 ⭐**
```python
nota = 8
if nota >= 5:
    print("Aprobado")
elif nota >= 7:
    print("Notable")
else:
    print("Suspenso")
```

**A7 ⭐**
```python
def precio(p, d=10):
    return p - p * d / 100

print(precio(50), precio(50, 50), precio(d=0, p=20))
```

**A8**
```python
def extremos(lista):
    return min(lista), max(lista)

r = extremos([3, 9, 1])
print(r, type(r))
a, b = extremos([5, 2])
print(a + b)
```

**A9 ⭐**
```python
d = {"a": 1}
d["b"] = 2
d["a"] = 5
print(len(d), d)
```

**A10 ⭐**
```python
i = 0
total = 0
while i < 5:
    i += 2
    total += i
print(i, total)
```

**A11**
```python
def f(n):
    if n <= 1:
        return 1
    return n * f(n - 1)

print(f(4))
```

**A12**
```python
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 10, filter(lambda x: x % 2 == 1, nums))))
```

**A13**
```python
a = [1, 2]
b = a
b.append(3)
c = a.copy()
c.append(4)
print(a, b, c)
```

**A14 ⭐**
```python
l = [3, 1, 2]
r = l.sort()
print(r, l)
print(sorted([3, 1, 2], reverse=True))
```

**A15**
```python
x = 10
def cambiar():
    x = 99
    return x

print(cambiar(), x)
```

**A16**
```python
for a, b in zip([1, 2, 3], ["x", "y"]):
    print(a, b)
for i, letra in enumerate("hey", start=1):
    print(i, letra)
```

**A17**
```python
for n in [1, 3, 5]:
    if n % 2 == 0:
        print("Hay par")
        break
else:
    print("Todos impares")
```

**A18 ⭐**
```python
contador = 0
for c in "banana":
    if c == "a":
        contador += 1
print(contador)
n = 0
print("pos" if n > 0 else "neg" if n < 0 else "cero")
```

**A19**
```python
def sumar(*nums):
    print(type(nums))
    return sum(nums)

def ficha(**datos):
    for k, v in datos.items():
        print(k, "=", v)

print(sumar(1, 2, 3))
ficha(nombre="Pau", edad=24)
```

**A20**
```python
tabla = [[1, 2], [3, 4], [5, 6]]
total = 0
for fila in tabla:
    for n in fila:
        if n % 2 == 0:
            total += n
print(total)
print([n * n for n in range(1, 5) if n != 2])
```

---

## Bloque B — Encuentra y corrige el error

Di **qué error da** (o qué hace mal) y **corrígelo**.

**B1 ⭐**
```python
edad = 18
if edad = 18
    print("Justo 18")
```

**B2 ⭐**
```python
i = 1
while i <= 5:
    print(i)
```

**B3 ⭐**
```python
notas = [5, 7, 9]
ultima = notas[len(notas)]
```

**B4**
```python
def saludo(saludo="Hola", nombre):
    return saludo + " " + nombre
```

**B5 ⭐**
```python
edad = 18
print("Tienes " + edad + " años")
```

**B6 ⭐**
```python
def calcular_total(precios):
    total = 0
    for p in precios:
        total += p
    print(total)

total_con_iva = calcular_total([10, 20]) * 1.21
```

**B7** (no da error, pero el resultado está mal: ¿por qué?)
```python
def mediana(lista):
    n = len(lista)
    return lista[n // 2]

print(mediana([9, 1, 5]))
```

**B8** (no da error, pero el resultado está mal: ¿por qué?)
```python
notas = [-1, -5, -3]
mayor = 0
for n in notas:
    if n > mayor:
        mayor = n
print(mayor)
```

**B9**
```python
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False
    print("Comprobado")   # ¿se imprime alguna vez?
```

**B10**
```python
alumno = {"nombre": "Ana", "nota": 7}
print(alumno["edad"])
print(alumno[0])
```

---

## Bloque C — Escribe la función (lo más parecido al examen)

Escribe cada una como **función con `return`**, y debajo una llamada de ejemplo con `print`.

**C1 ⭐** `es_par(n)` → devuelve `True` si n es par, `False` si no.

**C2 ⭐** `clasificar_nota(nota)` → devuelve `"Suspenso"` (<5), `"Aprobado"` (<7), `"Notable"` (<9) o `"Sobresaliente"`. Si la nota es menor que 0 o mayor que 10, devuelve `"Nota no válida"`.

**C3 ⭐** `contar_vocales(texto)` → devuelve cuántas vocales tiene (minúsculas, sin tildes). Pista: `if letra in "aeiou"`.

**C4 ⭐** `tabla_multiplicar(n)` → **muestra** (print) la tabla del n del 1 al 10 con formato `7 x 3 = 21`. No devuelve nada.

**C5 ⭐** `contar_aprobados(notas)` → recibe una lista de notas y devuelve **dos valores**: cuántos aprobados y cuántos suspensos.

**C6** `invertir(lista)` → devuelve una lista nueva al revés **sin** usar `reverse`, `[::-1]` ni `sorted`. Pista: `range(len(lista) - 1, -1, -1)`.

**C7** `quitar_duplicados(lista)` → devuelve una lista nueva sin repetidos **manteniendo el orden** original. Ej: `[3, 1, 3, 2, 1]` → `[3, 1, 2]`.

**C8 ⭐** `buscar(lista, valor)` → devuelve la **posición** del valor o `-1` si no está. Con `for` + `enumerate`, sin usar `.index()`.

**C9 ⭐** `validar_password(pwd)` → devuelve `True` si tiene al menos 8 caracteres, contiene `@`, y no es `"12345678"`.

**C10** `sumar_todo(*nums)` → suma cualquier cantidad de números con un bucle (sin `sum`). `sumar_todo(1, 2, 3, 4)` → 10.

**C11** `precio_final(precio, descuento=0, iva=21)` → aplica primero el descuento (%) y después el IVA (%). Llámala de 3 maneras: solo precio, precio + descuento, y con argumentos por nombre.

**C12 ⭐** Tienes:
```python
alumnos = [
    {"nombre": "Ana", "nota": 7.5, "faltas": 2},
    {"nombre": "Luis", "nota": 4.0, "faltas": 12},
    {"nombre": "Marta", "nota": 9.0, "faltas": 0},
    {"nombre": "Pedro", "nota": 5.5, "faltas": 11},
]
```
a) `media_clase(alumnos)` → media de las notas.
b) `nombres_aprobados(alumnos)` → lista con los nombres de los que tienen nota ≥ 5.
c) `mejor_alumno(alumnos)` → devuelve el **diccionario** del alumno con mayor nota (hazlo con bucle; luego hazlo también con `max(..., key=lambda ...)`).
d) `con_aviso(alumnos)` → lista de nombres con más de 10 faltas.
e) Ordena la lista por nota de mayor a menor con `sorted` + `lambda`.

**C13** `contar_palabras(lista)` → devuelve un diccionario con cuántas veces aparece cada palabra. `["sol", "mar", "sol"]` → `{"sol": 2, "mar": 1}`.

**C14** Con `map` y `filter` (y `lambda`): a partir de `precios = [12, 55, 8, 100, 30]`, obtén una lista con los precios mayores de 20 con un 10 % de descuento aplicado.

**C15** Recursividad: `suma_hasta(n)` → devuelve 1 + 2 + … + n **sin bucles**. ¿Cuál es el caso base?

**C16** `menu(opcion)` con `match-case`: `"1"` → `"Alta"`, `"2"` → `"Baja"`, `"3"` → `"Listar"`, cualquier otra → `"Opción no válida"`.

---

## Bloque D — Estadística sin pandas (lo de ML)

Usa `puntos = [50, 60, 60, 70, 70, 80, 80, 80, 90, 100]`. Resultados esperados: media 74, mediana 75, moda 80, varianza 204, desviación ≈ 14.28.

**D1 ⭐** `media(lista)` con bucle (sin `sum`).

**D2 ⭐** `ordenar_burbuja(lista)` → devuelve una lista **nueva** ordenada (no modifiques la original: usa `.copy()`).

**D3 ⭐** `mediana(lista)` → usa tu `ordenar_burbuja`. Cuidado con n par / impar. Pruébala también con `[3, 1, 2]` → 2.

**D4 ⭐** `moda(lista)` → construye un diccionario de frecuencias y busca la clave con más apariciones.

**D5** `varianza(lista)` poblacional (entre n) y `desviacion_estandar(lista)` (raíz con `** 0.5`). Reutiliza `media`.

**D6** `normalizar(lista)` → min‑max: cada valor pasa a `(x - min) / (max - min)`. Busca el min y el max **con un bucle**, sin `min()`/`max()`.

**D7** `z_scores(lista)` → `(x - media) / desviacion` para cada valor. ¿Quién tiene z positivo?

**D8 ⭐** `resumen(lista)` → devuelve un **diccionario** `{"media": ..., "mediana": ..., "moda": ..., "desviacion": ...}` llamando a las funciones anteriores.

**D9** Haz D1, D6 y D7 otra vez pero en una línea cada una, usando `sum`, `min`, `max`, `map`/`lambda` o comprensión de listas.

**D10** Teoría rápida (responde en una frase):
- ¿Qué diferencia hay entre varianza poblacional y muestral? ¿Entre qué se divide cada una?
- ¿Por qué la mediana necesita los datos ordenados?
- ¿Qué diferencia hay entre `sorted(l)` y `l.sort()`?
- ¿En qué se diferencian burbuja, selección e intercambio directo?

---

## Bloque E — Simulacro (45 min, sin mirar nada salvo la chuleta)

**E1. Tienda (40 %)**
```python
productos = [
    {"nombre": "ratón", "precio": 15.0, "stock": 12},
    {"nombre": "teclado", "precio": 25.0, "stock": 0},
    {"nombre": "monitor", "precio": 120.0, "stock": 3},
    {"nombre": "cable", "precio": 4.5, "stock": 25},
]
```
1. `valor_inventario(productos)` → suma de precio × stock.
2. `agotados(productos)` → lista de nombres con stock 0.
3. `reponer(productos, nombre, unidades)` → suma unidades al stock del producto con ese nombre. Devuelve `True` si lo encontró, `False` si no (usa `break`).
4. `mas_caro(productos)` → nombre del producto más caro (bucle, sin `max`).
5. Programa principal: llama a todo y muestra resultados. Repón 5 teclados y vuelve a mostrar los agotados.

**E2. Notas de la clase (40 %)**
```python
nombres = ["Ana", "Bruno", "Carla", "Diego", "Elena"]
notas = [6.5, 4.0, 9.5, 7.0, 3.5]
```
1. Con `zip`, crea un diccionario `{nombre: nota}`.
2. `estadisticas(notas)` → devuelve media, nota máxima y nota mínima (3 valores, sin `sum`/`max`/`min`).
3. Con `for` + `items()`, muestra `Ana: 6.5 (Aprobado)` usando tu `clasificar_nota` (C2) o un ternario.
4. ¿Cuántos están por encima de la media? Usa un contador.
5. Ordena los nombres de mayor a menor nota (`sorted` + `lambda` sobre `items()`).

**E3. Teoría corta (20 %)**
1. Diferencia entre `print` y `return`. ¿Qué devuelve una función sin `return`?
2. Diferencia entre lista y tupla. Pon un ejemplo de cuándo usar cada una.
3. ¿Qué hacen `break`, `continue` y `pass`?
4. ¿Qué es un parámetro y qué es un argumento?
5. ¿Qué necesita siempre una función recursiva?
6. ¿Qué genera `range(3, 12, 3)`?
