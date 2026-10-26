"""
Soluciones de 02_ejercicios.md

Hazlos primero en papel y luego compara.
Si ejecutas este archivo, cada bloque imprime su resultado y los assert
comprueban que las funciones dan lo esperado (si algo falla, salta un error).
"""


# =====================================================================
# BLOQUE A — ¿Qué imprime?  (la salida está en los comentarios)
# =====================================================================
print("===== BLOQUE A =====")

print("\nA1")
print(7 / 2, 7 // 2, 7 % 2, 2 ** 3, 10 / 5)
# 3.5 3 1 8 2.0        <- ojo: / SIEMPRE da float, aunque sea exacta

print("\nA2")
x = "5"
y = 5
print(x * 2, y * 2)
# 55 10                <- str * 2 repite el texto

print("\nA3")
print(list(range(10, 0, -3)))
print(list(range(2, 9, 2)))
# [10, 7, 4, 1]
# [2, 4, 6, 8]         <- el 9 (final) nunca entra

print("\nA4")
nums = [4, 7, 0, 9, 2]
for n in nums:
    if n == 0:
        continue
    if n > 8:
        break
    print(n)
# 4
# 7                    <- el 0 se salta, el 9 rompe el bucle, el 2 nunca llega

print("\nA5")
def doble(x):
    print(x * 2)

r = doble(3)
print(r)
# 6
# None                 <- sin return la función devuelve None

print("\nA6")
nota = 8
if nota >= 5:
    print("Aprobado")
elif nota >= 7:
    print("Notable")
else:
    print("Suspenso")
# Aprobado             <- la 1ª condición ya es True, el elif NO se mira

print("\nA7")
def precio(p, d=10):
    return p - p * d / 100

print(precio(50), precio(50, 50), precio(d=0, p=20))
# 45.0 25.0 20.0

print("\nA8")
def extremos(lista):
    return min(lista), max(lista)

r = extremos([3, 9, 1])
print(r, type(r))
a, b = extremos([5, 2])
print(a + b)
# (1, 9) <class 'tuple'>
# 7

print("\nA9")
d = {"a": 1}
d["b"] = 2
d["a"] = 5
print(len(d), d)
# 2 {'a': 5, 'b': 2}   <- "a" ya existía: se modifica, no se duplica

print("\nA10")
i = 0
total = 0
while i < 5:
    i += 2
    total += i
print(i, total)
# 6 12                 <- vueltas: i=2 t=2 | i=4 t=6 | i=6 t=12 | 6<5 False, sale

print("\nA11")
def f(n):
    if n <= 1:
        return 1
    return n * f(n - 1)

print(f(4))
# 24                   <- 4 * 3 * 2 * 1

print("\nA12")
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 10, filter(lambda x: x % 2 == 1, nums))))
# [10, 30, 50]         <- primero filtra impares (1,3,5), luego multiplica

print("\nA13")
a = [1, 2]
b = a
b.append(3)
c = a.copy()
c.append(4)
print(a, b, c)
# [1, 2, 3] [1, 2, 3] [1, 2, 3, 4]   <- b ES la misma lista que a; c es una copia

print("\nA14")
l = [3, 1, 2]
r = l.sort()
print(r, l)
print(sorted([3, 1, 2], reverse=True))
# None [1, 2, 3]
# [3, 2, 1]

print("\nA15")
x = 10
def cambiar():
    x = 99
    return x

print(cambiar(), x)
# 99 10                <- la x de dentro es local, no toca la de fuera

print("\nA16")
for a, b in zip([1, 2, 3], ["x", "y"]):
    print(a, b)
for i, letra in enumerate("hey", start=1):
    print(i, letra)
# 1 x
# 2 y                  <- zip para en la más corta
# 1 h
# 2 e
# 3 y

print("\nA17")
for n in [1, 3, 5]:
    if n % 2 == 0:
        print("Hay par")
        break
else:
    print("Todos impares")
# Todos impares        <- no hubo break, así que entra en el else

print("\nA18")
contador = 0
for c in "banana":
    if c == "a":
        contador += 1
print(contador)
n = 0
print("pos" if n > 0 else "neg" if n < 0 else "cero")
# 3
# cero

print("\nA19")
def sumar(*nums):
    print(type(nums))
    return sum(nums)

