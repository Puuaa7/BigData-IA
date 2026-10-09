

#Ejercicio 1. Control de notas
#Crea una lista llamada notas con al menos 10 calificaciones numéricas.
#El programa debe:
#- Mostrar todas las notas.
#- Calcular cuántas notas están aprobadas y cuántas suspendidas.
#- Calcular la nota media.
#- Mostrar la nota más alta y la nota más baja.
#- Indicar si la media final está aprobada o suspendida.
#Condición: Debe utilizar listas, bucle for, operadores de comparación y condicionales.

print("Solución del ejercicio 1")

notas = [6, 8, 5, 4, 7, 10, 4, 6, 1, 6]

print("notas:", notas)


aprobados= 0
suspendidos= 0
total= 0
notaMasAlta= notas[0]
notaMasBaja= notas[0]


for nota in notas:
    total += nota
    if nota >= 5:
        aprobados+= 1
    else:
        suspendidos+=1
    if nota > notaMasAlta:
        notaMasAlta= nota
    if nota < notaMasBaja:
        notaMasBaja= nota

media = total / len(notas)



print("Nota media:", media)
print("Aprobados: ",aprobados)
print("Suspensos: ",suspendidos)
print("Nota mas alta: ", notaMasAlta)
print("Nota mas baja: ", notaMasBaja)

if media >= 5:
    print("Media aprovada")
else:
    print("media suspendida")



# Ejercicio 2. Carrito de la compra
# Crea dos listas: una con nombres de productos y otra con sus precios.
# productos = ["pan", "leche", "arroz", "huevos"]
# precios = [1.20, 0.95, 2.10, 2.80]
# El programa debe:
# - Mostrar cada producto con su precio.
# - Calcular el precio total de la compra.
# - Aplicar un descuento del 10% si el total supera 20 euros.
# - Mostrar el total final que debe pagarse.
# Condición: Debe utilizar zip, un acumulador, if y operadores aritméticos.

print("")
print("Solución del ejercicio 2")

productos = ["pan", "leche", "arroz", "huevos"]
precios = [1.20, 0.95, 2.10, 2.80]
total = 0

for producto, precio in zip(productos, precios):
    print(producto, precio)
    total += precio

if total > 20:
    descuento = total * 0.10
    total -= descuento

print("Total final a pagar:", total)




# Ejercicio 3. Registro de alumno
# Crea un diccionario llamado alumno con los siguientes datos:
# nombre
# edad
# curso
# nota_media
# faltas
# El programa debe:
# - Mostrar todos los datos del alumno.
# - Indicar si el alumno aprueba. Aprueba si su nota_media es mayor o igual que 5.
# - Indicar si debe recibir un aviso. Recibe aviso si tiene más de 10 faltas.
# - Mostrar un mensaje final combinando el resultado académico y el aviso por faltas.
# Condición: Debe utilizar diccionarios, if, elif, else y operadores lógicos.

print("")
print("Solución del ejercicio 3")

alumno = {
    "nombre": "Isaac",
    "edad": 45,
    "curso": "Big Data",
    "nota_media": 8.5,
    "faltas": 12
}
#items() devuelve una lista de tuplas, donde cada tupla contiene un par clave-valor del diccionario.
#en este caso, se utiliza un bucle for para iterar sobre cada par clave-valor del diccionario alumno y se imprime la clave y el valor correspondiente.
for clave, valor in alumno.items():
    print(clave, ":", valor)
if alumno["nota_media"] >= 5 and alumno["faltas"] <= 10:
    print("Alumno aprobado y sin aviso por faltas.")
elif alumno["nota_media"] >= 5 and alumno["faltas"] > 10:
    print("Alumno aprobado pero con aviso por faltas.")
elif alumno["nota_media"] < 5 and alumno["faltas"] > 10:
    print("Alumno suspendido y con aviso por faltas.")
else:
    print("Alumno suspendido pero sin aviso por faltas.")



