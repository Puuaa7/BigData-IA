from pathlib import Path
import pandas as pd
import csv


# Ejercicio 1. Carga y exploración de datos
# - Carga el archivo CSV en un DataFrame llamado df.
# - Muestra las primeras filas.
# - Guarda la columna puntos_prueba en una variable llamada puntos.
# - Muestra cuántos datos hay en la columna.
# - Explica con tus palabras qué representa cada fila del CSV.
# Pandas que puedes usar: read_csv(), head(), len().

print("Ejercicio 1. Carga y exploración de datos")
print("=========================================")

print("1. Pandas")

# Carga el archivo CSV en un DataFrame llamado df.
# Un DataFrame es una tabla con filas y columnas.
df = pd.read_csv(Path(__file__).parent / "datos_estadistica_alumnos.csv")

# Muestro las primeras filas.
print(df.head())

# Guarda la columna puntos_prueba en una variable llamada puntos.
puntos = df["puntos_prueba"]

# Muestra cuántos datos hay en la columna.
print("Cantidad de datos:", len(puntos))

# Cada fila tiene los datos de un alumno.


print("")
print("2. Python nativo")

# Indicamos dónde está nuestro archivo
ruta = Path(__file__).parent / "datos_estadistica_alumnos.csv"

# Abrimos el archivo CSV y guardamos sus filas en una lista
# Abro el archivo para leerlo.
# utf-8 permite leer las tildes.
with open(ruta, "r", encoding="utf-8") as archivo:
    filas = list(csv.DictReader(archivo))


# Mostramos las primeras 5 filas
# El for muestra las filas una a una.
# Cada fila es un diccionario con los datos.
for fila in filas[:5]:
    print(fila)

# Creamos una lista vacía para guardar los puntos
puntos = []


# Recorremos las filas y guardamos cada puntuación
# Guardo los puntos en la lista.
# append sirve para añadir un elemento al final de la lista.
for fila in filas:
    puntos.append(fila["puntos_prueba"])

# Mostramos cuántas puntuaciones tenemos
print("Cantidad de datos:", len(puntos))

# Cada fila representa a un alumno y sus datos.



print("")
print("3. Python funcional")
print("===================")

# Uso la misma ruta de antes.

# Abrimos el CSV y guardamos sus filas en una lista
with open(ruta, "r", encoding="utf-8") as archivo:
    filas = list(csv.DictReader(archivo))

# Mostramos las primeras 5 filas
print(filas[:5])

# Extraemos los puntos de cada alumno usando map y lambda
puntos = list(map(lambda fila: fila["puntos_prueba"], filas))

# Mostramos cuántas puntuaciones tenemos
print("Cantidad de datos:", len(puntos))

# Cada fila del CSV representa a un alumno y sus datos.


print("")
# Ejercicio 2. Media
# - Calcula la media de puntos_prueba con el Método 1: bucle for, acumulador y len().
# - Calcula la misma media con el Método 2: sum(), len() y, si quieres practicarlo, map() con lambda.
# - Calcula la misma media con el Método 3: pandas usando .mean().
# - Muestra los tres resultados con nombres claros: media_bucle, media_funciones y media_pandas.
# - Comprueba que los tres resultados coinciden.
# - Explica qué significa esa media en el contexto de la prueba.
# Pandas que puedes usar: df["puntos_prueba"].mean().

print("Ejercicio 2. Media")








# 1. Python nativo
print("")
print("1. Python nativo")
print("===================")

puntos = []

# Recorremos las filas y guardamos cada puntuación
for fila in filas:
    puntos.append(int(fila["puntos_prueba"]))

# Sumo los puntos y divido entre los alumnos.
suma = 0
for valor in puntos:
    suma += valor

media_bucle = suma / len(puntos)

print("media_bucle:", media_bucle)


# 2. Python funcional
print("")
print("2. Python funcional")
print("===================")

# sum suma los puntos y len cuenta los alumnos.
media_funciones = sum(puntos) / len(puntos)

print("media_funciones:", media_funciones)


# 3. Pandas
print("")
print("3. Pandas")
print("===================")