def ficha(**datos):
    for k, v in datos.items():
        print(k, "=", v)

print(sumar(1, 2, 3))
ficha(nombre="Pau", edad=24)
# <class 'tuple'>
# 6
# nombre = Pau
# edad = 24

print("\nA20")
tabla = [[1, 2], [3, 4], [5, 6]]
total = 0
for fila in tabla:
    for n in fila:
        if n % 2 == 0:
            total += n
print(total)
print([n * n for n in range(1, 5) if n != 2])
# 12                   <- 2 + 4 + 6
# [1, 9, 16]


# =====================================================================
# BLOQUE B — Errores (respuestas en comentarios, versión corregida debajo)
# =====================================================================
print("\n===== BLOQUE B =====")

# B1: SyntaxError. Dos fallos: "=" en vez de "==" y falta ":".
edad = 18
if edad == 18:
    print("Justo 18")

# B2: bucle infinito, i nunca cambia. Falta "i += 1" dentro del while.
i = 1
while i <= 5:
    print(i)
    i += 1

# B3: IndexError. El último índice es len - 1. Correcto: notas[-1] o notas[len(notas) - 1]
notas = [5, 7, 9]
ultima = notas[len(notas) - 1]
print("B3:", ultima)

# B4: SyntaxError. Un parámetro con valor por defecto no puede ir antes de uno obligatorio.
def saludo(nombre, saludo="Hola"):
    return saludo + " " + nombre
print("B4:", saludo("Pau"))

# B5: TypeError, no se puede sumar str + int. Soluciones:
edad = 18
print("Tienes " + str(edad) + " años")
print("Tienes", edad, "años")
print(f"Tienes {edad} años")

# B6: TypeError (None * float). La función hace print pero no return -> devuelve None.
def calcular_total(precios):
    total = 0
    for p in precios:
        total += p
    return total
total_con_iva = calcular_total([10, 20]) * 1.21
print("B6:", total_con_iva)

