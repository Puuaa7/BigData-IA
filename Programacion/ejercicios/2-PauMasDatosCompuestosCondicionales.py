# Ejercicio 1. Listas: control de notas
# Crear una lista con las notas, guardar la primera y la ultima.
# cambiar una nota, añadir otra y mirar cuantas hay en total.
print("")
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
print("")
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
print("")
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
print("")
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

print("")
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



#Ejercicio 6. if, elif y else: clasificación de matrícula 
# Mirar la nota del alumno y decidir si esta admitido.
# si tiene beca o si hay que revisar la solicitud.

print("")
print("Solución del ejercicio 6")

notaMedia= 6
rentaBaja= True
familiaNumerosa= False
mensaje= ""

#if, elif y else se utilizan para evaluar varias condiciones y ejecutar el bloque de código correspondiente
if notaMedia < 5:
    mensaje= "No admitido"
elif notaMedia >= 9:
    mensaje= "Beca completa"
elif notaMedia >= 7 and (rentaBaja or familiaNumerosa):
    mensaje= "Beca Parcial"
elif notaMedia >= 5:
    mensaje= "Admitido sin beca"
else:
    mensaje= "Revisar solicitud"

print(mensaje)


#Ejercicio 7. Ternaria: mensaje de resultado 
# Mirar la nota del alumno y decidir si está admitido.
# si tiene beca o si hay que revisar la solicitud.

print("")
print("Solución del ejercicio 7")

nota= 4

#la expresión condicional se evalúa primero, si es True se devuelve el primer valor, si es False se devuelve el segundo valor
#ternaria: variable = valor_si_verdadero if condicion else valor_si_falso
texto= "Aprobado" if nota >= 5 else "Suspenso"
tipoNota= "Alta" if nota >= 8 else "Media" if nota >= 5 else ""

print(nota)
print(texto)
print(tipoNota)



#Ejercicio 8. match-case: menú de aplicación 
# Mirar qué opción se ha elegido y mostrar un mensaje diferente para cada caso.

print("")
print("Solución del ejercicio 8")

opcion= "crear"
mensaje= ""

#match-case es una estructura de control que permite evaluar una variable y ejecutar un bloque de código según el valor de esa variable
match opcion:
    case "crear":
        mensaje= "Creando registro"
    case "editar":
        mensaje= "Editando registro"
    case "borrar":
        mensaje= "Borrando registro"
    case "listar":
        mensaje= "mostrando registros"
    case _:
        mensaje= "opción no reconocida"

print(mensaje)



# Ejercicio 9. Caso completo: pedido online
# Crear un pedido con productos, precios y datos de un cliente.
# aplicar descuento si toca y comprobar si tiene saldo suficiente.

print("")
print("Solución del ejercicio 9")

#lista de productos y precios
productos = ["xboxOne", "ps3", "switch"]
precios = [250, 150, 300]

#datos del cliente
cliente = {
    "nombre": "Lluis",
    "esSocio": True,
    "saldo": 450
}

#cupones válidos para aplicar descuento
cuponesValidos= {"DESC10", "OFERTA20", "CLIENTESVIP"}
cuponusado= "DESC10"

#calcular el total del pedido
total= sum(precios)

#comprobar si el cliente tiene descuento por ser socio o por usar un cupón válido
tieneDescuento= cliente["esSocio"] or cuponusado in cuponesValidos

#aplicar descuento del 10% si tiene descuento
if tieneDescuento:
    totalFinal= total * 0.90
else:
    totalFinal= total

#comprobar si el cliente tiene saldo suficiente para pagar el pedido
if cliente["saldo"] >= totalFinal:
    mensaje= "Pedido aceptado"
else:
    mensaje= "Saldo insuficiente"

print("cliente:", cliente["nombre"])
print("productos:", productos)
print("totalfinal:", totalFinal)
print("mensaje:", mensaje)


# Ejercicio 10. Caso completo: evaluación de acceso
# Comprobar si un candidato puede entrar a un curso según su edad, nota y permiso.

print("")
print("Solución del ejercicio 10")

requisitos= (18, 6, True)

candidato= {
    "nombre": "Pau",
    "edad": 24,
    "nota": 7,
    "permiso": True
}

cursosDisponibles = {"IA", "BigData", "Ciberseguridad"}

cursoElegido= "BigData"

#comprobar si el curso elegido está en la lista de cursos disponibles con el operador in que devuelve True o False
cursoExiste= cursoElegido in cursosDisponibles

#comprobar si el candidato cumple los requisitos de edad y nota
cumpleEdad= candidato["edad"] >= requisitos[0]
cumpleNota= candidato["nota"] >= requisitos[1]

#comprobar si el candidato cumple el requisito de permiso, si no se requiere permiso se considera que cumple
if requisitos[2]:
    cumplePermiso= candidato["permiso"]
else:
    cumplePermiso= True

#evaluar las condiciones y asignar un mensaje según el resultado
if cursoExiste == False:
    mensaje= "Curso no disponible"

elif cumpleEdad and cumpleNota and cumplePermiso:
    mensaje= "Acceso permitido"

elif cumpleEdad == False or cumpleNota == False or cumplePermiso == False:
    mensaje= "No cumple requisitos"

else:
    mensaje= "Solicitud incompleta"

#la expresión condicional se evalúa primero, si es True se devuelve el primer valor, si es False se devuelve el segundo valor
estado= "apto" if mensaje == "Acceso permitido" else "no apto"

#mostrar resultados
print("nombre:", candidato["nombre"])
print("curso", cursoElegido)
print("estado:", estado)
print("mensaje:", mensaje)











