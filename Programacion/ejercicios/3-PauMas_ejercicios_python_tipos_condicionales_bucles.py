

#Ejercicio 1. Control de notas
#Crea una lista llamada notas con al menos 10 calificaciones numéricas.
#El programa debe:
#- Mostrar todas las notas.
#- Calcular cuántas notas están aprobadas y cuántas suspendidas.
#- Calcular la nota media.
#- Mostrar la nota más alta y la nota más baja.
#- Indicar si la media final está aprobada o suspendida.
#Condición: Debe utilizar listas, bucle for, operadores de comparación y condicionales.


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


    