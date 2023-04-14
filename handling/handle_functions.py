from Activity.manipulate_string import *

# Define function to handle user input for sub-menu of option 1 "Datos Numéricos"
def handle_input(choice):
    match choice:
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
        case  "0":
            print("¡Adiós!")
        case _:
            print("Opción inválida. Por favor, intenta nuevamente.")