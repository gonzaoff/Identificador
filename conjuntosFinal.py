from itertools import combinations

def es_multiplo(n, base):
    """
    Verifica si un número es múltiplo de otro.
    """
    return n % base == 0

def generar_combinaciones(numeros, r, bases):
    """
    Genera combinaciones de r números que sumen un múltiplo de alguna de las bases especificadas.
    """
    combinaciones_validas = []
    for combinacion in combinations(numeros, r):
        if any(es_multiplo(sum(combinacion), base) for base in bases):
            combinaciones_validas.append(combinacion)
    return combinaciones_validas

def combinar_grupos(grupos, r):
    """
    Encuentra todas las formas de combinar r grupos de combinaciones válidas.
    """
    if r == 1:
        return [[grupo] for grupo in grupos]
    
    combinaciones_grupos = []
    for i in range(len(grupos)):
        for resto in combinar_grupos(grupos[i+1:], r-1):
            combinaciones_grupos.append([grupos[i]] + resto)
    
    return combinaciones_grupos

def mostrar_combinaciones(combinaciones, tipo, indices=None):
    """
    Muestra las combinaciones disponibles u ocupadas con enumeración.
    """
    print(f"\n{tipo} combinaciones:")
    for idx, comb in enumerate(combinaciones):
        if indices is None or idx + 1 in indices:
            print(f"{idx + 1}: {comb}")

def manejar_ocupacion(disponibles, ocupados, primera_vez, indices_disponibles):
    """
    Maneja la ocupación de combinaciones, permitiendo al usuario seleccionar combinaciones una por una.
    """
    if primera_vez:
        mostrar_combinaciones(disponibles, "Disponibles", indices_disponibles)  # Mostrar solo la primera vez

    while True:
        try:
            indice = int(input("\nIngresa el número de la combinación que deseas ocupar (0 para cancelar): "))
            if indice == 0:
                break
            if not (1 <= indice <= len(disponibles)):
                raise ValueError
            combinacion = disponibles[indice - 1]
            if combinacion in ocupados:
                print("Esta combinación ya está ocupada.")
            else:
                # Guardar la combinación con el número ingresado
                ocupados.append((indice, combinacion))
                # Eliminar la combinación de la lista de disponibles
                disponibles.remove(combinacion)
                indices_disponibles.remove(indice)  # Eliminar el índice de la lista de índices disponibles
                print(f"\nCombinación {combinacion} ocupada exitosamente.")
                mostrar_combinaciones(ocupados, "Ocupadas")
        except ValueError:
            print(f"Entrada inválida. Debes ingresar un número entre 1 y {len(disponibles)}, o 0 para cancelar.")

def manejar_combinaciones(disponibles, ocupados):
    """
    Muestra el menú y gestiona las opciones del usuario.
    """
    primera_vez = True  # Bandera para la primera vez que se selecciona la opción de ocupar combinación
    indices_disponibles = list(range(1, len(disponibles) + 1))  # Lista de índices disponibles

    while True:
        print("\nOpciones:")
        print("1: Ocupa una combinación")
        print("2: Mostrar combinaciones disponibles")
        print("3: Mostrar combinaciones ocupadas")
        print("0: Salir")
        
        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion == 0:
                print("Saliendo del programa...")
                break
            elif opcion == 1:
                manejar_ocupacion(disponibles, ocupados, primera_vez, indices_disponibles)
                primera_vez = False  # Después de la primera vez, se establece la bandera en False
            elif opcion == 2:
                mostrar_combinaciones(disponibles, "Disponibles", indices_disponibles)
            elif opcion == 3:
                mostrar_combinaciones(ocupados, "Ocupadas")
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

# Combinar 4 grupos de las combinaciones válidas
todas_las_combinaciones_de_grupos = combinar_grupos(combinaciones_validas, 4)

# Listas de combinaciones disponibles y ocupadas
combinaciones_disponibles = todas_las_combinaciones_de_grupos.copy()
combinaciones_ocupadas = []

# Manejar combinaciones ingresadas por el usuario
manejar_combinaciones(combinaciones_disponibles, combinaciones_ocupadas)
