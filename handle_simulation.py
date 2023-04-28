from generadores import *
from Tools import terminal_help as help
import listas as list

# Define function to handle user input for sub-menu of option 1 "Datos Numéricos"
def handle_input():
    while True:
        help.print_menu_options(list.simulation_menu)
        sub_choice = input("\nIngresa el número de la opción que deseas: ")
            
        match sub_choice:
            case '1':
                get_most_wind()
            case '2':
                hottest_and_coldest()
            case '3':
                humid_and_dry()
            case '4':
                average_in_parana()
            case '5':
                create_in_libertador()
            case '6':
                delete_null()
            case '0':
                break
            case _:
                print("Opción inválida. Por favor, intenta nuevamente.")
