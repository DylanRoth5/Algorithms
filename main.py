import listas as list
from handling import handle_numeric
from handling import handle_bool_string
from handling import handle_manipulation
from handling import handle_functions
from WorkPractic import supermarket as SM
from Tools import terminal_help as help
import os
clear = lambda: os.system('cls')

# Activities menu handler
def handle_activity_menu():
    while True:
        help.print_menu_options(list.activity_menu)
        choice = input("Ingresa el número de la opción que deseas: ")
            
        match choice:
            case "1":
                clear()
                # Show sub-menu for option 1 "Datos Numéricos"
                handle_numeric.handle_input()
            case  "2":
                clear()
                # Show sub-menu for option 2 "Datos Booleanos y Strings"
                handle_bool_string.handle_input()
            case  "3":
                clear()
                # Show sub-menu for option 3 "Manipulación de Strings"
                handle_manipulation.handle_input()
            case  "4":
                clear()
                # Show sub-menu for option 4 "Funciones, Condicionales, iteración y recursividad"
                handle_functions.handle_input()
            case  "0":
                break
            case _:
                print("Opción inválida. Por favor, intenta nuevamente.")

# Practic Work menu handler
def handle_work_menu():
    while True:
        help.print_menu_options(list.work_menu)
        choice = input("Ingresa el número de la opción que deseas: ")
            
        match choice:
            case "1":
                clear()
                SM.open_market()
                select = input('\nPress any letter to go back to menu: ')
            case  "2":
                clear()
                print('a')
                select = input('\nPress any letter to go back to menu: ')
            case  "3":
                clear()
                print('a')
                select = input('\nPress any letter to go back to menu: ')
            case  "4":
                clear()
                print('a')
                select = input('\nPress any letter to go back to menu: ')
            case  "0":
                break
            case _:
                print("Opción inválida. Por favor, intenta nuevamente.")


# Print menu initially
help.print_menu_options(list.main_menu)

# Keep prompting user for input until they choose to exit
while True:
    
    choice = input("Ingresa el número de la opción que deseas: ")
    
    match choice:
        case "1":
            handle_activity_menu()
        case  "2":
            handle_work_menu()
        case  "0":
            print("¡Adiós!")
            exit()
        case _:
            print("Opción inválida. Por favor, intenta nuevamente.")
        
    help.print_menu_options(list.main_menu)
