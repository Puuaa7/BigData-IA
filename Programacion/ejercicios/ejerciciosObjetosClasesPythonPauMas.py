#Ejercicio 1. Crear una clase y sus objetos
#Define la clase Coche. Dentro de ella, escribe un __init__ que reciba la marca y el modelo y los
#guarde como atributos de cada objeto.
#Una vez definida la clase, fuera de ella:
#- Crea dos objetos que representen coches distintos.
#- Muestra la marca y el modelo de cada uno.
#- Cambia el modelo del primer coche y comprueba que el segundo conserva el suyo.

print("Ejercicio 1")
print("")

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


coche1 = Coche("Seat", "Coruña")
coche2 = Coche("Lancia", "Stratos HF")

print("Coche 1:", coche1.marca, coche1.modelo)
print("Coche 2:", coche2.marca, coche2.modelo)

coche1.modelo = "Leon"

print("Después de cambiar el modelo del coche 1:")
print("Coche 1:", coche1.marca, coche1.modelo)
print("Coche 2:", coche2.marca, coche2.modelo)


#Ejercicio 2. Modificar el estado de un objeto
#Escribe la definición completa de la clase CochePruebas. Los tres métodos siguientes deben
#quedar definidos dentro del cuerpo de la clase:
#- __init__(): crea el atributo de instancia velocidad con valor inicial 0, en km/h.
#- acelerar(): aumenta en 10 la velocidad del propio objeto.
#- detener(): pone a cero la velocidad del propio objeto.
#Después de terminar la definición de la clase, fuera de ella, crea dos coches de pruebas. Llama a
#sus métodos para acelerarlos un número distinto de veces y detén solo uno. Comprueba que
#cada coche conserva su propia velocidad y que detener uno no cambia la del otro.

print("")
print("Ejercicio 2")
print("")

class CochePruebas:
    def __init__(self):
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += 10

    def detener(self):
        self.velocidad = 0


cochePruebas1 = CochePruebas()
cochePruebas2 = CochePruebas()

for i in range(3):
    cochePruebas1.acelerar()

for i in range(5):
    cochePruebas2.acelerar()

print("Coche de pruebas 1: ", cochePruebas1.velocidad, "km/h")
print("Coche de pruebas 2: ", cochePruebas2.velocidad, "km/h")

cochePruebas1.detener()

print("Detenemos el coche de pruebas 1:")
print("Coche de pruebas 1: ", cochePruebas1.velocidad, "km/h")
print("Coche de pruebas 2: ", cochePruebas2.velocidad, "km/h")


#Ejercicio 3. Heredar atributos y métodos
#Define una clase Vehiculo. Su inicializador debe guardar marca y modelo, y su método describir() debe devolver un texto que incluya ambos atributos.
#Define después una clase CocheElectrico que herede de Vehiculo. Dentro de ella, escribe un inicializador que reutilice el de Vehiculo mediante super() y guarde también autonomia_km.
#Utiliza describir() por herencia, sin volver a definirlo.
#Fuera de las clases, crea un coche eléctrico y comprueba que puedes consultar sus tres atributos y utilizar la descripción heredada.

print("")
print("Ejercicio 3")
print("")

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"Vehículo {self.marca} {self.modelo}."


class CocheElectrico(Vehiculo):
    def __init__(self, marca, modelo, autonomia_km):
        super().__init__(marca, modelo)
        self.autonomia_km = autonomia_km


cocheElectrico = CocheElectrico("Fisker", "Karma", 80)

print("Marca:", cocheElectrico.marca)
print("Modelo:", cocheElectrico.modelo)
print("Autonomía:", cocheElectrico.autonomia_km, "km")
print(cocheElectrico.describir())

print(isinstance(cocheElectrico, CocheElectrico))
print(isinstance(cocheElectrico, Vehiculo))


#Ejercicio 4. Sobrescribir un método heredado
#Define una clase Motor para representar motores de coches. Su inicializador debe guardar modelo y su método arrancar() debe devolver "Motor en marcha". Crea dos subclases:
#- MotorGasolina: su método arrancar() debe devolver "Motor de gasolina en marcha".
#- MotorElectrico: su método arrancar() debe devolver "Motor eléctrico en marcha".
#Ambas subclases deben utilizar el inicializador heredado de Motor, sin definir otro __init__.
#Después, crea un motor de cada tipo con modelos distintos y comprueba sus modelos y mensajes de arranque.

print("")
print("Solución del ejercicio 4")
print("")

class Motor:
    def __init__(self, modelo):
        self.modelo = modelo

    def arrancar(self):
        return "Motor en marcha"


class MotorGasolina(Motor):
    def arrancar(self):
        return "Motor de gasolina en marcha"


class MotorElectrico(Motor):
    def arrancar(self):
        return "Motor eléctrico en marcha"

