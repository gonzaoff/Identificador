import random
from itertools import combinations

def es_multiplo(n, base):
    # Verifica si un número es múltiplo de otro.
    return n % base == 0

def generar_combinaciones(numeros, r, bases):
    # Genera combinaciones de r números que sumen un múltiplo de alguna de las bases especificadas.
    combinaciones_validas = []
    for combinacion in combinations(numeros, r):
        if any(es_multiplo(sum(combinacion), base) for base in bases):
            combinaciones_validas.append(combinacion)
    return combinaciones_validas

def seleccionar_grupo_disponible(disponibles):
    # Selecciona un grupo de 4 combinaciones disponibles al azar.
    if len(disponibles) < 4:
        print("No hay suficientes combinaciones disponibles para seleccionar un grupo de 4.")
        return None

    grupo = random.sample(disponibles, 4)
    return grupo

def manejar_ocupacion(disponibles, ocupados):
    # Maneja la ocupación de un grupo de 4 combinaciones y solicita al usuario un nombre para el grupo.
    grupo = seleccionar_grupo_disponible(disponibles)
    if grupo is None:
        return

    nombre = input("Ingresa un nombre para este grupo de combinaciones: ")

    if any(nombre == clave for clave in ocupados.keys()):
        print(f"El nombre '{nombre}' ya está en uso. Por favor, elige otro nombre.")
        return

    ocupados[nombre] = grupo
    for combinacion in grupo:
        disponibles.remove(combinacion)
    print(f"\nGrupo de combinaciones {grupo} ocupado exitosamente con el nombre '{nombre}'.")
    mostrar_combinaciones(list(ocupados.items()), "Ocupadas")  # Mostrar combinaciones ocupadas con nombres

def mostrar_combinaciones(combinaciones, tipo):
    # Muestra las combinaciones ocupadas con enumeración.
    print(f"\n{tipo}:")
    for idx, (nombre, comb) in enumerate(combinaciones):
        print(f"{idx + 1}: {nombre} -> {comb}")

def manejar_combinaciones(disponibles, ocupados):
    # Muestra el menú y gestiona las opciones del usuario.
    while True:
        print("\nOpciones:")
        print("1: Ocupa un grupo de 4 combinaciones al azar")
        print("2: Mostrar combinaciones ocupadas")
        print("0: Salir")
        
        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion == 0:
                print("Saliendo del programa...")
                break
            elif opcion == 1:
                manejar_ocupacion(disponibles, ocupados)
            elif opcion == 2:
                mostrar_combinaciones(list(ocupados.items()), "Ocupadas")  # Mostrar con nombres
            else:
                print("Opción no válida. Intenta nuevamente.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")

# Parámetros
numeros = range(1, 10)  # Rango de números del 1 al 9
r = 4  # Número de elementos en cada combinación
bases = [6, 8]  # Múltiplos deseados (6 y 8)

# Generar combinaciones válidas
combinaciones_validas = generar_combinaciones(numeros, r, bases)

# Listas de combinaciones disponibles y ocupadas
combinaciones_disponibles = combinaciones_validas.copy()
combinaciones_ocupadas = {}

# Manejar combinaciones ingresadas por el usuario
manejar_combinaciones(combinaciones_disponibles, combinaciones_ocupadas)
