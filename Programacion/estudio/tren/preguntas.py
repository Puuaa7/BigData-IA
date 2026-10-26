"""
Banco de preguntas de la app "Python en el tren".

Ejecuta este archivo para:
  1. Comprobar cada pregunta ejecutando su código (si alguna respuesta está mal, avisa).
  2. Generar tren.html a partir de plantilla.html.

Tipos de pregunta:
  out  -> "¿Qué imprime?"  La opción correcta debe ser exactamente la salida del código.
  err  -> "¿Qué error da?" La opción correcta es el nombre de la excepción (o "Ningún error").
  fill -> "Completa el hueco ___". Con la opción correcta el código imprime `expect`;
          con las demás no.
  mc   -> Teoría. No se ejecuta.
"""

import contextlib
import io
import json
import pathlib
import sys

EXAMENES = []


def examen(id, titulo, tema):
    EXAMENES.append({"id": id, "titulo": titulo, "tema": tema, "preguntas": []})


def q(t, code="", opts=(), a=0, exp="", q="", expect=None, por=None):
    """por: {opción_incorrecta: "por qué está mal"}. Se muestra al fallar."""
    ex = EXAMENES[-1]
    ex["preguntas"].append({
        "id": f"{ex['id']}-{len(ex['preguntas']) + 1}",
        "t": t,
        "q": q,
        "code": code.strip("\n"),
        "opts": list(opts),
        "a": a,
        "exp": exp,
        "expect": expect,
        "por": dict(por or {}),
    })


# ---------------------------------------------------------------------
examen("tipos", "Tipos y operadores", "Tema 1")
# ---------------------------------------------------------------------
q("out", "print(7 // 2, 7 % 2)", ["3 1", "3.5 1", "3 1.0", "4 1"], 0,
  "// es división entera (3) y % es el resto (1).")
q("out", "print(10 / 2)", ["5.0", "5", "5.00", "Error"], 0,
  "/ siempre devuelve float, aunque la división sea exacta.")
q("out", "print(17 % 5, 2 ** 4)", ["2 16", "3 16", "2 8", "3.4 16"], 0,
  "17 entre 5 cabe 3 veces y sobran 2. 2 ** 4 = 16.")
q("out", 'x = "3"\nprint(x * 3)', ["333", "9", "3 3 3", "Error"], 0,
  "Un str multiplicado por un int repite el texto.")
q("err", 'print("Edad: " + 20)', ["TypeError", "SyntaxError", "NameError", "Ningún error"], 0,
  'No se puede sumar str + int. Usa str(20), comas en print o un f-string.')
q("out", "print(type(6 / 3))", ["<class 'float'>", "<class 'int'>", "2.0", "<class 'str'>"], 0,
  "6 / 3 da 2.0, que es float.")
q("out", "a = 5\na += 3\na *= 2\nprint(a)", ["16", "13", "10", "11"], 0,
  "a pasa a 8 y luego a 16.")
q("out", "print(5 > 3 and 2 > 4, not False)", ["False True", "True True", "True False", "False False"], 0,
  "and necesita que las dos sean True; 2 > 4 es False. not False es True.")
q("mc", q="¿Qué representa None en Python?",
  opts=["La ausencia de valor", "El número 0", "Un texto vacío", "El valor False"], a=0,
  exp="0, \"\" y False son valores. None significa que no hay valor.")
q("out", 'print(int("7") + 3, str(7) + "3")', ["10 73", "73 10", "10 10", "73 73"], 0,
  'int("7") + 3 es una suma de números (10). str(7) + "3" une textos ("73").')

# ---------------------------------------------------------------------
examen("compuestos", "Listas, tuplas, dicts y sets", "Tema 2")
# ---------------------------------------------------------------------
q("out", "l = [4, 8, 15, 16]\nprint(l[1], l[-1])", ["8 16", "4 16", "8 15", "4 15"], 0,
  "El índice empieza en 0, así que l[1] es 8. l[-1] es el último.")
q("out", "l = [1, 2, 3]\nl.append([4, 5])\nprint(len(l))", ["4", "5", "3", "Error"], 0,
  "append añade UN elemento: la lista [4, 5] entera cuenta como uno.")
q("err", "t = (1, 2)\nt[0] = 5", ["TypeError", "IndexError", "KeyError", "Ningún error"], 0,
  "Las tuplas son inmutables: no se pueden modificar.")
q("out", 'd = {"a": 1, "b": 2}\nd["c"] = 3\nd["a"] = 0\nprint(d)',
  ["{'a': 0, 'b': 2, 'c': 3}", "{'a': 1, 'b': 2, 'c': 3}", "{'b': 2, 'c': 3, 'a': 0}", "Error"], 0,
  "Si la clave existe se modifica; si no existe, se añade al final.")
q("err", 'd = {"nombre": "Ana"}\nprint(d["edad"])', ["KeyError", "IndexError", "TypeError", "Ningún error"], 0,
  "Acceder a una clave que no existe da KeyError.")
q("out", "s = {3, 1, 3, 2, 1}\nprint(len(s))", ["3", "5", "2", "4"], 0,
  "Un set no guarda duplicados: quedan 1, 2 y 3.")
q("out", "l = [10, 20, 30, 40, 50]\nprint(l[1:3])", ["[20, 30]", "[20, 30, 40]", "[10, 20, 30]", "[30, 40]"], 0,
  "Desde el índice 1 hasta ANTES del 3.")
q("mc", q="Quieres guardar las coordenadas (x, y) de un punto que no van a cambiar. ¿Qué usas?",
  opts=["Una tupla", "Una lista", "Un set", "Un diccionario"], a=0,
  exp="Valores fijos que van juntos: tupla.")
q("out", 'print("Ana" in {"nombre": "Ana"})', ["False", "True", "Error", "None"], 0,
  "in en un diccionario mira las CLAVES, no los valores. \"Ana\" es un valor.")
q("out", "a = [1, 2]\nb = a\nb.append(3)\nprint(a)", ["[1, 2, 3]", "[1, 2]", "[3]", "Error"], 0,
  "b = a no copia: los dos nombres apuntan a la misma lista. Para copiar usa a.copy().")

# ---------------------------------------------------------------------
examen("condicionales", "Condicionales", "Tema 2")
# ---------------------------------------------------------------------
q("out", 'nota = 6\nif nota >= 5:\n    print("A")\nelif nota >= 6:\n    print("B")\nelse:\n    print("C")',
  ["A", "B", "A\nB", "C"], 0,
  "Solo se ejecuta el primer bloque que es True. El elif ya no se mira.")
q("out", 'edad = 17\npermiso = True\nprint("Entra" if edad >= 18 or permiso else "No")',
  ["Entra", "No", "True", "Error"], 0,
  "Con or basta con que una sea True, y permiso es True.")
q("err", 'x = 5\nif x = 5:\n    print("cinco")', ["SyntaxError", "TypeError", "NameError", "Ningún error"], 0,
  "Para comparar se usa ==. Un solo = asigna.")
q("out", 't = 30\nif t < 10:\n    print("Frío")\nelif t < 25:\n    print("Agradable")\nelse:\n    print("Calor")',
  ["Calor", "Agradable", "Frío", "Agradable\nCalor"], 0,
  "30 no es < 10 ni < 25, así que entra en el else.")
q("out", 'x = 0\nif x:\n    print("Sí")\nelse:\n    print("No")', ["No", "Sí", "0", "Error"], 0,
  "0 cuenta como False en un if (igual que \"\", [] y None).")
q("out", 'dia = "sábado"\nmatch dia:\n    case "lunes":\n        print("Inicio")\n    case "viernes":\n        print("Casi")\n    case _:\n        print("Otro")',
  ["Otro", "Inicio", "Casi", "Nada"], 0,
  "case _ es el caso por defecto cuando no coincide ninguno.")
q("out", 'n = -3\nprint("pos" if n > 0 else "neg" if n < 0 else "cero")', ["neg", "pos", "cero", "Error"], 0,
  "Ternario encadenado: no es > 0, sí es < 0.")
q("fill", 'nota = 7.5\nif nota ___ 5:\n    print("Aprobado")', ['>=', '=>', '=', '=<'], 0,
  "Los operadores son >= y <=, con el = siempre detrás.", expect="Aprobado")
q("out", "a = True\nb = False\nprint(a and not b, a or b, not a)",
  ["True True False", "False True False", "True False False", "True True True"], 0,
  "not b es True, así que a and True da True. a or b da True. not a da False.")
q("out", 'edad = 20\nentrada = False\nif edad >= 18:\n    if entrada:\n        print("Pasa")\n    else:\n        print("Sin entrada")\nelse:\n    print("Menor")',
  ["Sin entrada", "Pasa", "Menor", "Pasa\nSin entrada"], 0,
  "Entra en el primer if (20 >= 18) y dentro, como entrada es False, va al else interior.")

# ---------------------------------------------------------------------
examen("bucles", "Bucles y range", "Tema 3")
# ---------------------------------------------------------------------
q("out", "print(list(range(1, 10, 3)))", ["[1, 4, 7]", "[1, 4, 7, 10]", "[3, 6, 9]", "[1, 3, 6, 9]"], 0,
  "Empieza en 1 y va de 3 en 3 sin llegar a 10.")
q("out", "print(list(range(5, 0, -2)))", ["[5, 3, 1]", "[5, 3, 1, 0]", "[5, 3]", "[]"], 0,
  "Paso negativo: cuenta hacia atrás. El 0 no se incluye.")
q("out", "total = 0\nfor i in range(1, 5):\n    total += i\nprint(total)", ["10", "15", "4", "6"], 0,
  "1 + 2 + 3 + 4 = 10. El 5 no entra.")
q("out", "i = 10\nwhile i > 0:\n    i -= 3\nprint(i)", ["-2", "1", "0", "-3"], 0,
  "10, 7, 4, 1, -2. Cuando vale -2 la condición es False y sale.")
q("out", "for n in [1, 2, 3, 4, 5]:\n    if n == 3:\n        continue\n    if n == 5:\n        break\n    print(n)",
  ["1\n2\n4", "1\n2", "1\n2\n4\n5", "1\n2\n3\n4"], 0,
  "continue se salta el 3, break para en el 5 antes de imprimirlo.")
q("out", 'for i, c in enumerate("ab", start=1):\n    print(i, c)', ["1 a\n2 b", "0 a\n1 b", "a 1\nb 2", "1 ab"], 0,
  "enumerate da (posición, valor). Con start=1 empieza en 1.")
q("out", "for x, y in zip([1, 2, 3], [10, 20]):\n    print(x + y)", ["11\n22", "11\n22\n3", "11\n22\n33", "Error"], 0,
  "zip para cuando se acaba la lista más corta.")
q("out", 'for n in [2, 4, 6]:\n    if n % 2 == 1:\n        print("impar")\n        break\nelse:\n    print("todos pares")',
  ["todos pares", "impar", "Nada", "impar\ntodos pares"], 0,
  "El else de un for se ejecuta si el bucle acabó sin break.")
q("out", 'd = {"a": 1, "b": 2}\nfor k in d:\n    print(k)', ["a\nb", "1\n2", "a 1\nb 2", "('a', 1)\n('b', 2)"], 0,
  "Recorrer un diccionario directamente da sus claves.")
q("out", "c = 0\nfor f in range(3):\n    for col in range(2):\n        c += 1\nprint(c)", ["6", "5", "3", "2"], 0,
  "Bucle anidado: 3 vueltas fuera × 2 dentro = 6.")
