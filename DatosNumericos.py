import cmath
import math


def run():
    A = int(input("A : "))
    B = int(input("B : "))
    C = int(input("C : "))

    # 1. suma
    print(f'La suma de A, B y C es: {A + B + C}')

    # 2. multiplicacion
    print(f'La multiplicacion de A, B y C es: {A * B * C}')

    # 3. resto de A y B
    print(f'El resto de A y B es: {A % B}')

    # 4. A elevado a B
    print(f'A elevado a B es: {A ** B}')

    # 5. Raiz cuadrada de C
    print(f'La Raiz cuadrada de C es: {C ** 0.5}')

    # 6. hipotenusa usando A y B como los catetos
    print(f'La Hipotenusa de un triangulo rectangulo con los catetos A y B es: {(A ** 2 + B ** 2) ** 0.5}')

    # 7. siendo A, B y C coeficientes de la resolvente, calcule las raices (0 comprension del ejercicio tengo)

    # calcular la raíz cuadrada del discriminante
    discriminante = cmath.sqrt(B ** 2 - 4 * A * C)

    # calcular las raíces
    raiz1 = (-B + discriminante) / (2 * A)
    raiz2 = (-B - discriminante) / (2 * A)

    # redondear la parte real e imaginaria de cada raíz
    raiz1_real = round(raiz1.real, 2)
    raiz1_imag = round(raiz1.imag, 2)
    raiz2_real = round(raiz2.real, 2)
    raiz2_imag = round(raiz2.imag, 2)

    # imprimir las raíces
    print("Las raíces son:")
    print(f"{raiz1_real} + {raiz1_imag}j")
    print(f"{raiz2_real} + {raiz2_imag}j")

    # 8. Encuentra la medida de un cateto conociendo la medida de la hipotenusa y el otro cateto
    print(f'Teniendo la hipotenusa C={C} y el cateto A={A} el cateto B mide: {math.sqrt(C**2 - A**2)}')