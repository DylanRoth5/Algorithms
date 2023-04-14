from Activity.manipulate_string import *

# Define function to handle user input for sub-menu of option 1 "Datos Numéricos"
def handle_input(choice):
    match choice:
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
        case  "0":
            print("¡Adiós!")
        case _:
            print("Opción inválida. Por favor, intenta nuevamente.")