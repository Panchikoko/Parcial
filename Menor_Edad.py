def menor_edad(matriz):
    if not matriz or not matriz[0]:
        return None, []
    
    min_edad = matriz [0] [0]
    posiciones = [(0, 0)]

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz [i] [j] < min_edad:
                min_edad = matriz[i][j]
                posiciones = [(i, j)]
            elif matriz [i] [j] == min_edad:
                if (i, j) not in posiciones:
                    posiciones.append ((i, j))

    return min_edad, posiciones