media_pandas = df["puntos_prueba"].mean()

print("media_pandas:", media_pandas)


print("Coinciden:", media_bucle == media_funciones == media_pandas)

# La media del grupo es de 74 puntos.




print("")
# Ejercicio 3. Mediana
# - Calcula la mediana de puntos_prueba con el Método 1: ordenar la lista, comprobar si la cantidad de datos es par o impar y acceder por índice.
# - Calcula la misma mediana con el Método 2: sorted(), len() y acceso por índice. En este caso map() no es necesario.
# - Calcula la misma mediana con el Método 3: pandas usando .median().
# - Muestra los tres resultados con nombres claros: mediana_bucle, mediana_funciones y mediana_pandas.
# - Comprueba que los tres resultados coinciden.
# - Explica por qué la mediana representa el centro de los datos.
# Pandas que puedes usar: df["puntos_prueba"].median().

print("Ejercicio 3. Mediana")

# 1. Python nativo
print("")
print("1. Python nativo")
print("===================")

# Copio la lista de puntos.
ordenados = puntos.copy()
# Cambio los números de sitio para ordenarlos.
for pasada in range(len(ordenados)):
    for i in range(len(ordenados) - 1):
        if ordenados[i] > ordenados[i + 1]:
            temporal = ordenados[i]
            ordenados[i] = ordenados[i + 1]
            ordenados[i + 1] = temporal

mitad = len(puntos) // 2
# Si hay una cantidad par, uso los dos del medio.
if len(puntos) % 2 == 0:
    mediana_bucle = (ordenados[mitad - 1] + ordenados[mitad]) / 2
else:
    mediana_bucle = ordenados[mitad]

print("mediana_bucle:", mediana_bucle)


# 2. Python funcional
print("")
print("2. Python funcional")
print("===================")