# Ejercicio 4. Números pares, impares y múltiplos
# Usando range, recorre los números del 1 al 50.
# El programa debe:
# - Contar cuántos números son pares.
# - Contar cuántos números son impares.
# - Contar cuántos números son múltiplos de 5.
# - Mostrar los tres resultados finales.
# Condición: Debe utilizar for, range, el operador módulo % y contadores.


print("")
print("Solución del ejercicio 4")

pares = 0
impares = 0
multiplos5 = 0

# Recorrer los números del 1 al 50
for numero in range(1, 51):
    # Contar pares, impares y múltiplos de 5
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero % 5 == 0:
        multiplos5 += 1


print("Números pares:", pares)
print("Números impares:", impares)
print("Números múltiplos de 5:", multiplos5)


# Ejercicio 5. Validación de contraseña
# Crea una variable llamada password con una contraseña de prueba.
# El programa debe:
# - Comprobar si la contraseña tiene al menos 8 caracteres.
# - Comprobar si contiene el símbolo @.
# - Comprobar que no sea igual a 12345678.
# - Si cumple todas las condiciones, mostrar Contraseña válida.
# - En caso contrario, mostrar Contraseña no válida.
# Condición: Debe utilizar strings, len, operadores lógicos y condicionales. Para comprobar si aparece @ dentro
# del texto puede utilizarse "@" in password.

print("")
print("Solución del ejercicio 5")

password = "marulete@123"

# Comprobar si la contraseña cumple las condiciones con un condicional if y operadores lógicos
if len(password) >= 8 and "@" in password and password != "12345678":
    print("Contraseña válida")
else:
    print("Contraseña no válida")



# Ejercicio 6. Inventario de productos
# Crea un diccionario donde las claves sean nombres de productos y los valores sean las unidades
# disponibles.
# inventario = {
#  "ratón": 12,
#  "teclado": 5,
#  "monitor": 0,
#  "cable": 25
# }
# El programa debe:
# - Mostrar todos los productos y sus unidades.
# - Mostrar qué productos están agotados.
# - Calcular cuántas unidades hay en total.
# - Mostrar cuántos productos tienen menos de 10 unidades.
# Condición: Debe utilizar diccionarios, items(), acumuladores, contadores e if.


print("")
print("Solución del ejercicio 6")

inventario = {
    "ratón": 12,
    "teclado": 5,
    "monitor": 0,
    "cable": 25
}

totalUnidades = 0
productosMenosDe10 = 0

# Recorrer el diccionario inventario con un bucle for y items()
for producto, unidades in inventario.items():
    print(producto, ":", unidades)
    totalUnidades += unidades
    # Comprobar si el producto está agotado y si tiene menos de 10 unidades
    if unidades == 0:
        print(producto, "está agotado.")
    if unidades < 10:
        productosMenosDe10 += 1

print("Total de unidades:", totalUnidades)
print("Productos con menos de 10 unidades:", productosMenosDe10)


# Ejercicio 7. Búsqueda en una lista
# Crea una lista de nombres de alumnos y una variable con el nombre que se quiere buscar.
# El programa debe:
# - Recorrer la lista buscando ese nombre.
# - Si encuentra el nombre, mostrar en qué posición está.
# - Cuando lo encuentre, detener la búsqueda.
# - Si no lo encuentra, mostrar Alumno no encontrado.
# Condición: Debe utilizar listas, for, enumerate, if, break y una variable booleana de control.

print("")
print("Solución del ejercicio 7")

alumnos = ["Isaac", "Anna", "Carles", "Pau", "Alex"]
buscar = "Pau"
encontrado = False

# Recorrer la lista de alumnos con un bucle for y enumerate() para obtener la posición y el nombre
for posicion, nombre in enumerate(alumnos):
    # Comprobar si el nombre coincide con el que se busca
    if nombre == buscar:
        print("Alumno encontrado en la posición:", posicion)
        encontrado = True
        #si se encuentra el alumno, se detiene la búsqueda con break
        break

#inf encontrado == false, también se puede escribir como if not encontrado:
if not encontrado:
    print("Alumno no encontrado.")




