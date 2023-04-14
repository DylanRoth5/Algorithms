from math import sqrt
from Tools.terminal_help import *

def sum_ABC():
    A,B,C = get_ABC()
    print(f'La suma de {A}, {B} y {C} es: {A + B + C}')

def mul_ABC():
    A,B,C = get_ABC()
    print(f'La multiplicacion de {A}, {B} y {C} es: {A * B * C}')

def rest_AB():
    A,B = get_AB()
    print(f'El resto de {A} y {B} es: {A % B}')

def power_AB():
    A,B = get_AB()
    print(f'{A} elevado a {B} es: {A ** B}')

def root_C():
    C = gint()
    print(f'La Raiz cuadrada de {C} es: {C ** 0.5}')

def pitagoras_AB():
    A,B = get_AB()
    print(f'La Hipotenusa de un triangulo rectangulo con los catetos A y B es: {(A ** 2 + B ** 2) ** 0.5}')

def Quadratic_formula():
    A,B,C = getf_ABC()
    # quadratic formula -> (-b±√(b²-4ac))/(2a)
    # calculamos el discriminante
    discriminante =  B * B - 4 * A * C

    if discriminante < 0: # comprobamos si no existen soluciones reales
        print(f'La ecuación no tiene soluciones reales.')
    else:
        raiz = sqrt(discriminante)      # calculamos la raíz
        x_1 = (-B + raiz) / (2 * A)     # calculamos una primera solución
        if discriminante != 0:          # comprobamos si hay otra solución
            x_2 = (-B - raiz) / (2 * A) # calculamos la segunda solución
            print(f'Las soluciones son {x_1} y {x_2}.') # mostramos las dos soluciones
        else:
            print(f'La única solución es x = {x_1}') # mostramos la única solución

def wardrobe():
    A,B = get_AB('altura de la pared: ','profundidad del ropero: ')
    print(f'La Hipotenusa de un triangulo rectangulo con los catetos A y B es: {(A ** 2 - B ** 2) ** 0.5}')