q("out", "print([x * 2 for x in range(4) if x % 2 == 0])", ["[0, 4]", "[0, 2, 4, 6]", "[2, 6]", "[4]"], 0,
  "Los pares de range(4) son 0 y 2. Por 2 da 0 y 4.")

# ---------------------------------------------------------------------
examen("funciones1", "Funciones: return y parámetros", "Tema 4")
# ---------------------------------------------------------------------
q("out", "def f(x):\n    x * 2\n\nprint(f(4))", ["None", "8", "4", "Error"], 0,
  "Calcula x * 2 pero no lo devuelve. Sin return la función devuelve None.")
q("out", 'def saludo(n="mundo"):\n    return "Hola " + n\n\nprint(saludo(), saludo("Pau"))',
  ["Hola mundo Hola Pau", "Hola Pau Hola Pau", "Hola mundo Hola mundo", "Error"], 0,
  "Si no pasas argumento usa el valor por defecto.")
q("err", "def f(a=1, b):\n    return a + b", ["SyntaxError", "TypeError", "NameError", "Ningún error"], 0,
  "Los parámetros con valor por defecto van después de los obligatorios.")
q("out", "def f(a, b):\n    return a - b\n\nprint(f(b=10, a=3))", ["-7", "7", "Error", "13"], 0,
  "Con argumentos por nombre el orden no importa: a=3, b=10.")
q("out", "def f():\n    return 1\n    print(2)\n\nprint(f())", ["1", "2", "1\n2", "None"], 0,
  "return termina la función. El print(2) no se ejecuta nunca.")
q("out", "def mm(l):\n    return min(l), max(l)\n\nx = mm([4, 9, 2])\nprint(x)", ["(2, 9)", "[2, 9]", "2 9", "2"], 0,
  "return a, b devuelve una tupla.")
q("out", "x = 5\ndef g():\n    x = 1\n    return x\n\nprint(g(), x)", ["1 5", "1 1", "5 5", "5 1"], 0,
  "La x de dentro de g es local y no cambia la de fuera.")
q("err", "def total(l):\n    s = 0\n    for n in l:\n        s += n\n    print(s)\n\nr = total([1, 2]) + 1",
  ["TypeError", "NameError", "SyntaxError", "Ningún error"], 0,
  "total hace print pero no return, así que devuelve None, y None + 1 da error.")
q("mc", q='En def saludar(nombre): ... y la llamada saludar("Ana"), ¿qué es "Ana"?',
  opts=["Un argumento", "Un parámetro", "Una variable global", "Un return"], a=0,
  exp="El parámetro es el nombre de la definición (nombre). El argumento es el valor que pasas (\"Ana\").")
q("fill", "def doble(n):\n    ___ n * 2\n\nprint(doble(4))", ["return", "print", "def", "yield"], 0,
  "Para que la función entregue el resultado hace falta return.", expect="8")

# ---------------------------------------------------------------------
examen("funciones2", "Lambda, map, filter y recursión", "Tema 4")
# ---------------------------------------------------------------------
q("out", "def s(*n):\n    return len(n)\n\nprint(s(1, 2, 3))", ["3", "1", "6", "Error"], 0,
  "*n agrupa todos los argumentos en una tupla de 3 elementos.")
q("out", "def f(*a):\n    print(type(a))\n\nf(1)", ["<class 'tuple'>", "<class 'list'>", "<class 'int'>", "<class 'dict'>"], 0,
  "*args siempre es una tupla.")
q("out", "def f(**k):\n    print(k)\n\nf(x=1, y=2)", ["{'x': 1, 'y': 2}", "(1, 2)", "[1, 2]", "x y"], 0,
  "**kwargs es un diccionario con los argumentos por nombre.")
q("out", "sq = lambda x: x * x\nprint(sq(5))", ["25", "10", "5", "Error"], 0,
  "La lambda devuelve x * x automáticamente.")
q("out", "print(list(map(lambda x: x + 1, [1, 2, 3])))", ["[2, 3, 4]", "[1, 2, 3]", "[2]", "9"], 0,
  "map aplica la función a cada elemento.")
q("out", "print(list(filter(lambda x: x > 2, [1, 5, 2, 8])))", ["[5, 8]", "[True, True]", "[1, 2]", "[False, True, False, True]"], 0,
  "filter se queda con los elementos para los que la función da True.")
q("out", 'ps = [{"n": "A", "e": 30}, {"n": "B", "e": 20}]\nprint(sorted(ps, key=lambda p: p["e"])[0]["n"])',
  ["B", "A", "20", "Error"], 0,
  "Ordena por edad de menor a mayor: B (20) va primero.")
q("out", "def fact(n):\n    if n == 0:\n        return 1\n    return n * fact(n - 1)\n\nprint(fact(3))", ["6", "3", "0", "9"], 0,
  "3 * 2 * 1 * 1 = 6. El caso base es n == 0.")
q("mc", q="¿Qué pasa si una función recursiva no tiene caso base?",
  opts=["Se llama sin parar hasta dar RecursionError", "Devuelve None", "Devuelve 0", "Python la convierte en bucle"], a=0,
  exp="Sin caso base nunca para, y Python corta con RecursionError.")
q("out", "l = [3, 1, 2]\nr = l.sort()\nprint(r)", ["None", "[1, 2, 3]", "[3, 1, 2]", "Error"], 0,
  "l.sort() ordena la lista original y devuelve None. sorted(l) sí devuelve una lista nueva.")
q("out", 'print(max(["pera", "kiwi", "plátano"], key=lambda s: len(s)))', ["plátano", "pera", "kiwi", "7"], 0,
  "key indica qué se compara: la longitud. El más largo es plátano.")

# ---------------------------------------------------------------------
examen("estadistica", "Estadística y ordenación", "ML (solo Python)")
# ---------------------------------------------------------------------
q("out", "l = [2, 4, 9]\nprint(sum(l) / len(l))", ["5.0", "5", "15", "3"], 0,
  "Media = suma / cantidad = 15 / 3. La división / da float.")
q("out", "o = sorted([7, 1, 3, 9])\nn = len(o)\nprint((o[n // 2 - 1] + o[n // 2]) / 2)", ["5.0", "3", "7", "5"], 0,
  "Ordenada: [1, 3, 7, 9]. Como n es par, la mediana es la media de 3 y 7.")
q("mc", q="La varianza POBLACIONAL divide la suma de cuadrados entre…",
  opts=["n", "n - 1", "n + 1", "la media"], a=0,
  exp="Poblacional: entre n. Muestral: entre n - 1 (es lo que hace pandas .var() por defecto).")
q("out", "l = [1, 2, 2, 3, 3, 3]\nprint(max(set(l), key=l.count))", ["3", "2", "6", "1"], 0,
  "El valor que más se repite (la moda) es 3, que aparece 3 veces.")
q("out", 'l = ["a", "b", "a"]\nf = {}\nfor x in l:\n    if x in f:\n        f[x] += 1\n    else:\n        f[x] = 1\nprint(f)',
  ["{'a': 2, 'b': 1}", "{'a': 1, 'b': 1}", "{'b': 1, 'a': 2}", "['a', 'b']"], 0,
  "Patrón de frecuencias: si la clave existe suma 1, si no la crea con 1.")
q("out", "o = [3, 2, 1]\nfor j in range(2):\n    if o[j] > o[j + 1]:\n        o[j], o[j + 1] = o[j + 1], o[j]\nprint(o)",
  ["[2, 1, 3]", "[1, 2, 3]", "[3, 2, 1]", "[2, 3, 1]"], 0,
  "Una sola pasada de burbuja: el mayor (3) acaba al final, pero el resto todavía no está ordenado.")
q("mc", q="¿Qué método de ordenación compara siempre elementos VECINOS (j y j+1)?",
  opts=["Burbuja", "Selección", "Intercambio directo", "Ninguno"], a=0,
  exp="Burbuja compara vecinos. Selección busca el mínimo y hace un intercambio por pasada.")
q("out", "l = [10, 20, 30]\nmn, mx = min(l), max(l)\nprint([(x - mn) / (mx - mn) for x in l])",
  ["[0.0, 0.5, 1.0]", "[0, 1, 2]", "[10, 20, 30]", "[0.1, 0.2, 0.3]"], 0,
  "Min-max deja el mínimo en 0, el máximo en 1 y el resto entre medias.")
q("mc", q="Un alumno tiene un z-score de -1.5. ¿Qué significa?",
  opts=["Está 1.5 desviaciones típicas por debajo de la media", "Ha sacado -1.5 puntos",
        "Está 1.5 puntos por debajo de la media", "Está por encima de la media"], a=0,
  exp="z = (x - media) / desviación. Negativo es por debajo; el número son desviaciones típicas.")
q("out", "mayor = 0\nfor n in [-4, -2, -7]:\n    if n > mayor:\n        mayor = n\nprint(mayor)", ["0", "-2", "-7", "-4"], 0,
  "Trampa clásica: ningún número supera el 0 inicial. Hay que empezar con mayor = l[0].")
q("mc", q="¿Qué diferencia hay entre sorted(l) y l.sort()?",
  opts=["sorted devuelve una lista nueva; sort cambia l y devuelve None", "Ninguna",
        "sort devuelve una lista nueva; sorted cambia l", "sorted solo funciona con números"], a=0,
  exp="Si necesitas conservar la original, usa sorted o haz una copia.")

# ---------------------------------------------------------------------
examen("errores", "¿Qué error da?", "Todos")
# ---------------------------------------------------------------------
q("err", "l = [1, 2, 3]\nprint(l[3])", ["IndexError", "KeyError", "TypeError", "Ningún error"], 0,
  "Una lista de 3 elementos tiene los índices 0, 1 y 2.")
q("err", "print(10 / 0)", ["ZeroDivisionError", "TypeError", "SyntaxError", "Ningún error"], 0,
  "No se puede dividir entre 0.")
q("err", 'd = {}\nd["x"] += 1', ["KeyError", "TypeError", "IndexError", "Ningún error"], 0,
  "d[\"x\"] += 1 primero lee d[\"x\"], que no existe. Por eso en frecuencias se comprueba antes con in.")
q("err", "def f():\n    return f()\n\nf()", ["RecursionError", "SyntaxError", "TypeError", "Ningún error"], 0,
  "Se llama a sí misma sin caso base.")
q("err", "for x in [1, 2]\n    print(x)", ["SyntaxError", "IndentationError", "TypeError", "Ningún error"], 0,
  "Falta el : al final del for.")
q("err", 'if True:\nprint("hola")', ["IndentationError", "SyntaxError", "NameError", "Ningún error"], 0,
  "El cuerpo del if tiene que ir indentado.")
q("err", "def f():\n    pass\n\nprint(f() + 1)", ["TypeError", "NameError", "ZeroDivisionError", "Ningún error"], 0,
  "f() devuelve None, y None + 1 da error.")
q("err", "l = [1, 2, 3]\nprint(l[-1])", ["Ningún error", "IndexError", "KeyError", "TypeError"], 0,
  "Los índices negativos sí existen: l[-1] es el último (3).")
q("err", "edad = 20\nprint(Edad)", ["NameError", "KeyError", "SyntaxError", "Ningún error"], 0,
  "Python distingue mayúsculas: Edad no existe.")
q("err", 'alumno = {"nombre": "Ana"}\nprint(alumno[0])', ["KeyError", "IndexError", "TypeError", "Ningún error"], 0,
  "Los diccionarios no se acceden por posición: busca la CLAVE 0, que no existe.")

