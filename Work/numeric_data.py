from Tools.terminal_help import *

def get_ABC():
    A = gint('value of A: ')
    B = gint('value of B: ')
    C = gint('value of C: ')
    return A,B,C


def sum_ABC():
    A,B,C = get_ABC()
    print(f'La suma de {A}, {B} y {C} es: {A + B + C}')

def mul_ABC():
    A,B,C = get_ABC()
    print(f'La multiplicacion de {A}, {B} y {C} es: {A * B * C}')


# # 2. multiplicacion
#     print(f'La multiplicacion de A, B y C es: {A * B * C}')

#     # 3. resto de A y B
#     print(f'El resto de A y B es: {A % B}')

#     # 4. A elevado a B
#     print(f'A elevado a B es: {A ** B}')

#     # 5. Raiz cuadrada de C
#     print(f'La Raiz cuadrada de C es: {C ** 0.5}')

#     # 6. hipotenusa usando A y B como los catetos
#     print(f'La Hipotenusa de un triangulo rectangulo con los catetos A y B es: {(A ** 2 + B ** 2) ** 0.5}')