import listas as list
from handling.handle_numeric import *
from handling.handle_bool_string import *
from handling.handle_manipulation import *
from handling.handle_functions import *

# Define function to print menu
def print_menu_options(options_list):
    for index, option in enumerate(options_list):
        if index == 0:
            print("\n\033[1;34;4m" + option.upper() + "\033[0m\n")
        elif index == len(options_list) - 1:
            print("\033[91m0. " + option + "\033[0m\n")
        else:
            print("\033[92m" + f"{index}. {option}" + "\033[0m")

# Define function to handle user input for sub-menu of option 1 "Datos Numéricos"
def handle_input(choice):
    print("\nEsta opción aún no ha sido implementada.\n")

# Print menu initially
print_menu_options(list.menu)

# Keep prompting user for input until they choose to exit
while True:
    choice = input("Ingresa el número de la opción que deseas: ")
    
    match choice:
        case "1":
            # Show sub-menu for option 1 "Datos Numéricos"
            print_menu_options(list.numerical_menu)
            sub_choice = input("Ingresa el número de la opción que deseas: ")
            handle_input(sub_choice)
        case  "2":
            # Show sub-menu for option 2 "Datos Booleanos y Strings"
            print_menu_options(list.boolean_string_menu)
            sub_choice = input("Ingresa el número de la opción que deseas: ")
            handle_input(sub_choice)
        case  "3":
            # Show sub-menu for option 3 "Manipulación de Strings"
            print_menu_options(list.string_manipulation_menu)
            sub_choice = input("Ingresa el número de la opción que deseas: ")
            handle_input(sub_choice)
        case  "4":
            # Show sub-menu for option 4 "Funciones, Condicionales, iteración y recursividad"
            print_menu_options(list.functions_menu)
            sub_choice = input("Ingresa el número de la opción que deseas: ")
            handle_input(sub_choice)
        case  "0":
            print("¡Adiós!")
            exit()
        case _:
            print("Opción inválida. Por favor, intenta nuevamente.")
        
    print_menu_options(list.menu)