# ---------------------------------------------------------------------
examen("simulacro", "Simulacro: completa el código", "Todos")
# ---------------------------------------------------------------------
q("fill", "aprobados = 0\nfor n in [4, 6, 8]:\n    if n >= 5:\n        aprobados ___ 1\nprint(aprobados)",
  ["+=", "=", "==", "=+"], 0, "Contador: se suma 1 con +=.", expect="2")
q("fill", "for i ___ range(3):\n    print(i)", ["in", "of", "=", ":"], 0,
  "La sintaxis es for variable in iterable:", expect="0\n1\n2")
q("fill", 'd = {"a": 1, "b": 2}\nfor k, v in d.___():\n    print(k, v)', ["items", "keys", "values", "get"], 0,
  "items() da parejas (clave, valor) para desempaquetar en k, v.", expect="a 1\nb 2")
q("fill", "nums = [3, 7, 9, 7]\nfor i, x in enumerate(nums):\n    if x == 7:\n        print(i)\n        ___",
  ["break", "continue", "pass", "return"], 0,
  "break para el bucle en el primer 7. Con continue o pass seguiría y también imprimiría el 3.", expect="1")
q("fill", "def media(l):\n    return ___(l) / len(l)\n\nprint(media([2, 4]))", ["sum", "max", "min", "len"], 0,
  "Media = suma / cantidad.", expect="3.0")
q("fill", "print(list(range(___)))", ["2, 9, 2", "2, 8, 2", "0, 8, 2", "2, 10"], 0,
  "El final no se incluye, así que para llegar a 8 el fin tiene que ser 9 (o 10).", expect="[2, 4, 6, 8]")
q("fill", "l = [-3, -9, -4]\nmayor = ___\nfor x in l:\n    if x > mayor:\n        mayor = x\nprint(mayor)",
  ["l[0]", "0", "len(l)", "None"], 0,
  "El máximo se empieza con un elemento de la lista. Con 0 fallaría si todos son negativos.", expect="-3")
q("fill", "def f(___):\n    t = 0\n    for n in nums:\n        t += n\n    return t\n\nprint(f(1, 2, 3))",
  ["*nums", "nums", "**nums", "[nums]"], 0,
  "*nums recoge cualquier número de argumentos en una tupla.", expect="6")
q("fill", 'ps = [{"n": "Ana", "edad": 30}, {"n": "Luis", "edad": 19}]\nfor p in sorted(ps, key=___):\n    print(p["n"])',
  ['lambda p: p["edad"]', 'p["edad"]', 'lambda: p["edad"]', '"edad"'], 0,
  "key necesita una función que reciba cada elemento y devuelva por qué ordenar.", expect="Luis\nAna")
q("fill", "o = sorted([5, 1, 4])\nprint(o[___])", ["len(o) // 2", "len(o) / 2", "len(o)", "1.5"], 0,
  "Los índices deben ser int: // da entero. Con n impar el centro es o[n // 2].", expect="4")


# =====================================================================
# Sacados de tus ejercicios (2-DatosCompuestosCondicionales, 3-bucles, ML 3)
# =====================================================================

# ---------------------------------------------------------------------
examen("practica2", "Tu práctica 2: datos y condiciones", "Ejercicios 2")
# ---------------------------------------------------------------------
q("out", "notas = [6, 8, 5, 9, 7]\nnotas[1] = 10\nnotas.append(8)\nprint(notas[0], notas[-1], len(notas))",
  ["6 8 6", "6 7 6", "6 8 5", "10 8 6"], 0,
  "notas[1] cambia la segunda nota; append añade 8 al final, así que hay 6 notas y la última es 8.",
  por={"6 7 6": "append añade el 8 al final, así que el último ya no es el 7.",
       "6 8 5": "append aumenta la longitud: de 5 pasa a 6.",
       "10 8 6": "notas[1] es la SEGUNDA nota. La primera, notas[0], sigue siendo 6."})
q("out", 'producto = ("teclado", 25.5, 12)\nnombre, precio, unidades = producto\nprint(precio * unidades)',
  ["306.0", "306", "Error", "37.5"], 0,
  "Se desempaqueta la tupla en tres variables y se calcula el valor del stock: 25.5 × 12.",
  por={"306": "float × int da float: 306.0.",
       "Error": "Desempaquetar funciona si hay tantas variables como elementos (3 y 3).",
       "37.5": "Eso sería sumar precio + unidades. Aquí se multiplica."})
q("out", 'alumno = {"nombre": "Ana", "nota": 7.5}\nalumno["nota"] = 4\nalumno["aprobado"] = alumno["nota"] >= 5\nprint(alumno["aprobado"], len(alumno))',
  ["False 3", "True 3", "False 2", "True 2"], 0,
  "La nota se cambia a 4 ANTES de comparar, y asignar una clave nueva la añade.",
  por={"True 3": "La nota se cambió a 4 antes de comparar: 4 >= 5 es False.",
       "False 2": 'Asignar alumno["aprobado"] crea una clave nueva: ahora hay 3.',
       "True 2": "Dos fallos: la nota ya es 4 (False) y hay una clave nueva (3)."})
q("out", 'usuarios = {"Ana", "Luis", "Ana", "Pedro"}\nusuarios.add("Clara")\nusuarios.add("Luis")\nprint(len(usuarios))',
  ["4", "6", "5", "3"], 0,
  "El set empieza con Ana, Luis y Pedro (3). Clara suma 1. Luis ya estaba.",
  por={"6": "Un set no guarda duplicados: la segunda Ana y el segundo Luis no cuentan.",
       "5": "Luis ya estaba en el set; add no lo vuelve a meter.",
       "3": "Clara es nueva, así que sí se añade."})
q("out", "edad = 17\ntiene_permiso = True\nes_socio = True\nsancionado = True\nacceso_edad = edad >= 16 and tiene_permiso\nacceso_socio = es_socio and not sancionado\nprint(acceso_edad, acceso_socio, acceso_edad or acceso_socio)",
  ["True False True", "True True True", "False False False", "True False False"], 0,
  "Como en tu ejercicio 5: and pide las dos, not invierte y or pide al menos una.",
  por={"True True True": "not sancionado es False, así que es_socio and False da False.",
       "False False False": "17 >= 16 es True y tiene permiso: acceso_edad es True.",
       "True False False": "or da True si al menos una es True, y acceso_edad lo es."})
q("out", 'nota_media = 8\nrenta_baja = False\nfamilia_numerosa = True\nif nota_media < 5:\n    print("No admitido")\nelif nota_media >= 9:\n    print("Beca completa")\nelif nota_media >= 7 and (renta_baja or familia_numerosa):\n    print("Beca parcial")\nelif nota_media >= 5:\n    print("Admitido sin beca")',
  ["Beca parcial", "Admitido sin beca", "Beca completa", "No admitido"], 0,
  "8 >= 7 y (False or True) es True. Es el primer bloque True, así que no se mira el siguiente.",
  por={"Admitido sin beca": "8 >= 5 también es True, pero el elif de la beca parcial va antes y ya se cumplió.",
       "Beca completa": "8 >= 9 es False.",
       "No admitido": "8 < 5 es False."})
q("out", 'nota = 6\ntipo = "Alta" if nota >= 8 else "Media" if nota >= 5 else "Baja"\nprint(tipo)',
  ["Media", "Alta", "Baja", "Error"], 0,
  "Ternario encadenado de tu ejercicio 7: 6 no es >= 8 pero sí es >= 5.",
  por={"Alta": "6 >= 8 es False.",
       "Baja": "Solo sería Baja si 6 >= 5 fuera False.",
       "Error": "Los ternarios se pueden encadenar."})
q("fill", 'opcion = "borrar"\nmatch opcion:\n    case "crear":\n        print("Creando")\n    case ___:\n        print("Borrando")\n    case _:\n        print("No reconocida")',
  ['"borrar"', "borrar", "_", '"Borrar"'], 0,
  "Cada case compara con un texto, entre comillas y exactamente igual.", expect="Borrando",
  por={"borrar": "Sin comillas es un nombre de variable, no un texto. Python da error porque ese case lo captura todo.",
       "_": "_ es el caso por defecto, y solo puede ir al final. Aquí habría dos.",
       '"Borrar"': 'Python distingue mayúsculas: "Borrar" no es igual a "borrar", así que iría al caso por defecto.'})
q("out", 'precios = [250, 150, 300]\ncliente = {"socio": False, "saldo": 600}\ncupones = {"DESC10", "OFERTA20"}\ncupon = "desc10"\ntotal = sum(precios)\ntiene_descuento = cliente["socio"] or cupon in cupones\nfinal = total * 0.9 if tiene_descuento else total\nprint(final, "Aceptado" if cliente["saldo"] >= final else "Saldo insuficiente")',
  ["700 Saldo insuficiente", "630.0 Aceptado", "630.0 Saldo insuficiente", "700 Aceptado"], 0,
  'No es socio y "desc10" no está en el set (que tiene "DESC10"). Sin descuento son 700, y 600 no llega.',
  por={"630.0 Aceptado": 'in distingue mayúsculas: "desc10" no es "DESC10", así que no hay descuento.',
       "630.0 Saldo insuficiente": "No se aplica descuento: el cupón está en minúsculas.",
       "700 Aceptado": "El saldo (600) es menor que 700."})
q("out", 'requisitos = (18, 6, True)\ncandidato = {"edad": 24, "nota": 5.5, "permiso": True}\ncumple = candidato["edad"] >= requisitos[0] and candidato["nota"] >= requisitos[1]\nprint("apto" if cumple else "no apto", requisitos[1])',
  ["no apto 6", "apto 6", "apto 18", "no apto 18"], 0,
  "requisitos[1] es la nota mínima (6), y 5.5 no llega.",
  por={"apto 6": "La edad cumple, pero 5.5 >= 6 es False, y con and basta un False.",
       "apto 18": "requisitos[1] es el SEGUNDO elemento (6). Además la nota no llega.",
       "no apto 18": "requisitos[1] es el segundo elemento: 6. requisitos[0] sería 18."})
q("out", 'nombres = ["Frodo", "Bilbo"]\nfor posicion, nombre in enumerate(nombres):\n    print(posicion, nombre)',
  ["0 Frodo\n1 Bilbo", "1 Frodo\n2 Bilbo", "Frodo 0\nBilbo 1", "0\n1"], 0,
  "enumerate da (posición, valor) empezando en 0.",
  por={"1 Frodo\n2 Bilbo": "Sin start=1, enumerate empieza en 0.",
       "Frodo 0\nBilbo 1": "Se imprime posicion primero, que es como está escrito el print.",
       "0\n1": "Se imprimen las dos variables, posición y nombre."})

# ---------------------------------------------------------------------
examen("practica3", "Tu práctica 3: bucles", "Ejercicios 3")
# ---------------------------------------------------------------------
q("out", "notas = [6, 8, 4, 10, 3]\naprobados = 0\ntotal = 0\nfor nota in notas:\n    total += nota\n    if nota >= 5:\n        aprobados += 1\nprint(aprobados, total / len(notas))",
  ["3 6.2", "2 6.2", "3 31", "3 6"], 0,
  "Contador (aprobados) y acumulador (total) a la vez, como en tu ejercicio 1.",
  por={"2 6.2": "6, 8 y 10 son >= 5: son 3 aprobados.",
       "3 31": "31 es el total; falta dividir entre len(notas).",
       "3 6": "/ siempre da float, y 31 / 5 es 6.2."})
