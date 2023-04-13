def run():
    num1 = int(input("un numero: "))
    num2 = int(input("otro numero: "))
    age1 = int(input("edad de Jimmy: "))
    age2 = int(input("edad de John: "))
    age3 = int(input("edad de Tom: "))
    cantidad_cigarros_x_dia = int(input("Ingrese la cantidad de cigarrillos que fuma por día: "))
    tiempo_fumando = int(input("Ingrese la cantidad de años que ha estado fumando: "))
    nombre = input("Tu nombre es: ")
    edad = int(input("Tu edad es: "))
    disciplina = input("Tu disciplina es: ")
    anio_actual = int(input("El año actual es: "))


    # 1. es par?
    print(f'El numero {num1} es par? {not (bool(num1 % 2))}')

    # 2. es mayor?
    print(f'Es Jimmy mayor que John? {bool(age1 > age2)}')

    # 3. viaje de amigos
    print(f'Pueden Jimmy, John y Tom viajar solos? {bool(age1 >= 18 or age2 >= 18 or age3 >= 18)}')

    # 4. peliculas para mayores
    print(f'Pueden todos ellos ver una pelicula +18? {bool(age1 >= 18 and age2 >= 18 and age3 >= 18)}')

    # 5. tienen la misma paridad?
    print(f'Tienen los numeros {num1} y {num2} la misma paridad? {((not (bool(num1 % 2))) and (not (bool(num2 % 2))) or ((bool(num1 % 2)) and (bool(num2 % 2))))}')

    # 6. cuanta vida pierdes fumando?
    cigarrillos_totales = cantidad_cigarros_x_dia * 365 * tiempo_fumando
    minutos_perdidos = cigarrillos_totales * 10
    dias_perdidos = round(minutos_perdidos / (24 * 60))
    print(f'Señor, ha perdido aproximadamente {dias_perdidos} días de vida debido al tabaco.')

    # 7. textos con comillas?
    print("""O'Reilly Media, antes llamada O'Reilly & Associates, 
es una empresa editorial estadounidense fundada y dirigida por 
Tim O'Reilly que está principalmente enfocada a libros de tecnología e informática. 
""")

    # 8. variables concatenadas?
    texto1 = """O'Reilly Media, antes llamada O'Reilly & Associates, 
es una empresa editorial estadounidense fundada y dirigida por """
    texto2 = """
Tim O'Reilly que está principalmente enfocada a libros de tecnología e informática. 
"""
    print(texto1+texto2)

    # 9. texto con variables?
    print(f'{nombre} - {edad} - {disciplina} - {anio_actual}')

    # 10. 'texto con {}?'.format(variables)
    print('{} - {} - {} - {}'.format(nombre, edad, disciplina, anio_actual))