motorGasolina = MotorGasolina("Ferrari F154 V8")
motorElectrico = MotorElectrico("Fórmula E Gen3")

print("Motor de gasolina:", motorGasolina.modelo)
print(motorGasolina.arrancar())
print("Motor eléctrico:", motorElectrico.modelo)
print(motorElectrico.arrancar())


#Ejercicio 5. Utilizar el polimorfismo
#Reutiliza las clases del ejercicio anterior. Escribe una función poner_en_marcha(motor) que llame al método arrancar() del objeto recibido y devuelva su resultado. Después:
#- Crea una lista con un objeto MotorGasolina y otro MotorElectrico.
#- Recorre la lista con un bucle y utiliza poner_en_marcha() para mostrar el mensaje de cada motor.
#La función debe funcionar sin comprobar el tipo del motor con type() o isinstance().
#Finalmente, añade una clase MotorDiesel que herede de Motor y cuyo método arrancar() devuelva "Motor diésel en marcha". Incorpora un motor diésel a la lista y comprueba que funciona sin modificar la función poner_en_marcha() ni el bucle.

print("")
print("Ejercicio 5")
print("")

def poner_en_marcha(motor):
    return motor.arrancar()


motores = [MotorGasolina("Ferrari F154 V8"), MotorElectrico("Fórmula E Gen3")]


print(motores[0].modelo + ":", poner_en_marcha(motores[0]))
print(motores[1].modelo + ":", poner_en_marcha(motores[1]))

class MotorDiesel(Motor):
    def arrancar(self):
        return "Motor diésel en marcha"



motores.append(MotorDiesel("Audi 6.0 V12 TDI"))

print("Después de añadir el motor diésel:")
print(motores[0].modelo + ":", poner_en_marcha(motores[0]))
print(motores[1].modelo + ":", poner_en_marcha(motores[1]))
print(motores[2].modelo + ":", poner_en_marcha(motores[2]))


#Ejercicio 6. Ampliar un método heredado con super()
#Retoma las clases del ejercicio 3. Escribe una nueva versión de CocheElectrico que conserve su inicializador y defina su propio método describir().
#Ese método debe aprovechar la descripción de Vehiculo mediante super(), añadir una frase con la autonomía en kilómetros y devolver el mensaje completo. Reutiliza la descripción original sin volver a escribirla manualmente.
#Una vez definida esta versión de la clase, crea un coche eléctrico y comprueba tanto la descripción ampliada como la conservación de sus atributos.

print("")
print("Ejercicio 6")
print("")

class CocheElectrico(Vehiculo):
    def __init__(self, marca, modelo, autonomia_km):
        super().__init__(marca, modelo)
        self.autonomia_km = autonomia_km

    def describir(self):
        descripcion = super().describir()
        return descripcion + f" Tiene una autonomía de {self.autonomia_km} km."


cocheElectrico = CocheElectrico("Tesla", "Roadster 2008", 393)

print(cocheElectrico.describir())
print("Marca:", cocheElectrico.marca)
print("Modelo:", cocheElectrico.modelo)
print("Autonomía:", cocheElectrico.autonomia_km, "km")




#Ejercicio 7. Mostrar datos con f-strings
#Utiliza estos datos:
#marca = "Seat"
#modelo = "Ibiza"
#año = 2020
#Escribe un único print() con una f-string que inserte los valores de las tres variables en una frase legible.
#Después, cambia los valores de las variables y comprueba que el mensaje se actualiza sin modificar el print(). No necesitas crear ninguna clase.

print("")
print("Ejercicio 7")
print("")

marca = "Seat"
modelo = "Ibiza"
año = 2020

print(f"El coche es un {marca} {modelo} del año {año}.")

marca = "Lancia"
modelo = "Delta HF Integrale"
año = 1992

print(f"El coche es un {marca} {modelo} del año {año}.")


#Ejercicio 8. Gestionar una entrada incorrecta con try y except
#Pide al usuario los kilómetros recorridos por un coche con input() e intenta convertirlos a un entero con int() dentro de un bloque try.
#- Si la conversión funciona, muestra "Kilómetros indicados:" seguido del número.
#- Si se produce ValueError, muestra "Debes escribir un número entero.".
#- Fuera del try / except, muestra siempre "Programa finalizado.".
#Haz dos pruebas en ejecuciones distintas: introduce primero 12000 y después doce mil. Comprueba que el programa muestra el mensaje adecuado y llega al mensaje final en ambos casos.
#Solo debes comprobar si la entrada puede convertirse a entero. No hace falta repetir la pregunta ni utilizar un bucle.

print("")
print("Ejercicio 8")
print("")

try:
    kilometros = int(input("Escribe los kilómetros recorridos por el coche: "))
    print("Kilómetros indicados:", kilometros)
except ValueError:
    print("Debes escribir un número entero.")

print("Programa finalizado.")