q("out", "notas = [6, 8, 4, 10, 3]\nalta = notas[0]\nbaja = notas[0]\nfor n in notas:\n    if n > alta:\n        alta = n\n    if n < baja:\n        baja = n\nprint(alta, baja)",
  ["10 3", "6 6", "10 4", "8 3"], 0,
  "Máximo y mínimo a mano: empiezan con el primer elemento y se actualizan en el bucle.",
  por={"6 6": "alta y baja sí cambian dentro del bucle cuando aparece uno mayor o menor.",
       "10 4": "El 3 es menor que el 4: el mínimo es 3.",
       "8 3": "El 10 aparece después y supera al 8."})
q("out", 'productos = ["pan", "leche", "arroz"]\nprecios = [1.2, 0.8, 2.0]\ntotal = 0\nfor producto, precio in zip(productos, precios):\n    total += precio\nif total > 20:\n    total -= total * 0.10\nprint(total)',
  ["4.0", "3.6", "4", "Error"], 0,
  "El total es 4.0. El descuento solo se aplica si supera 20.",
  por={"3.6": "El descuento del 10 % solo se aplica si total > 20, y 4.0 no lo es.",
       "4": "Sumar floats da float: 4.0.",
       "Error": "zip con dos listas del mismo tamaño funciona sin problema."})
q("out", "pares = 0\nmultiplos5 = 0\nfor n in range(1, 21):\n    if n % 2 == 0:\n        pares += 1\n    if n % 5 == 0:\n        multiplos5 += 1\nprint(pares, multiplos5)",
  ["10 4", "10 5", "11 4", "9 3"], 0,
  "range(1, 21) va del 1 al 20: 10 pares y 4 múltiplos de 5 (5, 10, 15, 20).",
  por={"10 5": "range(1, 21) llega hasta 20, no 25: múltiplos de 5 son 5, 10, 15 y 20.",
       "11 4": "Del 1 al 20 hay exactamente 10 pares.",
       "9 3": "El 20 SÍ está incluido (el final es 21)."})
q("out", 'pwd = "python2024"\nprint(len(pwd) >= 8 and "@" in pwd and pwd != "12345678")',
  ["False", "True", "Error", "None"], 0,
  "Tiene 10 caracteres y no es 12345678, pero no tiene @. Con and basta un False.",
  por={"True": 'Falta la @: "@" in pwd es False, y con and todo es False.',
       "Error": "len, in y != se pueden combinar con and sin problema.",
       "None": "Una comparación con and devuelve True o False."})
q("out", 'inventario = {"ratón": 12, "teclado": 5, "monitor": 0, "cable": 25}\ntotal = 0\npocos = 0\nfor producto, unidades in inventario.items():\n    total += unidades\n    if unidades < 10:\n        pocos += 1\nprint(total, pocos)',
  ["42 2", "42 1", "4 2", "42 3"], 0,
  "Se suman las unidades (12+5+0+25) y se cuentan los que tienen menos de 10 (teclado y monitor).",
  por={"42 1": "El monitor tiene 0 unidades, y 0 también es < 10.",
       "4 2": "total acumula unidades, no cuenta productos.",
       "42 3": "El ratón tiene 12, que no es < 10."})
q("out", 'alumnos = ["Isaac", "Anna", "Carles", "Pau"]\nbuscar = "Carles"\nencontrado = False\nfor posicion, nombre in enumerate(alumnos):\n    if nombre == buscar:\n        print("Posición", posicion)\n        encontrado = True\n        break\nif not encontrado:\n    print("No encontrado")',
  ["Posición 2", "Posición 3", "Posición 2\nNo encontrado", "No encontrado"], 0,
  "Búsqueda con bandera y break, como tu ejercicio 7.",
  por={"Posición 3": "enumerate cuenta desde 0: Isaac 0, Anna 1, Carles 2.",
       "Posición 2\nNo encontrado": "encontrado pasa a True, así que not encontrado es False y no se imprime.",
       "No encontrado": "Carles sí está en la lista."})
q("out", "numeros = [5, -7, 0, 10, -1, 0]\nsuma = 0\nceros = 0\nfor n in numeros:\n    if n < 0:\n        continue\n    if n == 0:\n        ceros += 1\n    else:\n        suma += n\nprint(suma, ceros)",
  ["15 2", "7 2", "15 0", "-3 2"], 0,
  "continue se salta los negativos. Se suman 5 y 10 y se cuentan dos ceros.",
  por={"7 2": "Los negativos no se suman: continue salta a la siguiente vuelta antes de llegar a la suma.",
       "15 0": "Hay dos ceros y entran en el if n == 0.",
       "-3 2": "Los negativos se ignoran con continue."})
q("out", 'u = {"nombre": "Marc", "edad": 17, "activo": True, "puntos": 80}\nif not u["activo"]:\n    c = "Inactivo"\nelif u["puntos"] >= 100:\n    c = "Premium"\nelse:\n    c = "Estándar"\nif u["edad"] < 18:\n    c += " (menor)"\nprint(c)',
  ["Estándar (menor)", "Estándar", "Premium (menor)", "Inactivo"], 0,
  "Está activo con 80 puntos (Estándar). El segundo if es independiente y añade (menor).",
  por={"Estándar": "El segundo if no forma parte del if/elif anterior: también se comprueba, y 17 < 18.",
       "Premium (menor)": "80 >= 100 es False.",
       "Inactivo": "activo es True, así que not activo es False."})
q("out", 'codigo = "1234"\nintentos = ["0000", "", "1234", "9999"]\nacceso = False\nfor i in intentos:\n    if i == "":\n        pass\n    elif i == codigo:\n        acceso = True\n        break\n    else:\n        print("Incorrecto", i)\nprint(acceso)',
  ["Incorrecto 0000\nTrue", "Incorrecto 0000\nIncorrecto \nTrue", "Incorrecto 0000\nIncorrecto 9999\nTrue", "True"], 0,
  "El vacío entra en el pass (no hace nada), el 1234 hace break y el 9999 ya no se mira.",
  por={"Incorrecto 0000\nIncorrecto \nTrue": 'El intento vacío entra en el primer if, donde solo hay pass, así que no imprime nada.',
       "Incorrecto 0000\nIncorrecto 9999\nTrue": "break sale del bucle en el 1234: el 9999 nunca se revisa.",
       "True": '"0000" no es vacío ni el código: entra en el else e imprime.'})
q("out", 'alumno = {"nombre": "Isaac", "nota_media": 8.5, "faltas": 12}\nif alumno["nota_media"] >= 5 and alumno["faltas"] <= 10:\n    print("Aprobado sin aviso")\nelif alumno["nota_media"] >= 5 and alumno["faltas"] > 10:\n    print("Aprobado con aviso")\nelse:\n    print("Suspendido")',
  ["Aprobado con aviso", "Aprobado sin aviso", "Suspendido", "Aprobado sin aviso\nAprobado con aviso"], 0,
  "Aprueba (8.5) pero tiene 12 faltas, que son más de 10.",
  por={"Aprobado sin aviso": "12 <= 10 es False, así que el primer if no se cumple.",
       "Suspendido": "El elif se cumple: 8.5 >= 5 y 12 > 10.",
       "Aprobado sin aviso\nAprobado con aviso": "En if/elif solo se ejecuta un bloque."})
q("out", "i = 5\ni = i + 1\ni += 1\nprint(i)", ["7", "6", "5", "12"], 0,
  "i = i + 1 y i += 1 hacen lo mismo: dos sumas de 1.",
  por={"6": "Se suma 1 dos veces: i = i + 1 y luego i += 1.",
       "5": "Las dos líneas modifican i.",
       "12": "i += 1 suma 1, no suma i."})

# ---------------------------------------------------------------------
examen("practicaml", "Tu práctica ML: estadística a mano", "ML 3 (sin pandas)")
# ---------------------------------------------------------------------
q("out", "puntos = [50, 60, 60, 70, 70, 80, 80, 80, 90, 100]\nsuma = 0\nfor valor in puntos:\n    suma += valor\nprint(suma / len(puntos))",
  ["74.0", "740", "74", "75.0"], 0,
  "Media con bucle: 740 / 10.",
  por={"740": "740 es la suma; falta dividir entre la cantidad.",
       "74": "/ siempre da float.",
       "75.0": "75 es la mediana, no la media."})
q("out", "o = [50, 60, 60, 70, 70, 80, 80, 80, 90, 100]\nn = len(o)\nprint(o[n // 2 - 1], o[n // 2])",
  ["70 80", "80 80", "70 70", "60 70"], 0,
  "n = 10: los centrales son las posiciones 4 y 5 (quinto y sexto valor). La mediana es (70 + 80) / 2 = 75.",
  por={"80 80": "n // 2 - 1 es 4, la quinta posición, que vale 70.",
       "70 70": "o[n // 2] es o[5], la sexta posición, que vale 80.",
       "60 70": "Recuerda que se cuenta desde 0: o[4] es 70."})
q("out", "o = [3, 1, 2]\ni = 0\nfor j in range(i + 1, len(o)):\n    if o[j] < o[i]:\n        o[i], o[j] = o[j], o[i]\nprint(o)",
  ["[1, 3, 2]", "[1, 2, 3]", "[3, 1, 2]", "[2, 1, 3]"], 0,
  "Solo la primera pasada del intercambio directo (i = 0): el 1 sube al principio, pero el 3 y el 2 todavía no se comparan.",
  por={"[1, 2, 3]": "Es solo la pasada i = 0; la que ordena el 3 y el 2 sería i = 1.",
       "[3, 1, 2]": "1 < 3, así que sí se intercambian.",
       "[2, 1, 3]": "Se compara la posición 0 con las siguientes, no vecinos como en burbuja."})
q("out", "o = [4, 2, 3, 1]\ni = 0\npos_min = i\nfor j in range(i + 1, len(o)):\n    if o[j] < o[pos_min]:\n        pos_min = j\no[i], o[pos_min] = o[pos_min], o[i]\nprint(o, pos_min)",
  ["[1, 2, 3, 4] 3", "[2, 4, 3, 1] 1", "[4, 2, 3, 1] 3", "[1, 2, 3, 4] 0"], 0,
  "Selección: busca la posición del mínimo (el 1, en la posición 3) y hace UN intercambio con la posición 0.",
  por={"[2, 4, 3, 1] 1": "Selección no cambia al primer menor que encuentra: recorre todo y se queda con el mínimo (el 1).",
       "[4, 2, 3, 1] 3": "El intercambio de la última línea sí se ejecuta.",
       "[1, 2, 3, 4] 0": "pos_min guarda dónde estaba el mínimo: la posición 3."})
q("out", "puntos = [50, 60, 60, 80, 80, 80]\nfrecuencias = {}\nfor valor in puntos:\n    if valor in frecuencias:\n        frecuencias[valor] += 1\n    else:\n        frecuencias[valor] = 1\nmoda = puntos[0]\nmayor = 0\nfor valor in frecuencias:\n    if frecuencias[valor] > mayor:\n        mayor = frecuencias[valor]\n        moda = valor\nprint(moda, mayor)",
  ["80 3", "60 2", "50 1", "3 80"], 0,
  "Moda con diccionario: 80 aparece 3 veces.",
  por={"60 2": "60 aparece 2 veces, pero 80 aparece 3.",
       "50 1": "moda empieza en 50, pero se actualiza cuando encuentra una frecuencia mayor.",
       "3 80": "Se imprime moda (el valor) y luego mayor (cuántas veces)."})
q("out", "media = 74\nprint([valor - media for valor in [50, 74, 100]])",
  ["[-24, 0, 26]", "[24, 0, 26]", "[-24.0, 0.0, 26.0]", "[50, 74, 100]"], 0,
  "Desviación = valor - media. Negativa por debajo, positiva por encima.",
  por={"[24, 0, 26]": "50 - 74 es negativo: está por debajo de la media.",
       "[-24.0, 0.0, 26.0]": "Todo son int, y int - int sigue siendo int.",
       "[50, 74, 100]": "La comprensión crea una lista nueva con las restas."})
