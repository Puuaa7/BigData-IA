
# ==================================================
# EJERCICIO 1. Carga y exploración de datos
# ==================================================
# - Carga el archivo CSV en un DataFrame llamado df.
# - Muestra las primeras filas.
# - Guarda la columna puntos_prueba en una variable llamada puntos.
# - Muestra cuántos datos hay en la columna.
# - Explica con tus palabras qué representa cada fila del CSV.
#
# Pandas que puedes usar: read_csv(), head(), len().

from zipfile import Path
from pathlib import Path
import pandas as pd
import csv

# Ejercicio 1. Carga y exploración de datos

print("Ejercicio 1. Carga y exploración de datos")
print("=========================================")

print("1. Pandas")

# Carga el archivo CSV en un DataFrame llamado df.
# un dataframe es una estructura de datos bidimensional, como una tabla, que puede almacenar datos de diferentes tipos (como enteros, cadenas, etc.) en columnas. Cada fila del DataFrame representa un registro o una observación individual, mientras que cada columna representa una característica o variable de esos registros.
df = pd.read_csv(Path(__file__).parent / "datos_estadistica_alumnos.csv")

# Printea las primeras filas del DataFrame para explorar los datos.
print(df.head())

# Guarda la columna puntos_prueba en una variable llamada puntos.
puntos = df["puntos_prueba"]

# Muestra cuántos datos hay en la columna.
print("Cantidad de datos:", len(puntos))

# Cada fila del CSV representa a un alumno y contiene la información correspondiente a ese alumno, como su puntuación en la prueba.


print("")
print("2. Pyton nativo")

# Indicamos dónde está nuestro archivo
ruta = Path(__file__).parent / "datos_estadistica_alumnos.csv"

# Abrimos el archivo CSV y guardamos sus filas en una lista
# open sirve para abrir un archivo y con el parámetro "r" le decimos que lo abra en modo lectura.
# encoding="utf-8" es para que lea correctamente los caracteres especiales.
with open(ruta, "r", encoding="utf-8") as archivo:
    filas = list(csv.DictReader(archivo))


# Mostramos las primeras 5 filas
# Este for recorre las primeras 5 filas de la lista filas y las imprime una por una.
# Cada fila es un diccionario donde las claves son los nombres de las columnas y los valores son los datos correspondientes a esa fila.
for fila in filas[:5]:
    print(fila)

# Creamos una lista vacía para guardar los puntos
puntos = []


# Recorremos las filas y guardamos cada puntuación
# Este for recorre todas las filas de la lista filas y añade el valor de la columna "puntos_prueba" a la lista puntos.
# append sirve para añadir un elemento al final de la lista.
for fila in filas:
    puntos.append(fila["puntos_prueba"])

# Mostramos cuántas puntuaciones tenemos
print("Cantidad de datos:", len(puntos))

# Cada fila representa a un alumno y sus datos.



print("")
print("3. Python funcional")
print("===================")

# Utilizamos la variable ruta que ya hemos creado
# en los ejercicios anteriores.

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
print("Ejercicio 2. Media")

# - Calcula la media de puntos_prueba con el Método 1: bucle for, acumulador y len().

# - Calcula la misma media con el Método 2: sum(), len() y, si quieres practicarlo, map() con lambda.

# - Calcula la misma media con el Método 3: pandas usando .mean().

# - Muestra los tres resultados con nombres claros: media_bucle, media_funciones y media_pandas.

# - Comprueba que los tres resultados coinciden.

# - Explica qué significa esa media en el contexto de la prueba.

# Pandas que puedes usar: df["puntos_prueba"].mean().

puntos = []

# Recorremos las filas y guardamos cada puntuación
for fila in filas:
    puntos.append(int(fila["puntos_prueba"]))

# Calculamos la media con el Método 1: bucle for, acumulador y len().
suma = 0
for valor in puntos:
    suma += valor

media_bucle = suma / len(puntos)

print("media_bucle:", media_bucle)

# De promedio, cada alumno sacó 74 puntos: si se repartieran todos los puntos por igual, a cada uno le tocarían 74.




print("")
print("Ejercicio 3. Mediana")