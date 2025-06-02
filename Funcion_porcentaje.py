def porcentaje_mayores(matriz):
    total = 0
    mayores = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total += 1
            if matriz[i][j] > 60:
                mayores += 1
    if total == 0:
        return 0
    return (mayores * 100) / total