q("out", "l = [2, 4, 6]\nm = sum(l) / len(l)\nvar = sum(map(lambda x: (x - m) ** 2, l)) / len(l)\nprint(round(var, 2), round(var ** 0.5, 2))",
  ["2.67 1.63", "4.0 2.0", "8.0 2.83", "2.67 2.67"], 0,
  "Media 4. Cuadrados: 4, 0, 4. Suma 8, entre n = 3: 2.67. La desviación es la raíz: 1.63.",
  por={"4.0 2.0": "Eso es dividir entre n - 1 = 2 (muestral). Aquí se divide entre len(l) = 3.",
       "8.0 2.83": "8 es la suma de cuadrados; falta dividir entre n.",
       "2.67 2.67": "La desviación estándar es la RAÍZ de la varianza (** 0.5)."})
q("err", "normalizados = []\nnormalizados[0] = 0.5", ["IndexError", "KeyError", "TypeError", "Ningún error"], 0,
  "Asignar por índice solo cambia una posición que ya existe. En una lista vacía hay que usar append, o crearla con [0] * n.")
q("out", 'alumnos = [{"nombre": "Ana", "p": 50}, {"nombre": "Hugo", "p": 80}, {"nombre": "Lucía", "p": 100}]\nmedia = 74\nprint(list(map(lambda f: f["nombre"], filter(lambda f: f["p"] > media, alumnos))))',
  ["['Hugo', 'Lucía']", "['Ana']", "[80, 100]", "[True, True]"], 0,
  "filter se queda con los que superan la media y map saca su nombre (tu ejercicio 10 de ML).",
  por={"['Ana']": "El filtro es p > media: Ana (50) queda por debajo.",
       "[80, 100]": 'map extrae f["nombre"], no los puntos.',
       "[True, True]": "filter devuelve los elementos, no True/False."})
q("out", "print(round((100 - 74) / 14.28, 2))", ["1.82", "26", "-1.82", "0.26"], 0,
  "z = (valor - media) / desviación. Lucía (100) está a 1.82 desviaciones por encima.",
  por={"26": "26 es la distancia a la media; falta dividir entre la desviación.",
       "-1.82": "100 está por encima de la media, así que z es positivo.",
       "0.26": "Se divide entre la desviación (14.28), no entre 100."})
q("out", "print(max(map(lambda v: abs(v - 74), [50, 60, 100])))", ["26", "24", "-24", "100"], 0,
  "abs quita el signo. Distancias: 24, 14 y 26. La mayor es 26.",
  por={"24": "abs(50 - 74) es 24, pero 100 se aleja 26.",
       "-24": "abs siempre da un número positivo.",
       "100": "max se aplica a las distancias, no a los valores originales."})


# ---------------------------------------------------------------------
examen("bucles2", "Bucles II: while, anidados y textos", "Tema 3")
# ---------------------------------------------------------------------
q("out", "saldo = 10\nwhile saldo > 0:\n    saldo -= 4\n    print(saldo)",
  ["6\n2\n-2", "6\n2", "10\n6\n2", "6\n2\n-2\n-6"], 0,
  "La condición se mira al principio de cada vuelta: con 2 todavía entra, resta y imprime -2.",
  por={"6\n2": "Con saldo = 2, 2 > 0 es True: entra otra vez, resta 4 e imprime -2.",
       "10\n6\n2": "Se resta ANTES de imprimir: el 10 nunca se imprime.",
       "6\n2\n-2\n-6": "Con -2, -2 > 0 es False y el bucle termina."})
q("out", "n = 1\nveces = 0\nwhile n < 100:\n    n *= 3\n    veces += 1\nprint(n, veces)",
  ["243 5", "81 4", "243 6", "100 5"], 0,
  "n vale 3, 9, 27, 81 y 243: cinco vueltas. Con 243 la condición ya es False.",
  por={"81 4": "81 < 100 sigue siendo True: hay una vuelta más que lo multiplica por 3.",
       "243 6": "Son 5 multiplicaciones: 3, 9, 27, 81, 243.",
       "100 5": "n no se queda en 100: se multiplica por 3 y luego se comprueba."})
q("out", 'intentos = ["x", "y", "ok", "z"]\ni = 0\nwhile intentos[i] != "ok":\n    i += 1\nprint(i)',
  ["2", "3", "1", "Error"], 0,
  "Avanza mientras no encuentre \"ok\", que está en la posición 2.",
  por={"3": "Se cuenta desde 0: x 0, y 1, ok 2.",
       "1": "En la posición 1 está \"y\", que no es \"ok\": sigue avanzando.",
       "Error": "Para al encontrar \"ok\", antes de salirse de la lista."})
q("out", 'for i in range(1, 4):\n    print("*" * i)',
  ["*\n**\n***", "***\n**\n*", "*\n*\n*", "*\n**\n***\n****"], 0,
  '"*" * i repite el asterisco i veces, con i = 1, 2 y 3.',
  por={"***\n**\n*": "i va de 1 a 3 en orden creciente.",
       "*\n*\n*": '"*" * i repite el texto i veces, no siempre una.',
       "*\n**\n***\n****": "range(1, 4) no incluye el 4."})
q("out", "for i in range(1, 3):\n    for j in range(1, 3):\n        print(i * j)",
  ["1\n2\n2\n4", "1\n4", "1\n2\n3\n4", "2\n4"], 0,
  "Por cada i, j hace todas sus vueltas: (1,1) (1,2) (2,1) (2,2).",
  por={"1\n4": "El bucle de dentro se hace completo para cada i: son 4 combinaciones.",
       "1\n2\n3\n4": "Se imprime i * j, no un contador.",
       "2\n4": "range(1, 3) empieza en 1, así que también está i = 1."})
q("out", "m = [[1, 2], [3, 4]]\nfor fila in m:\n    print(sum(fila))",
  ["3\n7", "4\n6", "10", "1\n2\n3\n4"], 0,
  "Cada fila es una lista: [1, 2] suma 3 y [3, 4] suma 7.",
  por={"4\n6": "Eso sería sumar columnas. Aquí se recorre fila a fila.",
       "10": "El print está dentro del bucle: imprime una suma por fila.",
       "1\n2\n3\n4": "sum(fila) suma la fila entera de una vez."})
q("out", 'palabra = "programa"\nvocales = 0\nfor letra in palabra:\n    if letra in "aeiou":\n        vocales += 1\nprint(vocales)',
  ["3", "4", "8", "2"], 0,
  "Recorrer un texto va letra a letra: o, a, a son las vocales.",
  por={"4": "p-r-o-g-r-a-m-a: las vocales son o, a, a.",
       "8": "8 es len(palabra). Aquí solo se cuentan vocales.",
       "2": "La a aparece dos veces y cuentan las dos."})
q("out", 'texto = "hola"\ninv = ""\nfor c in texto:\n    inv = c + inv\nprint(inv)',
  ["aloh", "hola", "h", "a"], 0,
  "c + inv pone cada letra DELANTE de lo que había: el texto queda al revés.",
  por={"hola": "Sería así con inv + c. Con c + inv cada letra va delante.",
       "h": "inv va acumulando todas las letras.",
       "a": "inv va acumulando todas las letras, no solo la última."})
q("out", "for i in range(3):\n    for j in range(3):\n        if j == 1:\n            break\n        print(i, j)",
  ["0 0\n1 0\n2 0", "0 0", "0 0\n0 1\n1 0\n1 1\n2 0\n2 1", "0 0\n1 0\n2 0\n3 0"], 0,
  "break solo sale del bucle de DENTRO. El de fuera sigue con la siguiente i.",
  por={"0 0": "break solo rompe el bucle interior; el exterior continúa.",
       "0 0\n0 1\n1 0\n1 1\n2 0\n2 1": "Con j == 1 hace break ANTES de imprimir.",
       "0 0\n1 0\n2 0\n3 0": "range(3) es 0, 1 y 2."})
q("out", "n = 5\nwhile n > 0:\n    n //= 2\nprint(n)", ["0", "1", "2", "-1"], 0,
  "5 // 2 = 2, 2 // 2 = 1, 1 // 2 = 0. Con 0 el bucle termina.",
  por={"1": "1 > 0 es True: hay otra vuelta y 1 // 2 da 0.",
       "2": "2 > 0 es True: sigue dividiendo.",
       "-1": "1 // 2 da 0, no -1."})
q("err", "total = 0\nfor n in [1, 2, 3]:\ntotal += n", ["IndentationError", "SyntaxError", "NameError", "Ningún error"], 0,
  "El cuerpo del for tiene que ir indentado.")
q("out", 'alumnos = {"Ana": [5, 7], "Luis": [3, 4]}\nfor nombre, notas in alumnos.items():\n    print(nombre, sum(notas) / len(notas))',
  ["Ana 6.0\nLuis 3.5", "Ana 12\nLuis 7", "Ana 6\nLuis 3.5", "6.0\n3.5"], 0,
  "Cada valor del diccionario es una lista de notas, y se calcula su media.",
  por={"Ana 12\nLuis 7": "Falta dividir entre len(notas).",
       "Ana 6\nLuis 3.5": "/ siempre da float: 6.0.",
       "6.0\n3.5": "El print incluye también el nombre."})

# ---------------------------------------------------------------------
examen("funciones3", "Funciones III: escribir y seguir", "Tema 4")
# ---------------------------------------------------------------------
q("fill", "def es_par(n):\n    return n % 2 ___ 0\n\nprint(es_par(4), es_par(7))", ["==", "=", "!=", ">"], 0,
  "Una función que dice True/False puede devolver directamente la comparación.", expect="True False",
  por={"=": "= asigna. Dentro de return hay que comparar con ==.",
       "!=": "Invierte el resultado: sería es_impar.",
       ">": "n % 2 > 0 es True para los impares: sería es_impar."})
q("fill", "def area(base, altura=___):\n    return base * altura / 2\n\nprint(area(4), area(4, 10))", ["2", "1", "0", "None"], 0,
  "area(4) usa el valor por defecto: 4 * 2 / 2 = 4.0.", expect="4.0 20.0",
  por={"1": "Con altura 1, area(4) da 2.0, no 4.0.",
       "0": "Con altura 0 el área sería 0.0.",
       "None": "4 * None da error."})
q("out", "def contar(l, valor):\n    c = 0\n    for x in l:\n        if x == valor:\n            c += 1\n    return c\n\nprint(contar([1, 2, 1, 1], 1))",
  ["3", "1", "4", "2"], 0,
  "El return está FUERA del for: primero recorre toda la lista y luego devuelve.",
  por={"1": "El return va después del bucle, así que cuenta todos los 1.",
       "4": "Solo cuenta los que son iguales a 1.",
       "2": "Hay tres 1 en la lista."})
q("out", "def contar(l, valor):\n    c = 0\n    for x in l:\n        if x == valor:\n            c += 1\n        return c\n\nprint(contar([1, 2, 1, 1], 1))",
  ["1", "3", "0", "None"], 0,
  "Error típico: el return está DENTRO del for, así que la función termina en la primera vuelta.",
  por={"3": "Fíjate en la sangría: return está dentro del for y acaba en la primera vuelta.",
       "0": "La primera x ya es 1, así que c vale 1 cuando llega al return.",
       "None": "Sí hay return (aunque esté mal colocado)."})
