
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

import pandas as pd


#Ejercicio 1. Carga y exploración de datos

print("Ejercicio 1. Carga y exploración de datos")
print("=========================================")

# Carga el archivo CSV en un DataFrame llamado df.
#un dataframe es una estructura de datos bidimensional, como una tabla, que puede almacenar datos de diferentes tipos (como enteros, cadenas, etc.) en columnas. Cada fila del DataFrame representa un registro o una observación individual, mientras que cada columna representa una característica o variable de esos registros.
df = pd.read_csv("Machine_Learning/ejercicios/3ML/datos_estadistica_alumnos.csv")

# Printea las primeras filas del DataFrame para explorar los datos.
print(df.head())

# Guarda la columna puntos_prueba en una variable llamada puntos.
puntos = df["puntos_prueba"]

# Muestra cuántos datos hay en la columna.
print("Cantidad de datos:", len(puntos))

#las filas del CSV representan a cada uno de los alumnos
