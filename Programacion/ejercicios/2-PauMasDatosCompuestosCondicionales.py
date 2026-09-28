# Ejercicio 1. Listas: control de notas
# Crear una lista con las notas, guardar la primera y la ultima.
# cambiar una nota, añadir otra y mirar cuantas hay en total.

print("Solución del ejercicio 1")

#lista de notas
notas = [6, 8, 5, 9, 7]

# Guardar la primera y la última nota
primeraNota=notas[0]
ultimaNota=notas[4]

# Cambiar la segunda nota a 10
notas[1]=10

#append() añade un elemento al final de la lista
notas.append(8)

#len() devuelve el número de elementos de la lista
totalNotas=len(notas)

# Mostrar resultados
print("Lista final:", notas)
print("Primera nota:", primeraNota)
print("Ultima nota:", ultimaNota)
print("Total de notas:", totalNotas)


# Ejercicio 2. Tuplas: datos fijos de un producto
# Crear una tupla con un producto, su precio y sus unidades.
# Despues calcular cuanto vale todo el stock.

print("Solución del ejercicio 2")

# Tupla con datos de un producto
producto=("teclado", 25.50, 12)

#asignar los valores de la tupla a variables
nombre=producto[0]
precio=producto[1]
unidades=producto[2]

# Calcular el valor total del stock
valorTotal=precio * unidades

#mostrar resultados
print("Nombre:", nombre)
print("Precio:", precio)
print("Unidades:", unidades)
print("Valor total:", valorTotal)


# Ejercicio 3. Diccionarios: ficha de alumno
# Crear un diccionario con los datos de un alumno,
# cambiar la nota y mirar si está aprobado.

print("Solución del ejercicio 3")

#crear un diccionario con los datos de un alumno
alumno = {
    "nombre":"Ana",
    "edad":16,
    "curso":"IA",
    "nota":7.5
}

#en un diccionario se accede a los valores usando la clave entre corchetes
print("Nombre:", alumno["nombre"])
print("Nota:", alumno["nota"])

# Cambiar la nota del alumno a 8
alumno["nota"]= 8

#comprobar mediante una condición si el alumno está aprobado
alumno["aprobado"]=alumno["nota"]>=5

print(alumno)


# Ejercicio 4. Conjuntos: usuarios registrados
# Crear un conjunto de usuarios y comprobar si Luis esta dentro.
# Tambien añadimos otro usuario y contamos cuántos hay.

print("Solución del ejercicio 4")

#crear conjunto de usuarios, se utiliza llaves {} y no se permiten elementos duplicados,
#en este caso "Ana" está repetido y solo se guardará una vez
usuarios = {"Ana", "Luis", "Marta", "Ana", "Pedro"}

nuevoUsuario= "Luis"

#comprobar si el nuevo usuario ya existe en el conjunto, con el operador in que devuelve True o False
usuarioExiste= nuevoUsuario in usuarios

#añadir un nuevo usuario al conjunto, se utiliza el método add()
usuarios.add("Clara")

#len() devuelve el número de elementos del conjunto, igual que en las listas y tuplas
totalUsuarios= len(usuarios)

print("Usuarios:", usuarios)
print("Usuario existe:", usuarioExiste)
print("Total usuarios:", totalUsuarios)


# Ejercicio 5. Condiciones con and, or y not
# Comprobar si una persona puede acceder por edad o por ser socio.

print("Solución del ejercicio 5")

edad= 17
tienePermiso= True
esSocio= False
sancionado = False

#aqui usamos and asi que ambas condiciones deben ser True para que la variable accesoPorEdad sea True
accesoPorEdad = edad >= 16 and tienePermiso

#aqui al usar and not, la variable accesoPorSocio será True si esSocio es True y sancionado es False
accesoPorSocio = esSocio and not sancionado

#aqui con el or la variable puedeAcceder será True si al menos una de las condiciones es True
puedeAcceder = accesoPorEdad or accesoPorSocio

print("Acceso por edad:", accesoPorEdad)
print("Acceso por socio:", accesoPorSocio)
print("Puede acceder:", puedeAcceder)