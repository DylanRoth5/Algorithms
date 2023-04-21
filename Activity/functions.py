from Tools.terminal_help import *
import random
import time
import listas

def fibonacci():
    amount = gint('Cuantos numeros de fibonacci necesitas? ')
    num = 1
    num_min1 = 0
    i = 0
    print(f'{num_min1} -> {num}',end='')
    while i<amount-2:
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

def horse_run():
    index=0
    while True:
        pista_longitud = 1000
        num_caballos = 4
        caballos = []
        todos_en_meta=0
        for i in range(num_caballos):
            caballos.append({'nombre': f'Caballo {i+1}', 'posicion': 0, 'llego': bool(False)})
        carrera_terminada = False
        
        while not carrera_terminada:
            for caballo in caballos:
                time.sleep(0)

                if ((caballo['posicion'] >= pista_longitud) and (caballo['llego'] == False)):
                    todos_en_meta+=1
                    caballo["llego"] = True
                    print(f'{caballo["nombre"]} ha llegado a la meta!')
                elif((caballo['posicion'] >= pista_longitud) and (caballo['llego'] == True)):
                    print(f'{caballo["nombre"]} ha llegado a la meta!')
                else:
                    caballo['posicion'] += random.randint(1, 5)
                    print(f'{caballo["nombre"]} está en el metro {caballo["posicion"]}')

                index+=1
                if(index == 4 and not(todos_en_meta==4)):
                    delete_lines(4)
                    index = 0
                    time.sleep(0.01)

                if todos_en_meta==4:
                    time.sleep(1)
                    caballos.sort(key=lambda x: x['posicion'], reverse=True)
                    print('\nPodio:')
                    for i, c in enumerate(caballos[:4]):
                        time.sleep(0.01)
                        print(f'{i+1}. {c["nombre"]}, metros totales: {c["posicion"]}')
                    carrera_terminada = True
                    break
            
        break


def print_menu_options(options_list):
    for index, option in enumerate(options_list):
        if index == 0:
            print("\n\033[1;34;4m" + option.upper() + "\033[0m\n")
        elif index == len(options_list) - 1:
            print("\033[91m0. " + option + "\033[0m\n")
        else:
            print("\033[92m" + f"{index}. {option}" + "\033[0m")

import os
clear = lambda: os.system('cls')

def buffer():
    buffer = []
    while True:
        clear()
        print_menu_options(listas.printer_menu)
        try:
            select = gint("Ingresa el número de la opción que deseas: ")
        except ValueError:
            print('that is not a number') 
        match select:
            case 1:
                if len(buffer)<20:
                    doc_name = ginp('nombre del documento: ')
                    buffer.append(doc_name)
                    print('agregado documento...')
                else:
                    print('memory capacity reached.')
            case 2:
                if len(buffer)>0:
                    punto = ''
                    for i in range(3):
                        punto+= '.'
                        print(f'Imprimiendo documento{punto}')
                        delete_lines(1)
                        time.sleep(0.5)
                    
                    print()
                    buffer.pop(0)
                else:
                    print('No hay nada para imprimir.')
            case 3:
                print(buffer)
                nada = input('Presiona [Enter] para volver')
            case 0:
                print('Adios')
                break
