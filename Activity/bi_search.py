# Ejercicios: 
# 1) sumatoria de cada fila 
# 2) sumatoria de cada columna
# 3) calcular los valores de x, y y z del siguiente 
#    sistema de ecuaciones lineales con 3 incognitas.
#   3x - 2y - z = 12
#   x + 3y + z = -4
#   2x + 2y - 4z = 6
#   la solucion es (x, y, z)=(3, -2, -1).

matrix = [[3,-2,-1,12],[1,3,1,-4],[2,2,-4,6]]
print("\nmatrix")
filas_sum = []
sum_items = 0
for fila in matrix:
    print(fila)
    for item in fila:
        sum_items += item
    filas_sum.append(sum_items)
    sum_items = 0

print('\nsumatoria de filas')
print(filas_sum)

inverted_matrix = []
fila_min = []
for loop in range(len(matrix[1])):
    inverted_matrix.append(fila_min)
    for item in range(len(matrix)):
        fila_min.append(int(matrix[item][loop]))
    fila_min = []
inverted_matrix.append(fila_min)
inverted_matrix.pop(-1)

print('\ntransposed matrix')
for fila in inverted_matrix:
    print(fila)

print('\nsumatoria de columnas')
inv_filas_sum = []
inv_sum_items = 0
for fila in inverted_matrix:
    for item in fila:
        inv_sum_items += item
    inv_filas_sum.append(inv_sum_items)
    inv_sum_items = 0

print(inv_filas_sum)

