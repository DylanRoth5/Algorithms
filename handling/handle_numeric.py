from Work.numeric_data import *

# Define function to handle user input for sub-menu of option 1 "Datos Numéricos"
def handle_input(choice):
    match choice:
        case '1':
            sum_ABC()
        case '1':
            mul_ABC()
        case  "0":
            print("¡Adiós!")
            exit()
        case _:
            print("Opción inválida. Por favor, intenta nuevamente.")