# B7: no ordena la lista antes de coger el centro (y no trata el caso par).
#     mediana([9, 1, 5]) daría 1, pero la mediana real es 5.
def mediana_b7(lista):
    o = sorted(lista)
    n = len(o)
    if n % 2 == 0:
        return (o[n // 2 - 1] + o[n // 2]) / 2
    return o[n // 2]
print("B7:", mediana_b7([9, 1, 5]))

# B8: empieza con mayor = 0. Si todos son negativos, ninguno supera 0 y devuelve 0.
#     Hay que empezar con el primer elemento.
notas = [-1, -5, -3]
mayor = notas[0]
for n in notas:
    if n > mayor:
        mayor = n
print("B8:", mayor)   # -1

# B9: no da error, pero el print NUNCA se ejecuta: return termina la función antes.
#     Además se puede simplificar a:  return n % 2 == 0

# B10: KeyError("edad") porque esa clave no existe. alumno[0] también da KeyError:
#      los diccionarios NO se acceden por posición, solo por clave.


# =====================================================================
# BLOQUE C — Funciones
# =====================================================================
print("\n===== BLOQUE C =====")

# C1
def es_par(n):
    return n % 2 == 0

print("C1:", es_par(4), es_par(7))
assert es_par(4) and not es_par(7)


# C2
def clasificar_nota(nota):
    if nota < 0 or nota > 10:
        return "Nota no válida"
    elif nota < 5:
        return "Suspenso"
    elif nota < 7:
        return "Aprobado"
    elif nota < 9:
        return "Notable"
    else:
        return "Sobresaliente"

print("C2:", clasificar_nota(4), clasificar_nota(6), clasificar_nota(8), clasificar_nota(9.5), clasificar_nota(11))
assert clasificar_nota(7) == "Notable"
assert clasificar_nota(-1) == "Nota no válida"


# C3
def contar_vocales(texto):
    contador = 0
    for letra in texto:
        if letra in "aeiou":
            contador += 1
    return contador

print("C3:", contar_vocales("programacion"))
assert contar_vocales("programacion") == 5


# C4
def tabla_multiplicar(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

print("C4:")
tabla_multiplicar(7)


# C5
def contar_aprobados(notas):
    aprobados = 0
    suspensos = 0
    for nota in notas:
        if nota >= 5:
            aprobados += 1
        else:
            suspensos += 1
    return aprobados, suspensos

ap, su = contar_aprobados([6, 3, 8, 5, 2])
print("C5:", ap, su)
assert (ap, su) == (3, 2)


# C6
def invertir(lista):
    resultado = []
    for i in range(len(lista) - 1, -1, -1):
        resultado.append(lista[i])
    return resultado

print("C6:", invertir([1, 2, 3, 4]))
assert invertir([1, 2, 3]) == [3, 2, 1]


# C7
def quitar_duplicados(lista):
    resultado = []
    for x in lista:
        if x not in resultado:
            resultado.append(x)
    return resultado

print("C7:", quitar_duplicados([3, 1, 3, 2, 1]))
assert quitar_duplicados([3, 1, 3, 2, 1]) == [3, 1, 2]


# C8
def buscar(lista, valor):
    for posicion, elemento in enumerate(lista):
        if elemento == valor:
            return posicion      # return ya corta el bucle, no hace falta break
    return -1                    # solo llega aquí si no lo encontró

print("C8:", buscar(["Ana", "Luis", "Pau"], "Pau"), buscar(["Ana"], "Zoe"))
assert buscar([5, 6, 7], 7) == 2
assert buscar([5, 6, 7], 9) == -1


# C9
def validar_password(pwd):
    return len(pwd) >= 8 and "@" in pwd and pwd != "12345678"

print("C9:", validar_password("hola@1234"), validar_password("hola1234"))
assert validar_password("hola@1234")
assert not validar_password("ab@")


# C10
def sumar_todo(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print("C10:", sumar_todo(1, 2, 3, 4))
assert sumar_todo(1, 2, 3, 4) == 10


# C11
def precio_final(precio, descuento=0, iva=21):
    con_descuento = precio - precio * descuento / 100
    return con_descuento + con_descuento * iva / 100

print("C11:", precio_final(100), precio_final(100, 10), precio_final(iva=10, precio=50))
assert precio_final(100) == 121.0
assert precio_final(100, 10) == 108.9


# C12
alumnos = [
    {"nombre": "Ana", "nota": 7.5, "faltas": 2},
    {"nombre": "Luis", "nota": 4.0, "faltas": 12},
    {"nombre": "Marta", "nota": 9.0, "faltas": 0},
    {"nombre": "Pedro", "nota": 5.5, "faltas": 11},
]

def media_clase(alumnos):
    total = 0
    for alumno in alumnos:
        total += alumno["nota"]
    return total / len(alumnos)

def nombres_aprobados(alumnos):
    nombres = []
    for alumno in alumnos:
        if alumno["nota"] >= 5:
            nombres.append(alumno["nombre"])
    return nombres

def mejor_alumno(alumnos):
    mejor = alumnos[0]
    for alumno in alumnos:
        if alumno["nota"] > mejor["nota"]:
            mejor = alumno
    return mejor

def con_aviso(alumnos):
    nombres = []
    for alumno in alumnos:
        if alumno["faltas"] > 10:
            nombres.append(alumno["nombre"])
    return nombres

print("C12a:", media_clase(alumnos))
print("C12b:", nombres_aprobados(alumnos))
print("C12c:", mejor_alumno(alumnos))
print("C12c lambda:", max(alumnos, key=lambda a: a["nota"]))
print("C12d:", con_aviso(alumnos))
print("C12e:", sorted(alumnos, key=lambda a: a["nota"], reverse=True))
assert media_clase(alumnos) == 6.5
assert nombres_aprobados(alumnos) == ["Ana", "Marta", "Pedro"]
assert mejor_alumno(alumnos)["nombre"] == "Marta"
assert con_aviso(alumnos) == ["Luis", "Pedro"]


# C13
def contar_palabras(lista):
    frecuencias = {}
    for palabra in lista:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

print("C13:", contar_palabras(["sol", "mar", "sol"]))
assert contar_palabras(["sol", "mar", "sol"]) == {"sol": 2, "mar": 1}


# C14
precios = [12, 55, 8, 100, 30]
caros_con_descuento = list(map(lambda p: p * 0.9, filter(lambda p: p > 20, precios)))
print("C14:", caros_con_descuento)
assert caros_con_descuento == [49.5, 90.0, 27.0]


# C15  caso base: n == 1 (o n == 0 devolviendo 0)
def suma_hasta(n):
    if n == 1:
        return 1
    return n + suma_hasta(n - 1)

print("C15:", suma_hasta(5))
assert suma_hasta(5) == 15


# C16
def menu(opcion):
    match opcion:
        case "1":
            return "Alta"
        case "2":
            return "Baja"
        case "3":
            return "Listar"
        case _:
            return "Opción no válida"

print("C16:", menu("2"), menu("9"))
assert menu("1") == "Alta" and menu("x") == "Opción no válida"


# =====================================================================
# BLOQUE D — Estadística sin pandas
# =====================================================================
print("\n===== BLOQUE D =====")

puntos = [50, 60, 60, 70, 70, 80, 80, 80, 90, 100]


# D1
def media(lista):
    total = 0
    for x in lista:
        total += x
    return total / len(lista)

print("D1 media:", media(puntos))
assert media(puntos) == 74


# D2
def ordenar_burbuja(lista):
    o = lista.copy()
    for i in range(len(o) - 1):
        for j in range(len(o) - 1 - i):
            if o[j] > o[j + 1]:
                aux = o[j]
                o[j] = o[j + 1]
                o[j + 1] = aux
    return o

desordenada = [80, 50, 100, 60, 70]
print("D2:", ordenar_burbuja(desordenada), "original intacta:", desordenada)
assert ordenar_burbuja([3, 1, 2]) == [1, 2, 3]
assert desordenada == [80, 50, 100, 60, 70]


# D3
def mediana(lista):
    o = ordenar_burbuja(lista)
    n = len(o)
    if n % 2 == 0:
        return (o[n // 2 - 1] + o[n // 2]) / 2
    else:
        return o[n // 2]

print("D3 mediana:", mediana(puntos), mediana([3, 1, 2]))
assert mediana(puntos) == 75
assert mediana([3, 1, 2]) == 2


# D4
def moda(lista):
    frecuencias = {}
    for x in lista:
        if x in frecuencias:
            frecuencias[x] += 1
        else:
            frecuencias[x] = 1
    mas_repetido = lista[0]
    veces = 0
    for valor, cuantas in frecuencias.items():
        if cuantas > veces:
            veces = cuantas
            mas_repetido = valor
    return mas_repetido

print("D4 moda:", moda(puntos))
assert moda(puntos) == 80


# D5
def varianza(lista):
    m = media(lista)
    suma_cuadrados = 0
    for x in lista:
        suma_cuadrados += (x - m) ** 2
    return suma_cuadrados / len(lista)      # muestral: / (len(lista) - 1)

def desviacion_estandar(lista):
    return varianza(lista) ** 0.5

print("D5 varianza:", varianza(puntos), "desviación:", desviacion_estandar(puntos))
assert varianza(puntos) == 204
assert round(desviacion_estandar(puntos), 2) == 14.28


# D6
def normalizar(lista):
    minimo = lista[0]
    maximo = lista[0]
    for x in lista:
        if x < minimo:
            minimo = x
        if x > maximo:
            maximo = x
    resultado = []
    for x in lista:
        resultado.append((x - minimo) / (maximo - minimo))
    return resultado

print("D6 normalizados:", normalizar(puntos))
assert normalizar(puntos)[0] == 0 and normalizar(puntos)[-1] == 1


# D7
def z_scores(lista):
    m = media(lista)
    s = desviacion_estandar(lista)
    resultado = []
    for x in lista:
        resultado.append((x - m) / s)
    return resultado

print("D7 z:", [round(z, 2) for z in z_scores(puntos)])
# z positivo = por encima de la media (74): los de 80, 90 y 100.


# D8
def resumen(lista):
    return {
        "media": media(lista),
        "mediana": mediana(lista),
        "moda": moda(lista),
        "desviacion": desviacion_estandar(lista),
    }

print("D8:", resumen(puntos))


# D9 — versiones cortas
media_corta = sum(puntos) / len(puntos)
normalizados_cortos = list(map(lambda x: (x - min(puntos)) / (max(puntos) - min(puntos)), puntos))
z_cortos = [(x - media_corta) / desviacion_estandar(puntos) for x in puntos]
assert media_corta == media(puntos)
assert normalizados_cortos == normalizar(puntos)
assert z_cortos == z_scores(puntos)
print("D9: las versiones cortas coinciden con las largas")

# D10 — teoría
# - Poblacional: tienes TODOS los datos del grupo, divides entre n.
#   Muestral: tienes una parte de una población mayor, divides entre n - 1.
# - Porque la mediana es el valor que queda en el centro cuando están en orden.
# - sorted(l) devuelve una lista nueva y no toca l. l.sort() ordena l y devuelve None.
# - Burbuja: compara vecinos (j y j+1), el mayor "sube" al final en cada pasada.
#   Intercambio directo: compara la posición i con todas las siguientes y cambia cada vez que encuentra uno menor.
#   Selección: busca la posición del mínimo de lo que queda y hace UN solo intercambio por pasada.


# =====================================================================
# BLOQUE E — Simulacro
# =====================================================================
print("\n===== BLOQUE E =====")

# E1
productos = [
    {"nombre": "ratón", "precio": 15.0, "stock": 12},
    {"nombre": "teclado", "precio": 25.0, "stock": 0},
    {"nombre": "monitor", "precio": 120.0, "stock": 3},
    {"nombre": "cable", "precio": 4.5, "stock": 25},
]

def valor_inventario(productos):
    total = 0
    for p in productos:
        total += p["precio"] * p["stock"]
    return total

def agotados(productos):
    nombres = []
    for p in productos:
        if p["stock"] == 0:
            nombres.append(p["nombre"])
    return nombres

def reponer(productos, nombre, unidades):
    encontrado = False
    for p in productos:
        if p["nombre"] == nombre:
            p["stock"] += unidades
            encontrado = True
            break
    return encontrado

def mas_caro(productos):
    caro = productos[0]
    for p in productos:
        if p["precio"] > caro["precio"]:
            caro = p
    return caro["nombre"]

print("E1 valor inventario:", valor_inventario(productos))
print("E1 agotados:", agotados(productos))
print("E1 más caro:", mas_caro(productos))
print("E1 reponer teclado:", reponer(productos, "teclado", 5))
print("E1 reponer webcam:", reponer(productos, "webcam", 5))
print("E1 agotados después:", agotados(productos))
assert valor_inventario([{"precio": 2, "stock": 3}]) == 6
assert agotados(productos) == []
assert mas_caro(productos) == "monitor"


# E2
nombres = ["Ana", "Bruno", "Carla", "Diego", "Elena"]
notas = [6.5, 4.0, 9.5, 7.0, 3.5]

# 1
clase = {}
for nombre, nota in zip(nombres, notas):
    clase[nombre] = nota
print("E2.1:", clase)

# 2
def estadisticas(notas):
    total = 0
    maxima = notas[0]
    minima = notas[0]
    for n in notas:
        total += n
        if n > maxima:
            maxima = n
        if n < minima:
            minima = n
    return total / len(notas), maxima, minima

m, mx, mn = estadisticas(notas)
print("E2.2:", m, mx, mn)
assert (m, mx, mn) == (6.1, 9.5, 3.5)

# 3
for nombre, nota in clase.items():
    estado = "Aprobado" if nota >= 5 else "Suspenso"
    print(f"{nombre}: {nota} ({estado})")

# 4
por_encima = 0
for nota in notas:
    if nota > m:
        por_encima += 1
print("E2.4 por encima de la media:", por_encima)
assert por_encima == 3

# 5  items() da tuplas (nombre, nota): t[1] es la nota
ordenados = sorted(clase.items(), key=lambda t: t[1], reverse=True)
nombres_ordenados = []
for nombre, nota in ordenados:
    nombres_ordenados.append(nombre)
print("E2.5:", nombres_ordenados)
assert nombres_ordenados == ["Carla", "Diego", "Ana", "Bruno", "Elena"]

# E3 — teoría
# 1. print muestra por pantalla; return devuelve el valor a quien llamó para poder usarlo.
#    Sin return, la función devuelve None.
# 2. La lista se puede modificar [ ], la tupla no ( ). Lista: notas de un alumno que van cambiando.
#    Tupla: coordenadas (x, y) o una fecha (2026, 10, 28).
# 3. break: sale del bucle. continue: salta a la siguiente vuelta. pass: no hace nada (relleno).
# 4. Parámetro: el nombre en la definición, def f(nombre). Argumento: el valor en la llamada, f("Ana").
# 5. Un caso base que pare las llamadas.
# 6. 3, 6, 9  (el 12 no entra)

print("\nTodo correcto ✔")
