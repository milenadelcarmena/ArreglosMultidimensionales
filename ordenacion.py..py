def ordenar_fila(matriz, fila):
    # Usando Bubble Sort para ordenar la fila específica
    for j in range(len(matriz[fila]) - 1):
        for k in range(len(matriz[fila]) - 1 - j):
            if matriz[fila][k] > matriz[fila][k + 1]:
                matriz[fila][k], matriz[fila][k + 1] = matriz[fila][k + 1], matriz[fila][k]

# Ejemplo de matriz 3x3
matriz = [
    [9, 1, 0],
    [3, 8, 5],
    [6, 4, 7]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la segunda fila (índice 1)
ordenar_fila(matriz, 1)

print("\nMatriz después de ordenar la fila 1:")
for fila in matriz:
    print(fila)