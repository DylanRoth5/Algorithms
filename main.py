# Define function to print menu
def print_menu_options(options_list):
    for index, option in enumerate(options_list):
        if index == 0:
            print("\n" + option.upper() + "\n")
        elif index == len(options_list) - 1:
            print("0. " + option + "\n")
        else:
            print(f"{index}. {option}")

menu = ['Menu Principal',
        'Datos Numéricos',
     'Datos Booleanos y Strings',
     'Manipulación de Strings',
     'Funciones, Condicionales, iteración y recursividad'
     'Salir']

numerical_menu = ['Datos Numéricos',
        'Datos Numéricos',
     'Datos Booleanos y Strings',
     'Manipulación de Strings',
     'Funciones, Condicionales, iteración y recursividad'
     'Salir']

boolean_string_menu = ['Datos Booleanos y Strings',
        'Datos Numéricos',
     'Datos Booleanos y Strings',
     'Manipulación de Strings',
     'Funciones, Condicionales, iteración y recursividad'
     'Salir']

string_manipulation_menu = ['Manipulación de Strings',
        'Datos Numéricos',
     'Datos Booleanos y Strings',
     'Manipulación de Strings',
     'Funciones, Condicionales, iteración y recursividad'
     'Salir']

functions_menu = ['Funciones, Condicionales, iteración y recursividad',
        'Datos Numéricos',
     'Datos Booleanos y Strings',
     'Manipulación de Strings',
     'Funciones, Condicionales, iteración y recursividad'
     'Salir']

# Define function to handle user input for sub-menu of option 1 "Datos Numéricos"
def handle_input(choice):
    print("Esta opción aún no ha sido implementada.\n")

# Print menu initially
print_menu_options(menu)

# Keep prompting user for input until they choose to exit
while True:
    choice = input("Ingresa el número de la opción que deseas: ")
    
    if choice == "1":
        # Show sub-menu for option 1 "Datos Numéricos"
        print_menu_options(numerical_menu)
        sub_choice = input("Ingresa el número de la opción que deseas: ")
        handle_input(sub_choice)
    elif choice == "2":
        # Show sub-menu for option 2 "Datos Booleanos y Strings"
        print_menu_options(boolean_string_menu)
        sub_choice = input("Ingresa el número de la opción que deseas: ")
        handle_input(sub_choice)
    elif choice == "3":
        # Show sub-menu for option 3 "Manipulación de Strings"
        print_menu_options(string_manipulation_menu)
        sub_choice = input("Ingresa el número de la opción que deseas: ")
        handle_input(sub_choice)
    elif choice == "4":
        # Show sub-menu for option 4 "Funciones, Condicionales, iteración y recursividad"
        print_menu_options(functions_menu)
        sub_choice = input("Ingresa el número de la opción que deseas: ")
        handle_input(sub_choice)
    elif choice == "0":
        print("¡Adiós!")
        exit()
    else:
        print("Opción inválida. Por favor, intenta nuevamente.")
    
    print_menu_options(menu)
