from Tools.terminal_help import *
import random
import time

def fibonacci():
    amount = gint('Cuantos numeros de fibonacci necesitas? ')
    num = 1
    num_min1 = 0
    i = 0
    print(f'{num_min1} -> {num}',end='')
    while i<amount:
        num+=num_min1
        num_min1=num-num_min1
        print(f' -> {num}',end='')
        i+=1

def triangle_type():
    A,B,C = get_ABC('lado 1: ','lado 2: ','lado 3: ')
    if((A < B + C ) and (B < A + C ) and (C < B + A )):
        if(A==B==C):
            print('es equilatero')
        elif((A!=B) and (B!=C) and (A!=C)):
            print('es escaleno')
        elif((not(A==B==C)) and ((A==B) or (B==C) or (A==C))):
            print('es isoceles')
    else:
        print('Eso no puede ser un triangulo')


def roman_numbers():
    num = gint('numero: ')
    roman=''

    while(num>=1000):
        roman+= 'M'
        num-=1000

    if((num>=900) and (num<1000)):
        roman+= 'CM'
        num-=900
    elif((num>=500) and (num<900)):
        roman+= 'D'
        num-=500
    elif((num>=400) and (num<500)):
        roman+= 'CD'
        num-=400

    while(num>=100):
        roman+= 'C'
        num-=100

    if((num>=90) and (num<100)):
        roman+= 'XC'
        num-=90
    elif((num>=50) and (num<90)):
        roman+= 'L'
        num-=50
    elif((num>=40) and (num<50)):
        roman+= 'XL'
        num-=40
    
    while(num>=10):
        roman+= 'X'
        num-=10

    if((num==9)):
        roman+= 'IX'
        num-=9
    elif((num>=5) and (num<9)):
        roman+= 'V'
        num-=5
    elif((num==4)):
        roman+= 'IV'
        num-=4
    

    while((num>=1)):
        roman+= 'I'
        num-=1
    
    print(roman)
        



def arithmetic_or_weighted_average():
    A,B,C = get_ABC('nota 1: ','nota 2: ','nota 3: ')
    print(f'Media aritmetica: {(A+B+C)/3}')
    print(f'Promedio ponderado: {A*0.5+B*0.3+C*0.2}')


def factorial_impar():
    num = gint('numero impar: ')
    while(not(bool(num % 2))):
        num = gint('numero impar: ')
    result=1
    print(f'{num}! = ',end='')
    for i in range(num):
        if(not(bool(i % 2))):
            if(i==0):
                print(f'',end='')
            elif(i==2):
                print(f'{result}',end='')
            else:
                print(f' * {result}',end='')
            result = result*(i+1)
    
    print(f' * {num} = {result}',end='')

def digit_sum():
    num = ginp('nuero: ')
    sum = 0 
    for digit in num:
        sum += int(digit)
    
    print(f'la suma de los digitos es: {sum}')

import sys

def delete_last_line():
    # cursor up one line
    sys.stdout.write('\x1b[1A')
    # delete last line
    sys.stdout.write('\x1b[2K')

def what():
    delete_last_line()
    delete_last_line()
    delete_last_line()
    delete_last_line()

def horse_run():
    index=0
    while True:
        pista_longitud = 1000
        num_caballos = 4
        caballos = []
        for i in range(num_caballos):
            caballos.append({'nombre': f'Caballo {i+1}', 'posicion': 0})
        carrera_terminada = False
        
        while not carrera_terminada:
            for caballo in caballos:
                time.sleep(0)
                index+=1
                caballo['posicion'] += random.randint(1, 5)
                print(f'{caballo["nombre"]} está en el metro {caballo["posicion"]}')
                if(index == 4):
                    what()
                    index = 0                
                    time.sleep(0.5)

                if caballo['posicion'] >= pista_longitud:
                    print(f'{caballo["nombre"]} ha llegado a la meta!')
                    caballos.sort(key=lambda x: x['posicion'], reverse=True)
                    print('Podio:')
                    for i, c in enumerate(caballos[:3]):
                        print(f'{i+1}. {c["nombre"]}')
                    carrera_terminada = True
                    break
            

        continuar = input('¿Quieres iniciar otra carrera? (s/n): ')
        if continuar.lower() != 's':
            break