q("out", 'def f(x):\n    if x > 0:\n        return "pos"\n\nprint(f(5), f(-1))',
  ["pos None", "pos neg", "pos", "pos False"], 0,
  "Si x no es > 0, la función acaba sin pasar por ningún return y devuelve None.",
  por={"pos neg": 'No hay ningún return "neg". Sin return se devuelve None.',
       "pos": "Se imprimen dos valores, uno por cada llamada.",
       "pos False": "Sin return no devuelve False: devuelve None."})
q("out", "def aplicar(f, x):\n    return f(x)\n\nprint(aplicar(lambda n: n * 3, 4))", ["12", "7", "4", "Error"], 0,
  "Las funciones se pueden pasar como argumento: aplicar llama a la lambda con 4.",
  por={"7": "La lambda multiplica (n * 3), no suma.",
       "4": "aplicar no devuelve x: devuelve f(x).",
       "Error": "En Python las funciones son objetos y se pueden pasar como argumento."})
q("out", "def potencia(b, e):\n    if e == 0:\n        return 1\n    return b * potencia(b, e - 1)\n\nprint(potencia(2, 3))", ["8", "6", "9", "1"], 0,
  "2 * potencia(2, 2) = 2 * 2 * potencia(2, 1) = 2 * 2 * 2 * 1 = 8.",
  por={"6": "Es 2 · 2 · 2, no 2 · 3.",
       "9": "Eso sería 3 ** 2. Aquí la base es 2 y el exponente 3.",
       "1": "1 es el caso base, pero cada llamada lo multiplica por b."})
q("out", "def cuenta(n):\n    if n == 0:\n        return\n    print(n)\n    cuenta(n - 1)\n\ncuenta(3)", ["3\n2\n1", "1\n2\n3", "3\n2\n1\n0", "3"], 0,
  "Imprime y después se llama con n - 1. Con 0 para sin imprimir.",
  por={"1\n2\n3": "Imprime ANTES de llamarse, así que va de mayor a menor.",
       "3\n2\n1\n0": "Con n == 0 hace return antes del print.",
       "3": "Se vuelve a llamar con n - 1 hasta llegar a 0."})
q("out", "def media(*n):\n    return sum(n) / len(n)\n\nprint(media(4, 6, 8))", ["6.0", "18", "6", "Error"], 0,
  "*n recoge (4, 6, 8) en una tupla: 18 / 3.",
  por={"18": "18 es la suma; falta dividir entre len(n).",
       "6": "/ siempre da float: 6.0.",
       "Error": "sum y len funcionan con tuplas."})
q("out", 'def info(nombre, **extra):\n    print(nombre, len(extra))\n\ninfo("Pau", edad=24, curso="IA")', ["Pau 2", "Pau 3", "Pau", "Error"], 0,
  "nombre recoge \"Pau\" y **extra recoge solo los argumentos con nombre que sobran: edad y curso.",
  por={"Pau 3": "nombre no entra en **extra: extra solo tiene edad y curso.",
       "Pau": "El print también muestra len(extra).",
       "Error": "**extra recoge los argumentos con nombre que no tienen parámetro propio."})
q("out", "def mm(l):\n    return min(l), max(l)\n\nmn, mx = mm([3, 8, 1])\nprint(mx - mn)", ["7", "-7", "(1, 8)", "Error"], 0,
  "Se desempaqueta la tupla: mn = 1, mx = 8.",
  por={"-7": "Se calcula mx - mn = 8 - 1.",
       "(1, 8)": "La tupla se desempaqueta en mn y mx; se imprime la resta.",
       "Error": "Una tupla de 2 se puede desempaquetar en 2 variables."})
q("mc", q="¿Qué devuelve una función que termina con return a, b?",
  opts=["Una tupla (a, b)", "Solo a", "Una lista [a, b]", "Da error"], a=0,
  exp="Varios valores separados por comas forman una tupla.",
  por={"Solo a": "Devuelve los dos valores juntos.",
       "Una lista [a, b]": "Es una tupla, con paréntesis, no una lista.",
       "Da error": "Devolver varios valores es válido en Python."})
q("out", "total = 0\ndef sumar(x):\n    return total + x\n\nprint(sumar(5))", ["5", "Error", "0", "None"], 0,
  "Una función puede LEER una variable de fuera. Lo que no conviene es modificarla desde dentro.",
  por={"Error": "Leer una variable global desde una función sí está permitido.",
       "0": "Devuelve total + x = 0 + 5.",
       "None": "Sí hay return."})

# ---------------------------------------------------------------------
examen("simulacro2", "Simulacro 2: completa el código", "Todos")
# ---------------------------------------------------------------------
q("fill", "notas = [7, 3, 9]\naprobadas = [n for n in notas ___ n >= 5]\nprint(aprobadas)", ["if", "for", "and", "while"], 0,
  "En una comprensión el filtro se escribe con if al final.", expect="[7, 9]",
  por={"for": "El filtro de una comprensión va con if.",
       "and": "and no filtra: Python intenta calcular notas and n >= 5 y n todavía no existe.",
       "while": "while no se puede usar dentro de una comprensión."})
q("fill", 'd = {"ratón": 12, "monitor": 0}\nagotados = []\nfor p, u in d.items():\n    if u == 0:\n        agotados.___(p)\nprint(agotados)', ["append", "add", "insert", "push"], 0,
  "A una lista se le añade al final con append.", expect="['monitor']",
  por={"add": "add es de los set, no de las listas.",
       "insert": "insert necesita dos cosas: la posición y el valor.",
       "push": "push no existe en Python (es de JavaScript)."})
q("fill", "precios = [10, 20, 30]\ntotal = ___\nfor p in precios:\n    total += p\nprint(total)", ["0", "[]", "None", "1"], 0,
  "Un acumulador de sumas empieza en 0.", expect="60",
  por={"[]": "Una lista no se puede sumar con un número.",
       "None": "None + 10 da error.",
       "1": "Empezar en 1 suma uno de más: 61."})
q("fill", 'edad = 20\nprint("Mayor" ___ edad >= 18 else "Menor")', ["if", "and", "?", "elif"], 0,
  "Ternario: valor_si_true if condición else valor_si_false.", expect="Mayor",
  por={"and": "El ternario se escribe con if … else.",
       "?": "En Python no existe condición ? a : b (es de otros lenguajes).",
       "elif": "elif solo existe en un if de varias líneas."})
q("fill", 'def saludar(nombre___):\n    return "Hola " + nombre\n\nprint(saludar())', ['="anónimo"', "=anónimo", '="Anónimo"', ': "anónimo"'], 0,
  "Un valor por defecto se pone con = en la definición, y si es texto va entre comillas.", expect="Hola anónimo",
  por={"=anónimo": "Sin comillas, anónimo sería una variable, y no existe.",
       '="Anónimo"': "Funciona, pero imprime \"Anónimo\" con mayúscula, y el resultado pedido va en minúscula.",
       ': "anónimo"': "Con : es una anotación de tipo, no un valor por defecto."})
q("fill", "for i in range(___):\n    print(i)", ["5, 2, -1", "5, 3, -1", "3, 6", "5, 2"], 0,
  "Hacia atrás con paso -1. El final (2) no se incluye, así que para en 3.", expect="5\n4\n3",
  por={"5, 3, -1": "El final no se incluye: se queda en 4.",
       "3, 6": "Eso va hacia delante: 3, 4, 5.",
       "5, 2": "Sin paso negativo no puede ir hacia atrás: no sale nada."})
q("fill", 'alumno = {"nombre": "Ana"}\nalumno[___] = 8.5\nprint(alumno)', ['"nota"', "nota", "0", ".nota"], 0,
  "Las claves de texto van entre comillas dentro de los corchetes.", expect="{'nombre': 'Ana', 'nota': 8.5}",
  por={"nota": "Sin comillas, nota sería una variable que no existe.",
       "0": "Crearía una clave 0, no \"nota\".",
       ".nota": "Los diccionarios no usan punto: se accede con [\"clave\"]."})
q("fill", "n = [4, 1, 3]\no = ___(n)\nprint(n, o)", ["sorted", "n.sort", "list", "reversed"], 0,
  "sorted devuelve una lista nueva ordenada y deja la original igual.", expect="[4, 1, 3] [1, 3, 4]",
  por={"n.sort": "sort no recibe la lista como argumento, y además cambiaría n y devolvería None.",
       "list": "list(n) hace una copia, pero no la ordena.",
       "reversed": "reversed la recorre al revés, no la ordena."})
q("fill", 'frec = {}\nfor x in "aba":\n    if x ___ frec:\n        frec[x] += 1\n    else:\n        frec[x] = 1\nprint(frec)', ["in", "not in", "==", "is"], 0,
  "Patrón de frecuencias: si la clave ya está en el diccionario se suma, si no se crea.", expect="{'a': 2, 'b': 1}",
  por={"not in": "Al revés: intentaría sumar a una clave que todavía no existe.",
       "==": "Compara la letra con el diccionario entero, que nunca es igual.",
       "is": "is no mira si está dentro: hay que usar in."})
q("fill", "def fact(n):\n    if n ___ 1:\n        return 1\n    return n * fact(n - 1)\n\nprint(fact(5), fact(0))", ["<=", "==", ">=", "!="], 0,
  "Con <= el caso base cubre el 1 y también el 0.", expect="120 1",
  por={"==": "fact(0) nunca llega a 1: baja a -1, -2… y da RecursionError.",
       ">=": "fact(5) devolvería 1 directamente, y fact(0) nunca cumple 0 >= 1: baja sin fin hasta RecursionError.",
       "!=": "Para todo lo que no sea 1 devuelve 1 enseguida."})
q("fill", "o = sorted([8, 2, 6, 4])\nn = len(o)\nprint((o[n // 2 - 1] + o[n // 2]) ___ 2)", ["/", "//", "*", "%"], 0,
  "Mediana con n par: la media de los dos centrales (4 y 6).", expect="5.0",
  por={"//": "// da entero (5). Además, con dos centrales impares perderías el .5.",
       "*": "La media es dividir entre 2, no multiplicar.",
       "%": "% da el resto, no la media."})
q("fill", 'usuarios = {"ana", "luis"}\nusuarios.___("marta")\nprint(len(usuarios))', ["add", "append", "insert", "push"], 0,
  "A un set se le añade con add.", expect="3",
  por={"append": "append es de las listas. Los set usan add.",
       "insert": "Los set no tienen posiciones, así que no hay insert.",
       "push": "push no existe en Python."})


