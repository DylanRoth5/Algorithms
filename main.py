import listas as list
from handling import handle_numeric as HN
from handling import handle_bool_string as HBS
from handling import handle_manipulation as HM 
from handling import handle_functions as HF

# Define function to print menu
def print_menu_options(options_list):
    for index, option in enumerate(options_list):
        if index == 0:
            print("\n\033[1;34;4m" + option.upper() + "\033[0m\n")
        elif index == len(options_list) - 1:
            print("\033[91m0. " + option + "\033[0m\n")
        else:
            print("\033[92m" + f"{index}. {option}" + "\033[0m")

# Activities menu handler
def handle_activity_menu(choice):
    match choice:
        case "1":
            # Show sub-menu for option 1 "Datos Numéricos"
            print_menu_options(list.numerical_menu)
            sub_choice = input("Ingresa el número de la opción que deseas: ")
            HN.handle_input(sub_choice)
        case  "2":
            # Show sub-menu for option 2 "Datos Booleanos y Strings"
            print_menu_options(list.boolean_string_menu)
            sub_choice = input("Ingresa el número de la opción que deseas: ")
            HBS.handle_input(sub_choice)
        case  "3":
            # Show sub-menu for option 3 "Manipulación de Strings"
            print_menu_options(list.string_manipulation_menu)
            sub_choice = input("Ingresa el número de la opción que deseas: ")
            HM.handle_input(sub_choice)
        case  "4":
            # Show sub-menu for option 4 "Funciones, Condicionales, iteración y recursividad"
            print_menu_options(list.functions_menu)
            sub_choice = input("Ingresa el número de la opción que deseas: ")
            HF.handle_input(sub_choice)
        case  "0":
            print("¡Adiós!")
            exit()
        case _:
            print("Opción inválida. Por favor, intenta nuevamente.")
        
    print_menu_options(list.main_menu)

# Practic Work menu handler
def handle_work_menu(choice):
    match choice:
        case "1":
            print('a')
        case  "2":
            print('a')
        case  "3":
            print('a')
        case  "4":
            print('a')
        case  "0":
            print("¡Adiós!")
            exit()
        case _:
            print("Opción inválida. Por favor, intenta nuevamente.")


# Print menu initially
print_menu_options(list.main_menu)

# Keep prompting user for input until they choose to exit
while True:
    choice = input("Ingresa el número de la opción que deseas: ")
    
    match choice:
        case "1":
            print_menu_options(list.activity_menu)
            sub_choice = input("Ingresa el número de la opción que deseas: ")
            handle_activity_menu(sub_choice)
        case  "2":
            print_menu_options(list.boolean_string_menu)
            sub_choice = input("Ingresa el número de la opción que deseas: ")
            HBS.handle_input(sub_choice)
        case  "0":
            print("¡Adiós!")
            exit()
        case _:
            print("Opción inválida. Por favor, intenta nuevamente.")
        
    print_menu_options(list.main_menu)
