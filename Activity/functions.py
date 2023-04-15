from Tools.terminal_help import *

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
    print()


def roman_numbers():
    print()


def arithmetic_or_weighted_average():
    print()


def factorial():
    print()


def digit_sum():
    print()


def horse_run():
    print()