# =====================================================================
# Por qué fallas: explicación de cada opción incorrecta (preguntas de los temas)
# =====================================================================
POR = {
    "tipos-1": {"3.5 1": "3.5 sería con /. // es división entera y quita los decimales.",
                "3 1.0": "Con dos int, % devuelve int: 1, no 1.0.",
                "4 1": "// no redondea al más cercano: se queda con la parte entera (3)."},
    "tipos-2": {"5": "/ siempre da float aunque sea exacta. Para obtener 5 usarías //.",
                "5.00": "print no añade ceros: un float exacto se muestra como 5.0.",
                "Error": "Dividir dos int es válido."},
    "tipos-3": {"3 16": "3 es el cociente (17 // 5). % da el RESTO: 2.",
                "2 8": "2 ** 4 = 2·2·2·2 = 16. El 8 sería 2 ** 3.",
                "3.4 16": "3.4 sería 17 / 5. % da el resto."},
    "tipos-4": {"9": 'x es el texto "3", no el número 3. str * int repite el texto.',
                "3 3 3": "Repetir un texto no añade espacios.",
                "Error": "str * int es válido (repite). Lo que da error es str + int."},
    "tipos-6": {"<class 'int'>": "/ siempre devuelve float, aunque el resultado sea exacto.",
                "2.0": "Se imprime el TIPO del resultado, no el resultado.",
                "<class 'str'>": "Es una división de números; no hay texto."},
    "tipos-7": {"13": "Van en orden: primero a = 8 y luego 8 * 2 = 16.",
                "10": "a += 3 se hace antes de multiplicar: 8 * 2.",
                "11": "*= multiplica, no suma."},
    "tipos-8": {"True True": "and necesita las dos, y 2 > 4 es False.",
                "True False": "5 > 3 and 2 > 4 da False. not False da True.",
                "False False": "not False es True."},
    "tipos-9": {"El número 0": "0 es un número: hay valor, y es cero.",
                "Un texto vacío": '"" es un texto que existe aunque esté vacío.',
                "El valor False": "False es un booleano. None no es ni True ni False."},
    "tipos-10": {"73 10": "print respeta el orden: primero va int(\"7\") + 3, que es 10.",
                 "10 10": 'str(7) + "3" une textos: "73".',
                 "73 73": 'int("7") lo convierte a número, así que + suma: 10.'},
    "compuestos-1": {"4 16": "Los índices empiezan en 0: l[0] es 4 y l[1] es 8.",
                     "8 15": "l[-1] es el ÚLTIMO elemento: 16.",
                     "4 15": "l[1] es el segundo (8) y l[-1] el último (16)."},
    "compuestos-2": {"5": "append añade UN elemento: la lista [4, 5] entera. Para añadir 4 y 5 sueltos harían falta dos append.",
                     "3": "append sí modifica la lista: tiene un elemento más.",
                     "Error": "Una lista puede contener otra lista."},
    "compuestos-4": {"{'a': 1, 'b': 2, 'c': 3}": 'd["a"] = 0 modifica el valor de "a".',
                     "{'b': 2, 'c': 3, 'a': 0}": "Modificar una clave no la mueve de sitio. Solo las claves nuevas van al final.",
                     "Error": "Asignar a una clave que no existe la crea."},
    "compuestos-6": {"5": "Un set elimina los repetidos.",
                     "2": "Quedan 1, 2 y 3: tres valores distintos.",
                     "4": "Solo hay tres valores distintos: 1, 2 y 3."},
    "compuestos-7": {"[20, 30, 40]": "El final del slice no se incluye: para antes del índice 3.",
                     "[10, 20, 30]": "Empieza en el índice 1 (20), no en el 0.",
                     "[30, 40]": "El índice 1 es 20, porque se cuenta desde 0."},
    "compuestos-8": {"Una lista": "Funcionaría, pero la lista es para datos que cambian. Para valores fijos, tupla.",
                     "Un set": "Un set no tiene orden: no sabrías cuál es x y cuál es y.",
                     "Un diccionario": "Se podría, pero para dos valores fijos y ordenados lo natural es una tupla."},
    "compuestos-9": {"True": 'in en un dict busca en las CLAVES ("nombre"), no en los valores ("Ana").',
                     "Error": "in con un diccionario es válido.",
                     "None": "in siempre devuelve True o False."},
    "compuestos-10": {"[1, 2]": "b = a NO copia: a y b son la misma lista, así que el append se ve en las dos.",
                      "[3]": "append añade al final; no borra lo que había.",
                      "Error": "Es válido: b es otro nombre para la misma lista."},
    "condicionales-1": {"B": "El if va primero y 6 >= 5 es True, así que el elif ya no se evalúa.",
                        "A\nB": "En un if/elif/else solo se ejecuta UN bloque: el primero que es True.",
                        "C": "else solo se ejecuta si todas las condiciones anteriores son False."},
    "condicionales-2": {"No": "or basta con que una sea True, y permiso es True.",
                        "True": "El ternario devuelve uno de los dos textos, no el booleano.",
                        "Error": "Se puede usar or dentro de un ternario."},
    "condicionales-4": {"Agradable": "30 < 25 es False.",
                        "Frío": "30 < 10 es False.",
                        "Agradable\nCalor": "Solo se ejecuta un bloque del if/elif/else."},
    "condicionales-5": {"Sí": "0 cuenta como False en un if.",
                        "0": "Se imprime uno de los dos textos, no x.",
                        "Error": "if x es válido con cualquier valor."},
    "condicionales-6": {"Inicio": '"sábado" no coincide con "lunes".',
                        "Casi": '"sábado" no coincide con "viernes".',
                        "Nada": "case _ recoge todo lo demás, así que siempre imprime algo."},
    "condicionales-7": {"pos": "-3 > 0 es False.",
                        "cero": 'Solo sería "cero" si no fuera > 0 ni < 0, pero -3 < 0 es True.',
                        "Error": "Los ternarios se pueden encadenar."},
    "condicionales-9": {"False True False": "not b es True, y True and True es True.",
                        "True False False": "a or b es True porque a ya es True.",
                        "True True True": "not a es False porque a es True."},
    "condicionales-10": {"Pasa": "entrada es False, así que va al else de dentro.",
                         "Menor": "20 >= 18 es True: entra en el if de fuera.",
                         "Pasa\nSin entrada": "El if/else de dentro solo ejecuta uno de los dos."},
    "bucles-1": {"[1, 4, 7, 10]": "El final (10) nunca se incluye.",
                 "[3, 6, 9]": "El primer número es el inicio (1), no el paso.",
                 "[1, 3, 6, 9]": "Va de 3 en 3 desde el 1: 1, 4, 7."},
    "bucles-2": {"[5, 3, 1, 0]": "De 5 restando 2: 5, 3, 1, -1… El 0 no aparece y el final no se incluye.",
                 "[5, 3]": "1 todavía es mayor que el final (0), así que entra.",
                 "[]": "Con paso negativo sí cuenta hacia atrás."},
    "bucles-3": {"15": "range(1, 5) no incluye el 5: 1+2+3+4 = 10.",
                 "4": "total acumula la suma, no cuenta vueltas.",
                 "6": "Falta el 4: range(1, 5) incluye 1, 2, 3 y 4."},
    "bucles-4": {"1": "Con i = 1, 1 > 0 sigue siendo True: da otra vuelta y queda en -2.",
                 "0": "Va de 3 en 3: 10, 7, 4, 1, -2. Nunca pasa por 0.",
                 "-3": "Desde 1, restar 3 da -2."},
    "bucles-5": {"1\n2": "continue solo se salta el 3; el bucle sigue con el 4.",
                 "1\n2\n4\n5": "break sale ANTES del print, así que el 5 no se imprime.",
                 "1\n2\n3\n4": "continue se salta el print del 3."},
    "bucles-6": {"0 a\n1 b": "start=1 hace que empiece a contar en 1.",
                 "a 1\nb 2": "enumerate da primero la posición y luego el valor.",
                 "1 ab": "Recorrer un texto va letra a letra."},
    "bucles-7": {"11\n22\n3": "zip para en la lista más corta: el 3 no tiene pareja.",
                 "11\n22\n33": "La segunda lista no tiene tercer elemento.",
                 "Error": "zip con listas de distinto tamaño no da error: se corta."},
    "bucles-8": {"impar": "n % 2 == 1 es False para 2, 4 y 6.",
                 "Nada": "El else del for se ejecuta porque no hubo break.",
                 "impar\ntodos pares": "Ningún número es impar, así que nunca entra en el if."},
    "bucles-9": {"1\n2": "Eso sería recorrer d.values().",
                 "a 1\nb 2": "Para clave y valor hace falta d.items() y dos variables.",
                 "('a', 1)\n('b', 2)": "Eso sería imprimir cada elemento de d.items()."},
    "bucles-10": {"5": "El bucle de dentro da 2 vueltas por cada una de las 3 de fuera: 3 × 2 = 6.",
                  "3": "Hay que contar las vueltas del bucle interior: 3 × 2.",
                  "2": "El de fuera repite 3 veces el de dentro: 3 × 2."},
    "bucles-11": {"[0, 2, 4, 6]": "El if filtra: solo pasan 0 y 2, que por 2 dan 0 y 4.",
                  "[2, 6]": "Los pares de range(4) son 0 y 2, no 1 y 3.",
                  "[4]": "El 0 también es par: 0 % 2 == 0."},
    "funciones1-1": {"8": "Calcula x * 2, pero sin return ese valor se pierde.",
                     "4": "La función no devuelve x: no devuelve nada (None).",
                     "Error": "Una función sin return es válida: devuelve None."},
    "funciones1-2": {"Hola Pau Hola Pau": 'La primera llamada no pasa argumento: usa "mundo".',
                     "Hola mundo Hola mundo": 'La segunda pasa "Pau", que sustituye al valor por defecto.',
                     "Error": "Un parámetro con valor por defecto se puede omitir."},
    "funciones1-4": {"7": "Por nombre: a=3 y b=10, aunque b se escriba primero. 3 - 10 = -7.",
                     "Error": "Los argumentos por nombre se pueden pasar en cualquier orden.",
                     "13": "Es una resta, no una suma."},
    "funciones1-5": {"2": "return termina la función: el print(2) nunca se ejecuta.",
                     "1\n2": "return termina la función: el print(2) nunca se ejecuta.",
                     "None": "Sí hay return: devuelve 1."},
    "funciones1-6": {"[2, 9]": "return a, b crea una TUPLA, con paréntesis.",
                     "2 9": "Se imprime x, que es una tupla entera.",
                     "2": "Devuelve los dos valores, no solo el primero."},
    "funciones1-7": {"1 1": "La x de dentro es local: la de fuera sigue valiendo 5.",
                     "5 5": "g() devuelve su x local, que vale 1.",
                     "5 1": "Al revés: g() da 1 y la x de fuera es 5."},
    "funciones1-9": {"Un parámetro": 'El parámetro es nombre, en la definición. "Ana" es el valor que pasas: el argumento.',
                     "Una variable global": "Es el valor que se pasa en la llamada.",
                     "Un return": "return es lo que la función devuelve."},
    "funciones2-1": {"1": "*n agrupa TODOS los argumentos: una tupla de 3.",
                     "6": "len cuenta elementos; 6 sería la suma.",
                     "Error": "Con *n puedes pasar cualquier cantidad de argumentos."},
    "funciones2-2": {"<class 'list'>": "*args es una tupla, no una lista.",
                     "<class 'int'>": "Aunque pases un solo valor, va dentro de una tupla.",
                     "<class 'dict'>": "Un dict sería con **kwargs."},
    "funciones2-3": {"(1, 2)": "Eso sería *args. **kwargs guarda nombre y valor en un diccionario.",
                     "[1, 2]": "**kwargs es un diccionario con nombres y valores.",
                     "x y": "Se imprime el diccionario entero."},
    "funciones2-4": {"10": "x * x es 5 · 5, no 5 + 5.",
                     "5": "La lambda devuelve el resultado de x * x.",
                     "Error": "Se puede guardar una lambda en una variable y llamarla."},
    "funciones2-5": {"[1, 2, 3]": "map aplica x + 1 a cada elemento.",
                     "[2]": "map transforma todos los elementos, no solo el primero.",
                     "9": "map no suma: devuelve otra lista."},
    "funciones2-6": {"[True, True]": "filter no devuelve True/False: devuelve los elementos que cumplen.",
                     "[1, 2]": "Esos son los que NO cumplen x > 2.",
                     "[False, True, False, True]": "Eso sería map. filter devuelve los elementos que dan True."},
    "funciones2-7": {"A": "sorted ordena de menor a mayor: 20 va antes que 30.",
                     "20": 'Se imprime ["n"], el nombre.',
                     "Error": "sorted con key=lambda funciona con listas de diccionarios."},
    "funciones2-8": {"3": "Se multiplica: 3 * fact(2) = 3 * 2 = 6.",
                     "0": "Con n == 0 devuelve 1, no 0.",
                     "9": "Es 3 · 2 · 1, no 3 · 3."},
    "funciones2-9": {"Devuelve None": "Nunca llega a devolver nada: se llama sin parar.",
                     "Devuelve 0": "Nunca llega a devolver nada: se llama sin parar.",
                     "Python la convierte en bucle": "Python no hace eso: la corta con RecursionError."},
    "funciones2-10": {"[1, 2, 3]": "l.sort() ordena l pero devuelve None, y se imprime r.",
                      "[3, 1, 2]": "Se imprime r, no l.",
                      "Error": "No da error: r simplemente vale None."},
    "funciones2-11": {"pera": "key=len compara longitudes: plátano (7 letras) es la más larga.",
                      "kiwi": "key=len compara longitudes: plátano (7 letras) es la más larga.",
                      "7": "max devuelve el elemento, no su longitud."},
    "estadistica-1": {"5": "/ siempre da float.",
                      "15": "Esa es la suma; falta dividir entre len(l).",
                      "3": "3 es la cantidad de elementos."},
    "estadistica-2": {"3": "Con n par, la mediana es la media de los DOS centrales: (3 + 7) / 2.",
                      "7": "Con n par, la mediana es la media de los DOS centrales: (3 + 7) / 2.",
                      "5": "/ siempre da float: 5.0."},
    "estadistica-3": {"n - 1": "Entre n - 1 es la MUESTRAL (lo que hace pandas por defecto).",
                      "n + 1": "No existe esa versión.",
                      "la media": "La media se resta a cada dato; luego se divide entre n."},
    "estadistica-4": {"2": "2 aparece 2 veces, pero 3 aparece 3.",
                      "6": "max devuelve el valor que más se repite, no cuántas veces.",
                      "1": "1 aparece solo una vez."},
    "estadistica-5": {"{'a': 1, 'b': 1}": 'La segunda "a" entra en el if y suma 1: queda 2.',
                      "{'b': 1, 'a': 2}": 'El dict mantiene el orden de creación: "a" se creó primero.',
                      "['a', 'b']": "f es un diccionario de frecuencias."},
    "estadistica-6": {"[1, 2, 3]": "Es una sola pasada: el 3 llega al final, pero el 2 y el 1 aún no se ordenan.",
                      "[3, 2, 1]": "Sí hay intercambios: 3 > 2 y después 3 > 1.",
                      "[2, 3, 1]": "Después de cambiar 3 y 2, se compara 3 con 1 y también se cambian."},
    "estadistica-7": {"Selección": "Selección busca la posición del mínimo y hace un intercambio por pasada.",
                      "Intercambio directo": "Intercambio directo compara la posición i con TODAS las siguientes, no con la vecina.",
                      "Ninguno": "Burbuja compara j con j + 1."},
    "estadistica-8": {"[0, 1, 2]": "Se divide entre (max - min) = 20, y / da float.",
                      "[10, 20, 30]": "La comprensión crea valores nuevos con la fórmula.",
                      "[0.1, 0.2, 0.3]": "Eso sería dividir entre 100. Min-max resta el mínimo y divide entre el rango."},
    "estadistica-9": {"Ha sacado -1.5 puntos": "z no es una nota: indica a cuántas desviaciones está de la media.",
                      "Está 1.5 puntos por debajo de la media": "Son desviaciones típicas, no puntos.",
                      "Está por encima de la media": "Negativo significa por debajo."},
    "estadistica-10": {"-2": "Sería lo correcto si empezara con mayor = l[0]. Con 0, ningún negativo lo supera.",
                       "-7": "Ningún número supera el 0 inicial, así que mayor nunca cambia.",
                       "-4": "Ningún número supera el 0 inicial, así que mayor nunca cambia."},
    "condicionales-8": {"=>": "Ese operador no existe: es >= (el = siempre detrás).",
                        "=": "Un solo = asigna. Para comparar hace falta >=.",
                        "=<": "Ese operador no existe: es <=. Y aquí queremos mayor o igual."},
    "funciones1-10": {"print": "print necesita paréntesis, y aunque los tuviera no devolvería el valor.",
                      "def": "def sirve para definir funciones, no para devolver.",
                      "yield": "yield no es de este temario: crea un generador en vez de devolver 8."},
    "simulacro-1": {"=": "aprobados = 1 no suma: vuelve a poner 1 cada vez.",
                    "==": "== compara pero no guarda nada: aprobados se queda en 0.",
                    "=+": "=+ 1 es lo mismo que = +1: asigna 1, no suma."},
    "simulacro-2": {"of": "for … of no existe en Python (es de JavaScript).",
                    "=": "for usa in, no =.",
                    ":": "Los dos puntos van al final de la línea del for."},
    "simulacro-3": {"keys": "keys() da solo las claves: no se pueden repartir en k, v.",
                    "values": "values() da solo los valores.",
                    "get": "get necesita una clave como argumento."},
    "simulacro-4": {"continue": "continue pasa a la siguiente vuelta: también encuentra el segundo 7.",
                    "pass": "pass no hace nada: el bucle sigue y encuentra el segundo 7.",
                    "return": "return solo se puede usar dentro de una función."},
    "simulacro-5": {"max": "max da el mayor, no la suma.",
                    "min": "min da el menor, no la suma.",
                    "len": "len da la cantidad: quedaría 2 / 2."},
    "simulacro-6": {"2, 8, 2": "El final (8) no se incluye.",
                    "0, 8, 2": "Empieza en 0 y no llega al 8.",
                    "2, 10": "Sin paso, va de 1 en 1."},
    "simulacro-7": {"0": "Con todos negativos, ninguno supera el 0.",
                    "len(l)": "len(l) es 3, mayor que todos los valores.",
                    "None": "No se puede comparar un número con None."},
    "simulacro-8": {"nums": "Sin * solo acepta un argumento, y le pasas tres.",
                    "**nums": "** es para argumentos con nombre (x=1).",
                    "[nums]": "No es una forma válida de escribir un parámetro."},
    "simulacro-9": {'p["edad"]': "key necesita una función. Además p no existe fuera de la lambda.",
                    'lambda: p["edad"]': "La lambda tiene que recibir cada elemento: lambda p: …",
                    '"edad"': "key necesita una función, no un texto."},
    "simulacro-10": {"len(o) / 2": "/ da float (1.5) y los índices tienen que ser int.",
                     "len(o)": "len(o) es 3, y el último índice es 2.",
                     "1.5": "Los índices tienen que ser int."},
    "estadistica-11": {"Ninguna": "sorted devuelve una lista nueva; sort cambia l y devuelve None.",
                       "sort devuelve una lista nueva; sorted cambia l": "Es al revés.",
                       "sorted solo funciona con números": "sorted también ordena textos."},
}

