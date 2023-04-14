from Tools.terminal_help import *

def is_pair():
    num = gint('Un numero: ')
    print(f'El numero {num} es par? {not (bool(num % 2))}')

def is_older():
    age1, age2 = get_AB('edad 1: ','edad 2: ')
    print(f'Es Jimmy mayor que John? {bool(age1 > age2)}')

def travel_alone():
    age1,age2,age3 = get_ABC('Jimmy: ', 'John: ', 'Tom: ')
    print(f'Pueden Jimmy, John y Tom viajar solos? {bool(age1 >= 18 or age2 >= 18 or age3 >= 18)}')

def r_rated():
    age1,age2,age3 = get_ABC('Jimmy: ', 'John: ', 'Tom: ')
    print(f'Pueden todos ellos ver una pelicula +18? {bool(age1 >= 18 and age2 >= 18 and age3 >= 18)}')

def same_parity():
    num1, num2 = get_AB('numero 1: ','numero 2: ')
    print(f'Tienen los numeros {num1} y {num2} la misma paridad? {((not (bool(num1 % 2))) and (not (bool(num2 % 2))) or ((bool(num1 % 2)) and (bool(num2 % 2))))}')

def time_lost():
    cantidad_cigarros_x_dia, tiempo_fumando = get_AB('cantidad cigarros x dia: ','tiempo fumando: ')
    cigarrillos_totales = cantidad_cigarros_x_dia * 365 * tiempo_fumando
    minutos_perdidos = cigarrillos_totales * 10
    dias_perdidos = round(minutos_perdidos / (24 * 60))
    print(f'Señor, ha perdido aproximadamente {dias_perdidos} días de vida debido al tabaco.')

def text_quote():
    print("""O'Reilly Media, antes llamada O'Reilly & Associates, 
es una empresa editorial estadounidense fundada y dirigida por 
Tim O'Reilly que está principalmente enfocada a libros de tecnología e informática. 
""")

def conected_var():
    texto1 = """O'Reilly Media, antes llamada O'Reilly & Associates, 
es una empresa editorial estadounidense fundada y dirigida por """
    texto2 = """
Tim O'Reilly que está principalmente enfocada a libros de tecnología e informática. 
"""
    print(texto1+texto2)

def var_text():
    nombre,edad,disciplina,anio_actual = get_ABCD('nombre: ', 'edad: ', 'disciplina: ', 'año actual: ')
    print(f'{nombre} - {edad} - {disciplina} - {anio_actual}')


def formatted_text():
    nombre,edad,disciplina,anio_actual = get_ABCD('nombre: ', 'edad: ', 'disciplina: ', 'año actual: ')
    print('{} - {} - {} - {}'.format(nombre, edad, disciplina, anio_actual))
