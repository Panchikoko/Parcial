# PARTE 2 – EJERCICIO PRÁCTICO
# Contexto: Se desea analizar los datos de una población organizada en
# una matriz de n filas por m columnas, donde cada celda representa la
# edad de una persona.
# Requisitos Generales para Todos los Puntos:
# - Se deben modularizar todas las operaciones. No se permite resolver
# todo en el main.
# - No está permitido el uso de funciones propias de Python como max,
# min, sum, enumerate, etc.
# - La validación debe hacerse en la función de carga, verificando que
# cada edad ingresada sea mayor a 0.
# - Se debe implementar un menú con opciones para ejecutar cada punto
# de forma separada.
# - Usar estructuras adecuadas, acumuladores, contadores y recorrido
# doble.
# - Nombrar las funciones tal como se indican a continuación.

# 1 – Función cargar_matriz_edades(): Recibe dos enteros n y m y
# permite cargar n x m edades válidas mayores a 0. La validación debe
# hacerse dentro de esta función.
# 2 – Función porcentaje_mayores(): Calcula qué porcentaje del total de
# datos representa personas mayores de 60 años. Utilizar contadores y
# acumuladores.
# 3 – Función menor_edad(): Determina la edad mínima de toda la matriz
# (sin usar min) y retorna ese valor junto con todas las posiciones (fila,
# columna) donde aparece.
# 4 – Función buscar_edad(): Recibe una matriz y una edad determinada,
# y retorna todas las posiciones donde aparece esa edad exacta.*


# Importación de funciones desde otros módulos
from Funcion_porcentaje import porcentaje_mayores  # Importa función para calcular porcentaje de mayores
from Matriz_edades import cargar_matriz_edades    # Importa función para cargar la matriz de edades
from Menor_Edad import menor_edad                 # Importa función para encontrar edad mínima
from Buscar_edad import buscar_edad               # Importa función para buscar edades específicas

# Variable global para almacenar la matriz de edades
matriz = None  # Inicializada como None al comienzo del programa

# Bucle principal del menú
while True:
    # Mostrar opciones del menú
    print("\nMENU")
    print("1 = Cargar matriz de las edades")
    print("2 = Calcular porcentaje de los mayores")
    print("3 = Buscar la edad minima de toda la matriz")
    print("4 = Buscar una edad especifica")
    print("5 = Salir")

    # Solicitar opción al usuario
    opcion = input("Seleccione una opción: ")

    # Opción 1: Cargar matriz de edades
    if opcion == "1":
        n = 0  # Inicializar número de filas
        m = 0  # Inicializar número de columnas
        
        # Validar entrada para número de filas
        while n <= 0:
            n_string = input("Ingrese el número de filas: ")
            if n_string.isdigit() and int(n_string) > 0:  # Verificar si es número positivo
                n = int(n_string)  # Convertir a entero
            else:
                print("Error, tiene que ser un número mayor a 0")
                
        # Validar entrada para número de columnas
        while m <= 0:
            m_string = input("Ingrese el número de columnas: ")
            if m_string.isdigit() and int(m_string) > 0:  # Verificar si es número positivo
                m = int(m_string)  # Convertir a entero
            else:
                print("Error, tiene que ser un número mayor a 0")

        # Cargar matriz con las dimensiones especificadas
        matriz = cargar_matriz_edades(n, m)  # Llamar a función de carga
        print("Matriz cargada exitosamente!")

    # Opción 2: Calcular porcentaje de mayores de 60
    elif opcion == "2":
        if matriz is None:  # Verificar si la matriz está cargada
            print("Primero debe cargar la matriz de edades (opción 1).")
        else:
            porcentaje = porcentaje_mayores(matriz)  # Calcular porcentaje
            print(f"Porcentaje de mayores de 60: {porcentaje}%")  # Mostrar resultado

    # Opción 3: Encontrar la edad mínima
    elif opcion =="3":
        if matriz is None:  # Verificar si la matriz está cargada
            print("Primero debe cargar la matriz de edades (Opcion 1).")
        else:
            edad_min, posiciones = menor_edad(matriz)  # Obtener edad mínima y posiciones
            print("La menor edad es {edad_min} y aparece en:")  # Mostrar edad mínima
            for pos in posiciones:  # Recorrer todas las posiciones
                print(" - Fila {pos[0]+1}, Columna {pos[1]+1}")  # Mostrar cada posición

    # Opción 4: Buscar edad específica
    elif opcion =="4":
        if matriz is None:  # Verificar si la matriz está cargada
            print("Primero debe cargar la matriz de edades (opción 1).")
        else:
            edad_buscar = input("Ingrese la edad que está buscando: ")
            if edad_buscar.isdigit():  # Verificar si la entrada es numérica
                edad_buscar = int(edad_buscar)  # Convertir a entero
                posiciones = buscar_edad(matriz, edad_buscar)  # Buscar edad en matriz
                if not posiciones:  # Si no se encontró la edad
                    print("La edad {edad_buscar} no aparece en la matriz")
                else:  # Si se encontró la edad
                    print("La edad {edad_buscar} aparece en:")
                    for pos in posiciones:  # Recorrer posiciones encontradas
                        print(" - Fila {pos[0]+1}, Columna {pos[1]+1}")
            else:
                print("Error: Debe ingresar un número entero positivo")

    # Opción 5: Salir del programa
    elif opcion == "5":
        print("Adios!")  # Mensaje de despedida
        break  # Salir del bucle while

    # Opción no válida
    else: 
        print("Opción no válida. Por favor ingrese: 1, 2 o 3.")  # Mensaje de error