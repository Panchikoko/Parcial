def cargar_matriz_edades(n, m):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            while True:
                entrada = input(f"Ingrese edad para [{i}][{j}]: ")
                if entrada.isdigit():
                    edad = int(entrada)
                    if edad > 0:
                        fila.append(edad)
                        break
                    else:
                        print("Error, ingrese una edad válida mayor a 0")
                else:
                    print("Error, solamente se permiten números positivos")
        matriz.append(fila)
    return matriz