# sorted ordena los puntos.
lista_ordenada = sorted(puntos)
if len(puntos) % 2 == 0:
    mediana_funciones = (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
else:
    mediana_funciones = lista_ordenada[mitad]

print("mediana_funciones:", mediana_funciones)


# 3. Pandas
print("")
print("3. Pandas")
print("===================")

mediana_pandas = df["puntos_prueba"].median()

print("mediana_pandas:", mediana_pandas)


print("Coinciden:", mediana_bucle == mediana_funciones == mediana_pandas)
# Sale 75 porque los dos puntos centrales son 70 y 80.
# Cinco alumnos quedan por debajo de 75 y cinco por encima.


print("")
# Ejercicio 4. Moda
# - Calcula la moda de puntos_prueba con el Método 1: recorre la lista con un bucle y crea un diccionario de frecuencias.
# - Calcula la misma moda con el Método 2: usa set(), count(), max() y una lambda para encontrar el valor más repetido.
# - Calcula la misma moda con el Método 3: pandas usando .mode().
# - Muestra los tres resultados con nombres claros: moda_bucle, moda_funciones y moda_pandas.
# - Comprueba que los tres resultados coinciden.
# - Explica qué significa que ese valor sea la moda.
# Pandas que puedes usar: df["puntos_prueba"].mode().

print("Ejercicio 4. Moda")

# 1. Python nativo
print("")
print("1. Python nativo")
print("===================")

# Cuento cuántas veces sale cada puntuación.
veces_mayor = 0
moda_bucle = puntos[0]
for valor in puntos:
    veces = 0
    for numero in puntos:
        if numero == valor:
            veces += 1
    if veces > veces_mayor:
        veces_mayor = veces
        moda_bucle = valor

print("moda_bucle:", moda_bucle)


# 2. Python funcional
print("")
print("2. Python funcional")
print("===================")

# Busco el número que más se repite.
moda_funciones = max(puntos, key=lambda valor: puntos.count(valor))

print("moda_funciones:", moda_funciones)


# 3. Pandas
print("")
print("3. Pandas")
print("===================")

moda_pandas = df["puntos_prueba"].mode().iloc[0]

print("moda_pandas:", moda_pandas)


print("Coinciden:", moda_bucle == moda_funciones == moda_pandas)
print("Veces que aparece:", veces_mayor)
# La moda es 80 porque aparece tres veces.


print("")
# Ejercicio 5. Desviación de cada dato respecto a la media
# - Calcula primero la media de puntos_prueba.
# - Calcula una lista de desviaciones con el Método 1: bucle for y append(). Cada valor debe ser punto - media.
# - Calcula la misma lista con el Método 2: map() y lambda.
# - Calcula las mismas desviaciones con el Método 3: pandas, restando la media directamente a la columna y creando una columna llamada desviacion.
# - Muestra las tres versiones y comprueba que contienen los mismos valores.
# - Explica qué significa que una desviación sea positiva, negativa o cero.
# Pandas que puedes usar: df["desviacion"] = df["puntos_prueba"] - media.

print("Ejercicio 5. Desviaciones respecto a la media")

# 1. Python nativo
print("")
print("1. Python nativo")
print("===================")

# Restamos la media a cada puntuación.
desviaciones_bucle = []
for valor in puntos:
    diferencia = valor - media_bucle
    desviaciones_bucle.append(diferencia)

print("desviaciones_bucle:", desviaciones_bucle)


# 2. Python funcional
print("")
print("2. Python funcional")
print("===================")

desviaciones_funciones = list(map(lambda valor: valor - media_funciones, puntos))

print("desviaciones_funciones:", desviaciones_funciones)


# 3. Pandas
print("")
print("3. Pandas")
print("===================")

df["desviacion"] = df["puntos_prueba"] - media_pandas
desviaciones_pandas = df["desviacion"].tolist()

print("desviaciones_pandas:", desviaciones_pandas)


print("Coinciden:", desviaciones_bucle == desviaciones_funciones == desviaciones_pandas)
# Negativo: menos que la media. Positivo: más que la media.
# Cero: igual que la media.


print("")
# Ejercicio 6. Varianza
# - Calcula la varianza de puntos_prueba con el Método 1: bucle for, desviaciones, cuadrados y promedio final.
# - Recuerda: primero se calcula cada desviación, después se eleva al cuadrado y finalmente se hace la media de esos cuadrados.
# - Calcula la misma varianza con el Método 2: map(), lambda, sum() y len().
# - Calcula la misma varianza con el Método 3: pandas usando ddof=0.
# - Muestra los tres resultados con nombres claros: varianza_bucle, varianza_funciones y varianza_pandas.
# - Comprueba que los tres resultados coinciden.
# - Explica qué nos dice la varianza sobre el grupo.
# Pandas que puedes usar: df["puntos_prueba"].var(ddof=0).

print("Ejercicio 6. Varianza poblacional")

# 1. Python nativo
print("")
print("1. Python nativo")
print("===================")

# Sumamos las diferencias al cuadrado y dividimos entre los alumnos.
suma_cuadrados = 0
for diferencia in desviaciones_bucle:
    suma_cuadrados += diferencia ** 2
varianza_bucle = suma_cuadrados / len(puntos)

print("varianza_bucle:", varianza_bucle)


# 2. Python funcional
print("")
print("2. Python funcional")
print("===================")

cuadrados = list(map(lambda diferencia: diferencia ** 2, desviaciones_funciones))
varianza_funciones = sum(cuadrados) / len(puntos)

print("varianza_funciones:", varianza_funciones)


# 3. Pandas
print("")
print("3. Pandas")
print("===================")

# Con ddof=0 divido entre los 10 alumnos.
varianza_pandas = df["puntos_prueba"].var(ddof=0)

print("varianza_pandas:", varianza_pandas)


print("Coinciden:", varianza_bucle == varianza_funciones == varianza_pandas)
# La varianza da 204. Indica cuánto se separan los puntos de la media.


print("")
# Ejercicio 7. Desviación estándar
# - Calcula la desviación estándar con el Método 1: parte de la varianza calculada con bucles y aplica la raíz cuadrada.
# - Calcula la misma desviación estándar con el Método 2: usa map(), lambda, sum(), len() y raíz cuadrada.
# - Calcula la misma desviación estándar con el Método 3: pandas usando .std(ddof=0).
# - Muestra los tres resultados con nombres claros: desviacion_estandar_bucle, desviacion_estandar_funciones y desviacion_estandar_pandas.
# - Comprueba que los tres resultados coinciden o que solo cambian por pequeños decimales.
# - Explica por qué la desviación estándar es más fácil de interpretar que la varianza.
# Pandas que puedes usar: df["puntos_prueba"].std(ddof=0).

print("Ejercicio 7. Desviación estándar poblacional")

# 1. Python nativo
print("")
print("1. Python nativo")
print("===================")

# Elevar a 0.5 sirve para calcular la raíz cuadrada.
desviacion_estandar_bucle = varianza_bucle ** 0.5

print("desviacion_estandar_bucle:", desviacion_estandar_bucle)


# 2. Python funcional
print("")
print("2. Python funcional")
print("===================")

desviacion_estandar_funciones = varianza_funciones ** 0.5

print("desviacion_estandar_funciones:", desviacion_estandar_funciones)


# 3. Pandas
print("")
print("3. Pandas")
print("===================")

desviacion_estandar_pandas = df["puntos_prueba"].std(ddof=0)

print("desviacion_estandar_pandas:", desviacion_estandar_pandas)


# Redondeo para comparar los resultados.
print("Coinciden:", round(desviacion_estandar_bucle, 8) == round(desviacion_estandar_funciones, 8) == round(desviacion_estandar_pandas, 8))
# Da unos 14.28 puntos. Es más fácil de entender porque está en puntos.


print("")
# Ejercicio 8. Normalización min-max
# - Calcula el mínimo y el máximo de puntos_prueba.
# - Normaliza cada valor con el Método 1: bucle for y append(), usando la fórmula (valor - mínimo) / (máximo - mínimo).
# - Normaliza los mismos valores con el Método 2: min(), max(), map() y lambda.
# - Normaliza los mismos valores con el Método 3: pandas usando .min(), .max() y operaciones sobre columnas. Crea una columna llamada puntos_normalizados.
# - Muestra las tres versiones y comprueba que contienen los mismos valores.
# - Explica qué significa que un valor normalizado sea 0, 0.5 o 1.
# Pandas que puedes usar: min(), max() y operaciones directas sobre columnas.

print("Ejercicio 8. Normalización min-max")

# 1. Python nativo
print("")
print("1. Python nativo")
print("===================")

# Buscamos el menor y el mayor recorriendo los puntos.
minimo = puntos[0]
maximo = puntos[0]
for valor in puntos:
    if valor < minimo:
        minimo = valor
    if valor > maximo:
        maximo = valor

normalizados_bucle = []
for valor in puntos:
    resultado = (valor - minimo) / (maximo - minimo)
    normalizados_bucle.append(resultado)

print("normalizados_bucle:", normalizados_bucle)


# 2. Python funcional
print("")
print("2. Python funcional")
print("===================")

minimo_funciones = min(puntos)
maximo_funciones = max(puntos)
normalizados_funciones = list(map(
    lambda valor: (valor - minimo_funciones) / (maximo_funciones - minimo_funciones), puntos
))

print("normalizados_funciones:", normalizados_funciones)


# 3. Pandas
print("")
print("3. Pandas")
print("===================")

columna = df["puntos_prueba"]
df["puntos_normalizados"] = (columna - columna.min()) / (columna.max() - columna.min())
normalizados_pandas = df["puntos_normalizados"].tolist()
print("Mínimo:", minimo)
print("Máximo:", maximo)

print("normalizados_pandas:", normalizados_pandas)


print("Coinciden:", normalizados_bucle == normalizados_funciones == normalizados_pandas)
# Cambiamos los puntos a una escala de 0 a 1.
# 0 corresponde a 50 puntos, 1 a 100 puntos y 0.5 a 75 puntos.


print("")
# Ejercicio 9. Estandarización z-score
# - Calcula la media y la desviación estándar de puntos_prueba.
# - Estandariza cada valor con el Método 1: bucle for y append(), usando la fórmula z = (valor - media) / desviación estándar.
# - Estandariza los mismos valores con el Método 2: map(), lambda y las variables media y desviación estándar ya calculadas.
# - Estandariza los mismos valores con el Método 3: pandas usando .mean(), .std(ddof=0) y operaciones sobre columnas. Crea una columna llamada puntos_estandarizados.
# - Muestra las tres versiones y comprueba que contienen los mismos valores.
# - Explica qué significa que un valor z sea positivo, negativo o cercano a 0.
# Pandas que puedes usar: mean(), std(ddof=0) y operaciones directas sobre columnas.

print("Ejercicio 9. Estandarización z-score")

# 1. Python nativo
print("")
print("1. Python nativo")
print("===================")

# Restamos la media y dividimos entre la desviación estándar.
estandarizados_bucle = []
for valor in puntos:
    resultado = (valor - media_bucle) / desviacion_estandar_bucle
    estandarizados_bucle.append(resultado)

print("estandarizados_bucle:", estandarizados_bucle)


# 2. Python funcional
print("")
print("2. Python funcional")
print("===================")

estandarizados_funciones = list(map(
    lambda valor: (valor - media_funciones) / desviacion_estandar_funciones, puntos
))

print("estandarizados_funciones:", estandarizados_funciones)


# 3. Pandas
print("")
print("3. Pandas")
print("===================")

df["puntos_estandarizados"] = (df["puntos_prueba"] - media_pandas) / desviacion_estandar_pandas
estandarizados_pandas = df["puntos_estandarizados"].tolist()

print("estandarizados_pandas:", estandarizados_pandas)


coinciden = True
for i in range(len(puntos)):
    if round(estandarizados_bucle[i], 8) != round(estandarizados_funciones[i], 8):
        coinciden = False
    if round(estandarizados_bucle[i], 8) != round(estandarizados_pandas[i], 8):
        coinciden = False
print("Coinciden:", coinciden)
# Si sale 1, está una desviación estándar por encima de la media.
# Negativo: por debajo. Cerca de 0: cerca de la media.


print("")
# Ejercicio 10. Interpretación final
# - Indica qué alumnos están por encima de la media usando el Método 1: bucle for y condicional.
# - Indica los mismos alumnos usando el Método 2: filter() y lambda.
# - Indica los mismos alumnos usando el Método 3: filtrado de pandas con condiciones sobre columnas.
# - Indica qué alumnos están por debajo de la media usando también los tres métodos.
# - Indica qué alumno o alumnos tienen el valor normalizado más alto.
# - Indica qué alumno o alumnos tienen el valor normalizado más bajo.
# - Indica si hay algún valor que parezca especialmente alejado del resto.
# - Escribe una conclusión breve sobre el rendimiento general del grupo.

print("Ejercicio 10. Interpretación final")

# 1. Python nativo
print("")
print("1. Python nativo")
print("===================")

encima_bucle = []
debajo_bucle = []
mayor_normalizado_bucle = []
menor_normalizado_bucle = []
mas_alejados_bucle = []

# abs quita el signo negativo.
distancia_mayor = 0
for diferencia in desviaciones_bucle:
    if abs(diferencia) > distancia_mayor:
        distancia_mayor = abs(diferencia)

for i in range(len(puntos)):
    nombre = filas[i]["nombre"]
    if puntos[i] > media_bucle:
        encima_bucle.append(nombre)
    elif puntos[i] < media_bucle:
        debajo_bucle.append(nombre)
    if normalizados_bucle[i] == 1:
        mayor_normalizado_bucle.append(nombre)
    if normalizados_bucle[i] == 0:
        menor_normalizado_bucle.append(nombre)
    if abs(desviaciones_bucle[i]) == distancia_mayor:
        mas_alejados_bucle.append(nombre)

print("Por encima (bucle):", encima_bucle)
print("Por debajo (bucle):", debajo_bucle)
print("Mayor normalizado (bucle):", mayor_normalizado_bucle)
print("Menor normalizado (bucle):", menor_normalizado_bucle)
print("Más alejados (bucle):", mas_alejados_bucle)


# 2. Python funcional
print("")
print("2. Python funcional")
print("===================")

# filter selecciona los alumnos.
# map saca sus nombres.
# int pasa los puntos a número.

# Alumnos por encima de la media
alumnos_encima = filter(lambda fila: int(fila["puntos_prueba"]) > media_funciones, filas)
encima_funciones = list(map(lambda fila: fila["nombre"], alumnos_encima))

# Alumnos por debajo de la media
alumnos_debajo = filter(lambda fila: int(fila["puntos_prueba"]) < media_funciones, filas)
debajo_funciones = list(map(lambda fila: fila["nombre"], alumnos_debajo))

# Busco los alumnos con más puntos.
alumnos_maximo = filter(lambda fila: int(fila["puntos_prueba"]) == maximo_funciones, filas)
mayor_normalizado_funciones = list(map(lambda fila: fila["nombre"], alumnos_maximo))

# Busco los alumnos con menos puntos.
alumnos_minimo = filter(lambda fila: int(fila["puntos_prueba"]) == minimo_funciones, filas)
menor_normalizado_funciones = list(map(lambda fila: fila["nombre"], alumnos_minimo))

# Busco la mayor distancia a la media.
distancia_funciones = max(map(abs, desviaciones_funciones))
alumnos_alejados = filter(
    lambda fila: abs(int(fila["puntos_prueba"]) - media_funciones) == distancia_funciones,
    filas
)
mas_alejados_funciones = list(map(lambda fila: fila["nombre"], alumnos_alejados))

print("Por encima (funciones):", encima_funciones)
print("Por debajo (funciones):", debajo_funciones)
print("Mayor normalizado (funciones):", mayor_normalizado_funciones)
print("Menor normalizado (funciones):", menor_normalizado_funciones)
print("Más alejados (funciones):", mas_alejados_funciones)


# 3. Pandas
print("")
print("3. Pandas")
print("===================")

# Con loc saco los nombres que cumplen la condición.
encima_pandas = df.loc[df["puntos_prueba"] > media_pandas, "nombre"].tolist()
debajo_pandas = df.loc[df["puntos_prueba"] < media_pandas, "nombre"].tolist()
mayor_normalizado_pandas = df.loc[df["puntos_normalizados"] == 1, "nombre"].tolist()
menor_normalizado_pandas = df.loc[df["puntos_normalizados"] == 0, "nombre"].tolist()
distancias = df["desviacion"].abs()
mas_alejados_pandas = df.loc[distancias == distancias.max(), "nombre"].tolist()

print("Por encima (pandas):", encima_pandas)
print("Por debajo (pandas):", debajo_pandas)
print("Mayor normalizado (pandas):", mayor_normalizado_pandas)
print("Menor normalizado (pandas):", menor_normalizado_pandas)
print("Más alejados (pandas):", mas_alejados_pandas)


coinciden = (
    encima_bucle == encima_funciones == encima_pandas
    and debajo_bucle == debajo_funciones == debajo_pandas
    and mayor_normalizado_bucle == mayor_normalizado_funciones == mayor_normalizado_pandas
    and menor_normalizado_bucle == menor_normalizado_funciones == menor_normalizado_pandas
    and mas_alejados_bucle == mas_alejados_funciones == mas_alejados_pandas
)
print("Coinciden:", coinciden)

# Lucía tiene el mayor normalizado (1) y Ana el menor (0).
# Lucía es la que más se aleja de la media, con 26 puntos más.
# La media es 74, la mediana 75 y la moda 80.
# Siete de los diez alumnos tienen entre 60 y 80 puntos.
# Al normalizar los valores van de 0 a 1.
# Al estandarizar veo cuánto se alejan de la media.

print("")
print("Tabla final:")
print(df[["nombre", "puntos_prueba", "desviacion", "puntos_normalizados", "puntos_estandarizados"]])

# Me ha costado bastante hacer estos ejercicios e incluso entender la solucion.
# Sin mirar la solución no los habría podido terminar y todavía hay partes que me cuestan.
# Los entrego porque dijiste que era obligatorio entregar los 10 ejercicios,
# pero he necesitado mucha ayuda de la solución para poder hacerlos.
