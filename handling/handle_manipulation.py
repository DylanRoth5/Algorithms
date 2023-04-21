from Activity.manipulate_string import *
from Tools import terminal_help as help

# Define function to handle user input for sub-menu of option 1 "Datos Numéricos"
def handle_input():
    while True:
        help.print_menu_options(list.string_manipulation_menu)
        sub_choice = input("\nIngresa el número de la opción que deseas: ")
            
        match sub_choice:
            case '1':
                ten_animal_string()
            case '2':
                animal_string_print()
            case '3':
                string_to_list()
            case '4':
                string_order()
            case '5':
                array_of_five()
            case '6':
                tour_array()
            case '7':
                sum_array_elements()
            case '8':
                add_on_arrays()
            case '0':
                break
            case _:
                print("Opción inválida. Por favor, intenta nuevamente.")