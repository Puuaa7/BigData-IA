import pandas as pd








#Ejercicio 1. Crear la estructura de datos

datos = {
    "nombre": ["Ana", "Paco", "Marta", "Luis", "Elena", "Carlos", "Sara", "Miguel", "Lucia", "Andres"],
    "edad": [23, 21, 19, 25, 22, 20, 18, 27, 21, 24],
    "puntos": [43, 38, 41, 35, 39, 36, 34, 45, 42, 37],
    "estudiosSuperiores": [True, False, True, False, True, True, False, False, True, False]
}


#Ejercicio 2. Crear un DataFrame
df = pd.DataFrame(datos)
print(df)
print("----------------------------------------")
#Ejercicio 3. Explorar el DataFrame

print(df.head())  # Muestra las primeras filas del DataFrame
print("----------------------------------------")
print(df.shape)  # Muestra cuantas filas y columnas tiene el DataFrame
print("----------------------------------------")
print(df.columns)  # Muestra los nombres de las columnas del DataFrame
print("----------------------------------------")
print(df.dtypes)  # Muestra los tipos de datos de cada columna del DataFrame
print("----------------------------------------")
df.info()  # Muestra un resumen del DataFrame, incluyendo el número de entradas, columnas y tipos de datos
print("----------------------------------------")
print(df.describe())  # Calcula estadísticas basicas para las columnas numéricas del DataFrame

#head, info y describe son métodos por eso llevan "()", mientras que shape, columns y dtypes son atributos por eso no lo llevan.



# Ejercicio 4. Crear una regla de selección
# Si tiene 22 años o más, necesita mínimo 40 puntos para ser apto.
# Si tiene menos de 22 años, necesita estudios superiores y al menos 35 puntos.
# Si no cumple ninguna de estas condiciones, no es apto.
print("----------------------------------------")
# Ejercicio 5. Añadir una nueva columna

#crear lista vacia
aptos = []

#recorremos las personas
for i in range(len(df)):
    #obtenemos los valores de cada persona
    edad = df["edad"][i]
    puntos = df["puntos"][i]
    estudios = df["estudiosSuperiores"][i]

    #comprobamos las condiciones
    if edad >= 22 and puntos >= 40:
        #append sirve para añadir un elemento al final de la lista
        aptos.append(True)
    elif edad < 22 and estudios == True and puntos >= 35:
        aptos.append(True)
    else:
        aptos.append(False)

# Añadir la nueva columna al DataFrame
df["apto"] = aptos
print(df)


print("----------------------------------------")
#Ejercicio 6. Contar personas aptas y no aptas
#value_counts() sirve para contar quantas veces aparece cada valor en una columna
print(df["apto"].value_counts())




print("----------------------------------------")
#Ejercicio 7. Filtrar candidatos aptos
#guardar en una nueva variable los candidatos aptos
candidatosAptos = df[df["apto"] == True]
print(candidatosAptos)

# tabla["apto"]      → Selecciona la columna apto.
# == True            → Comprueba qué personas son aptas.
# tabla[...]         → Filtra la tabla y se queda solo con esas personas.
# candidatos_aptos = → Guarda el resultado en una nueva variable.



print("----------------------------------------")
#Ejercicio 8. Filtrar candidatos con estudios superiores
# RECORDOAR! == sirve para comparar si dos valores son iguales, mientras que = sirve para asignar un valor a una variable

conEstudios = df[df["estudiosSuperiores"] == True]

print(conEstudios)

# Cuantas personas tiene estudios superiores
print("Personas con estudios superiores: ", len(conEstudios))

# Cuantos aptos con estudios superiores
print("Personas aptas: ", conEstudios["apto"].sum())

# No aptas con estudios superiores
print("Personas no aptas: ", (conEstudios["apto"] == False).sum())




print("----------------------------------------")
#Ejercicio 9. Ordenar los candidatos

# Ordenar de menor a mayor
print("Orden de menor a mayor:")
#sort_values() sirve para ordenar los valores de una columna
print(df.sort_values("puntos"))
print("")
print("orden de mayor a menor:")
# Ordenar de mayor a menor
#ascending=False cambia el orden de mayor a menor
print(df.sort_values("puntos", ascending= False))



print("----------------------------------------")
#Ejercicio 10. Calcular estadísticas

print("Edad media: ", df["edad"].mean())

print("Puntuación media:", df["puntos"].mean())

print("Puntuación maxima: ", df["puntos"].max())

print("Puntuación minima: ", df["puntos"].min())

print("Mas joven: ", df["edad"].min())

print("Mas viejo: ", df["edad"].max())

#no hace falta for ni if porque pandas ya tiene métodos para calcular estas estadísticas.
#.mean() calcula la media de los valores de una columna
#.max() calcula el valor máximo de una columna
#.min() calcula el valor mínimo de una columna



print("----------------------------------------")
#Ejercicio 11. Crear una columna de nivel

nivel = []

for punts in df["puntos"]:
    if punts >= 40:
        nivel.append("Alto")
    elif punts >= 35:
        nivel.append("Medio")
    else:
        nivel.append("Bajo")


#crear una nueva columna en el DataFrame con los niveles
df["nivel"] = nivel
#Si la columna "nivel" ya existiera, se sobreescribiría con los nuevos valores.



print("----------------------------------------")
#Ejercicio 12. Agrupar por nivel

#groupby() sirve para juntar las filas que tienen algo en común, en este caso el nivel. size() sirve para contar cuantas filas hay en cada grupo.

print(df.groupby("nivel").size())

print(df.groupby("nivel")["edad"].mean())

print(df.groupby("nivel")["puntos"].mean())



print("----------------------------------------")
 #Ejercicio 13. Seleccionar columnas concretas

#para seleccionar columnas concretas de un DataFrame, se puede usar la sintaxis df[["columna1", "columna2"]].
#Esto devuelve un nuevo DataFrame con solo esas columnas.
tablaReducida = df[["nombre", "puntos", "apto"]]
print(tablaReducida)



print("----------------------------------------")
#Ejercicio 14. Renombrar columnas

#rename() sirve para modificar el nombre de las columnas de un DataFrame.
df = df.rename(columns={
    "nombre": "Nom",
    "edad": "Edat",
    "puntos": "Punts",
    "estudiosSuperiores": "Estudis superiors",
    "apto": "Apte",
    "nivel": "Nivell"
})

print(df)