# Qué significa cada error, para explicar por qué otra opción no encaja
ERRORES = {
    "SyntaxError": "el código está mal escrito (falta :, = en vez de ==, …) y Python ni lo ejecuta",
    "IndentationError": "falta o sobra sangría en un bloque",
    "IndexError": "se accede a una posición de lista/tupla que no existe",
    "KeyError": "se busca una clave que no está en un diccionario",
    "TypeError": "se mezclan tipos incompatibles (str + int, None + 1) o se modifica algo inmutable",
    "NameError": "se usa una variable que no existe o está mal escrita",
    "ZeroDivisionError": "se divide entre 0",
    "RecursionError": "una función se llama a sí misma sin parar",
}

ORDEN = ["tipos", "compuestos", "condicionales", "practica2", "bucles", "bucles2", "practica3",
         "funciones1", "funciones2", "funciones3", "estadistica", "practicaml", "errores",
         "simulacro", "simulacro2"]
EXAMENES.sort(key=lambda e: ORDEN.index(e["id"]))


# =====================================================================
# Verificación
# =====================================================================
def ejecutar(code):
    """Devuelve (salida, nombre_de_error_o_None)."""
    buf = io.StringIO()
    sys.setrecursionlimit(200)
    try:
        with contextlib.redirect_stdout(buf):
            exec(compile(code, "<q>", "exec"), {})
        return buf.getvalue().strip(), None
    except BaseException as e:   # noqa: BLE001
        return buf.getvalue().strip(), type(e).__name__
    finally:
        sys.setrecursionlimit(1000)


def verificar():
    errores = []
    total = 0
    for ex in EXAMENES:
        for p in ex["preguntas"]:
            total += 1
            correcta = p["opts"][p["a"]]
            if len(set(p["opts"])) != len(p["opts"]):
                errores.append(f"{p['id']}: opciones repetidas")
            if p["t"] == "out":
                salida, err = ejecutar(p["code"])
                if err or salida != correcta:
                    errores.append(f"{p['id']}: salida real {salida!r} (error {err}) != {correcta!r}")
            elif p["t"] == "err":
                _, err = ejecutar(p["code"])
                if (err or "Ningún error") != correcta:
                    errores.append(f"{p['id']}: error real {err} != {correcta}")
            elif p["t"] == "fill":
                for i, op in enumerate(p["opts"]):
                    salida, err = ejecutar(p["code"].replace("___", op))
                    ok = err is None and salida == p["expect"]
                    if i == p["a"] and not ok:
                        errores.append(f"{p['id']}: la correcta da {salida!r} ({err})")
                    if i != p["a"] and ok:
                        errores.append(f"{p['id']}: la opción incorrecta {op!r} también funciona")
            completar_por(p, errores)
    return total, errores


def completar_por(p, errores):
    """Junta las explicaciones de por qué falla cada opción incorrecta."""
    p["por"] = {**POR.get(p["id"], {}), **p["por"]}
    for op in p["por"]:
        if op not in p["opts"]:
            errores.append(f"{p['id']}: 'por' explica {op!r}, que no es una opción")
    correcta = p["opts"][p["a"]]
    for i, op in enumerate(p["opts"]):
        if i == p["a"]:
            continue
        if p["t"] == "fill":
            # Se ejecuta el código con esa opción: lo que pasa de verdad.
            salida, err = ejecutar(p["code"].replace("___", op))
            real = f"da {err}" if err else ("no imprime nada" if not salida else f"imprime:\n{salida}")
            extra = p["por"].get(op)
            p["por"][op] = f"Con {op} el código {real}" + (f"\n{extra}" if extra else "")
        elif p["t"] == "err" and op not in p["por"]:
            if op == "Ningún error":
                p["por"][op] = f"Sí hay error: {correcta}."
            else:
                p["por"][op] = f"{op} sale cuando {ERRORES[op]}. Aquí no pasa eso."
        elif op not in p["por"]:
            errores.append(f"{p['id']}: falta explicar por qué {op!r} está mal")


if __name__ == "__main__":
    total, errores = verificar()
    for e in errores:
        print("❌", e)
    if errores:
        sys.exit(1)
    print(f"✔ {total} preguntas verificadas en {len(EXAMENES)} exámenes")

    aqui = pathlib.Path(__file__).parent
    datos = json.dumps(EXAMENES, ensure_ascii=False)
    plantilla = (aqui / "plantilla.html").read_text(encoding="utf8")
    (aqui / "tren.html").write_text(plantilla.replace("/*__DATOS__*/[]", datos), encoding="utf8")
    print("✔ tren.html generado")
