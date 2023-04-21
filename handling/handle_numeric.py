from Activity.numeric_data import *
from Tools import terminal_help as help

# Define function to handle user input for sub-menu of option 1 "Datos Numéricos"
def handle_input():
    while True:
        help.print_menu_options(list.numerical_menu)
        sub_choice = input("\nIngresa el número de la opción que deseas: ")
        
        match sub_choice:
            case '1':
                sum_ABC()
            case '2':
                mul_ABC()
            case '3':
                rest_AB()
            case '4':
                power_AB()
            case '5':
                root_C()
            case '6':
                pitagoras_AB()
            case '7':
                Quadratic_formula()
            case '8':
                wardrobe()
            case '0':
                break
            case _:
                print("Opción inválida. Por favor, intenta nuevamente.")