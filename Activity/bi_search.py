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
print("")


a = (matrix[0][0]*matrix[1][1]*matrix[2][2])
b = (matrix[0][1]*matrix[1][2]*matrix[2][0])
c = (matrix[0][2]*matrix[1][0]*matrix[2][1])


d = (matrix[0][2]*matrix[1][1]*matrix[2][0])
e = (matrix[0][0]*matrix[1][2]*matrix[2][1])
f = (matrix[0][1]*matrix[1][0]*matrix[2][2])


determinante = (a+b+c)-(d+e+f)
print(f'({a}+{b}+{c})-({d}+{e}+{f}) = {determinante}')

a = (matrix[0][3]*matrix[1][1]*matrix[2][2])
b = (matrix[0][1]*matrix[1][2]*matrix[2][3])
c = (matrix[0][2]*matrix[1][3]*matrix[2][1])


d = (matrix[0][2]*matrix[1][1]*matrix[2][3])
e = (matrix[0][3]*matrix[1][2]*matrix[2][1])
f = (matrix[0][1]*matrix[1][3]*matrix[2][2])


det_x = (a+b+c)-(d+e+f)
print(f'({a}+{b}+{c})-({d}+{e}+{f}) = {det_x}')

a = (matrix[0][0]*matrix[1][3]*matrix[2][2])
b = (matrix[0][3]*matrix[1][2]*matrix[2][0])
c = (matrix[0][2]*matrix[1][0]*matrix[2][3])


d = (matrix[0][2]*matrix[1][3]*matrix[2][0])
e = (matrix[0][0]*matrix[1][2]*matrix[2][3])
f = (matrix[0][3]*matrix[1][0]*matrix[2][2])


det_y = (a+b+c)-(d+e+f)
print(f'({a}+{b}+{c})-({d}+{e}+{f}) = {det_y}')

a = (matrix[0][0]*matrix[1][1]*matrix[2][3])
b = (matrix[0][1]*matrix[1][3]*matrix[2][0])
c = (matrix[0][3]*matrix[1][0]*matrix[2][1])


d = (matrix[0][3]*matrix[1][1]*matrix[2][0])
e = (matrix[0][0]*matrix[1][3]*matrix[2][1])
f = (matrix[0][1]*matrix[1][0]*matrix[2][3])


det_z = (a+b+c)-(d+e+f)
print(f'({a}+{b}+{c})-({d}+{e}+{f}) = {det_z}')


print()
X = det_x/determinante
Y = det_y/determinante
Z = det_z/determinante

print(f'(X,Y,Z)=({X},{Y},{Z})')
from fractions import Fraction

X = Fraction(X).limit_denominator()
Y = Fraction(Y).limit_denominator()
Z = Fraction(Z).limit_denominator()

print(f'(X,Y,Z)=({X},{Y},{Z})')
print()