# Ejercicio 8. Limpieza de datos
# Crea una lista con varios números, incluyendo positivos, negativos y ceros.
# El programa debe:
# - Recorrer la lista completa.
# - Ignorar los números negativos usando continue.
# - Sumar solo los números positivos.
# - Contar cuántos ceros hay.
# - Mostrar la suma final y la cantidad de ceros.
# Condición: Debe utilizar listas, for, continue, un acumulador y un contador.

print("")
print("Solución del ejercicio 8")

numeros = [5, -7, 0, 10, -1, 0, 7, 10, -3, 0]

sumaPositivos = 0
contadorCeros = 0

# Recorrer la lista de números con un bucle for
for n in numeros:
    # Comprobar si el número es negativo y usar continue para ignorarlo
    if n < 0:
        #continue hace que el bucle pase a la siguiente iteración sin ejecutar el resto del código dentro del bucle para ese número negativo.
        continue
    # Comprobar si el número es cero y contar los ceros, o sumar los positivos
    if n == 0:
        contadorCeros += 1
    else:
        sumaPositivos += n

print("Suma de números positivos:", sumaPositivos)
print("Cantidad de ceros:", contadorCeros)



# Ejercicio 9. Clasificación de usuarios
# Crea una lista de diccionarios. Cada diccionario representa un usuario con los siguientes datos:
# nombre
# edad
# activo
# puntos
# El programa debe:
# - Clasificar como Premium a los usuarios activos con 100 puntos o más.
# - Clasificar como Estándar a los usuarios activos con menos de 100 puntos.
# - Clasificar como Inactivo a los usuarios que no estén activos.
# - Además, si el usuario es menor de 18 años, debe indicarse como usuario menor de edad.
# - Mostrar el nombre de cada usuario y su clasificación.
# Condición: Debe utilizar una lista de diccionarios, bucle for, booleanos, if, elif, else y operadores lógicos.

print("")
print("Solución del ejercicio 9")

usuarios = [
    {"nombre": "Pau", "edad": 24, "activo": True, "puntos": 120},
    {"nombre": "Marc", "edad": 17, "activo": True, "puntos": 80},
    {"nombre": "Alex", "edad": 21, "activo": False, "puntos": 150}
]

for usuario in usuarios:
    # Clasificar al usuario según su estado y puntos, el if not usuario["activo"] verifica si el usuario no está activo, y en ese caso se le asigna la clasificación "Inactivo". Si el usuario está activo, se evalúa su cantidad de puntos para determinar si es "Premium" o "Estándar".
    if not usuario["activo"]:
        clasificacion = "Inactivo"
    elif usuario["puntos"] >= 100:
        clasificacion = "Premium"
    else:
        clasificacion = "Estándar"

    if usuario["edad"] < 18:
        #al usar += se añade la cadena " (menor de edad)" a la variable clasificacion, manteniendo la clasificación original y agregando la información adicional sobre la edad del usuario.
        clasificacion += " (menor de edad)"

    print(usuario["nombre"], ":", clasificacion)


# Ejercicio 10. Sistema de intentos
# Crea una variable codigo_correcto y una lista llamada intentos con varios códigos introducidos.
# El programa debe:
# - Recorrer todos los intentos.
# - Mostrar cada intento realizado.
# - Si un intento está vacío, debe entrar en una condición donde se use pass como marcador.
# - Si un intento coincide con el código correcto, mostrar Acceso concedido y terminar el bucle.
# - Si después de todos los intentos no se encuentra el código correcto, mostrar Acceso denegado.
# Condición: Debe utilizar listas, for, if, elif, else, break, pass, una variable booleana y un condicional final.

print("")
print("Solución del ejercicio 10")

codigoCorrecto = "1234"
intentos = ["0000", "1111", "", "1234", "9999"]
accesoConcedido = False

for intento in intentos:
    print("Intento:", intento)
    if intento == "":
        #pass es un marcador de posición que indica que no se realiza ninguna acción en este caso.
        pass
    elif intento == codigoCorrecto:
        print("Acceso concedido")
        accesoConcedido = True
        break

    else:
        print("Código incorrecto")

if accesoConcedido == False:
    print("Acceso denegado")









    