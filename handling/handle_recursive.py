from Activity.recursivity import *
from Tools import terminal_help as help
import listas as list

# Define function to handle user input for sub-menu of option 1 "Datos Numéricos"
def handle_input():
    while True:
        help.print_menu_options(list.recursivity_menu)
        sub_choice = input("\nIngresa el número de la opción que deseas: ")
            
        match sub_choice:
            case '1':
                dictionary()
            case '2':
                ages_dictionary()
            case '3':
                ages_and_index()
            case '4':
                prime()
            case '5':
                current_age()
            case '6':
                matrix()
            case '7':
                write_matrix()
            case '0':
                break
            case _:
                print("Opción inválida. Por favor, intenta nuevamente.")