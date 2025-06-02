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



from Funcion_porcentaje import porcentaje_mayores
from Matriz_edades import cargar_matriz_edades

matriz = None

while True:
    print("\nMENU")
    print("1 = Cargar matriz de las edades")
    print("2 = Calcular porcentaje de los mayores")
    print("3 = Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        n = 0
        m = 0
        while n <= 0:
            n_string = input("Ingrese el número de filas: ")
            if n_string.isdigit() and int(n_string) > 0:
                n = int(n_string)
            else:
                print("Error, tiene que ser un número mayor a 0")
                
        while m <= 0:
            m_string = input("Ingrese el número de columnas: ")
            if m_string.isdigit() and int(m_string) > 0:
                m = int(m_string)
            else:
                print("Error, tiene que ser un número mayor a 0")

        matriz = cargar_matriz_edades(n, m)
        print("Matriz cargada exitosamente!")

    elif opcion == "2":
        if matriz is None:
            print("Primero debe cargar la matriz de edades (opción 1).")
        else:
            porcentaje = porcentaje_mayores(matriz)
            print(f"Porcentaje de mayores de 60: {porcentaje}%")

    elif opcion == "3":
        print("Adios!")
        break

    else: 
        print("Opción no válida. Por favor ingrese: 1, 2 o 3.")