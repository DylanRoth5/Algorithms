def ginp(text):
    value = input(text)
    return value

def gint(text):
    value = int(input(text))
    return value

def gf(text):
    value = float(input(text))
    return value

def get_ABC():
    A = gint('value of A: ')
    B = gint('value of B: ')
    C = gint('value of C: ')
    return A,B,C

def get_ABCD(text1,text2,text3,text4):
    A = gint(text1)
    B = gint(text2)
    C = gint(text3)
    D = gint(text4)
    return A,B,C,D

def get_ABC(text1,text2,text3):
    A = gint(text1)
    B = gint(text2)
    C = gint(text3)
    return A,B,C

def getf_ABC():
    A = gf('value of A: ')
    B = gf('value of B: ')
    C = gf('value of C: ')
    return A,B,C

def get_AB():
    A = gint('value of A: ')
    B = gint('value of B: ')
    return A,B

def get_AB(text1,text2):
    A = gint(text1)
    B = gint(text2)
    return A,B

import sys

def delete_last_line():
    # cursor up one line
    sys.stdout.write('\x1b[1A')
    # delete last line
    sys.stdout.write('\x1b[2K')

def delete_lines(amount):
    for i in range(amount):
        delete_last_line()  

import os
clear = lambda: os.system('cls')

def print_menu_options(options_list):
    clear()
    for index, option in enumerate(options_list):
        if index == 0:
            print("\033[1;34;4m" + option.upper() + "\033[0m\n")
        elif index == len(options_list) - 1:
            print("\033[91m0. " + option + "\033[0m\n")
        else:
            print("\033[92m" + f"{index}. {option}" + "\033[0m")

import datetime

def get_date():
    year = int(input('Enter a year'))
    month = int(input('Enter a month'))
    day = int(input('Enter a day'))
    date = datetime.date(year, month, day)
    return date