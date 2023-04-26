from Activity.functions import *
from Tools import terminal_help as help
import listas as list

# Define function to handle user input for sub-menu of option 1 "Datos Numéricos"
def handle_input():
    while True:
        help.print_menu_options(list.functions_menu)
        sub_choice = input("\nIngresa el número de la opción que deseas: ")
            
        match sub_choice:
            case '1':
                fibonacci()
            case '2':
                triangle_type()
            case '3':
                roman_numbers()
            case '4':
                arithmetic_or_weighted_average()
            case '5':
                factorial_impar()
            case '6':
                digit_sum()
            case '7':
                horse_run()
            case '8':
                buffer()
            case '0':
                break
            case _:
                print("Opción inválida. Por favor, intenta nuevamente.")