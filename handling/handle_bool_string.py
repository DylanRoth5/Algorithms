from Activity.bool_string import *
from Tools import terminal_help as help

# Define function to handle user input for sub-menu of option 1 "Datos Numéricos"
def handle_input():
    while True:
        help.print_menu_options(list.boolean_string_menu)
        sub_choice = input("\nIngresa el número de la opción que deseas: ")
            
        match sub_choice:
            case '1':
                is_pair()
            case '2':
                is_older()
            case '3':
                travel_alone()
            case '4':
                r_rated()
            case '5':
                same_parity()
            case '6':
                time_lost()
            case '7':
                text_quote()
            case '8':
                conected_var()
            case '9':
                var_text()
            case '10':
                formatted_text()
            case '0':
                break
            case _:
                print("Opción inválida. Por favor, intenta nuevamente.")
