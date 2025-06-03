def buscar_edad(matriz, edad):
    posicion = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == edad:
                posicion.append((i, j))
    return posicion