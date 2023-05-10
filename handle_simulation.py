from parciales.generadores import *
from Tools import terminal_help as help
import listas as list

# Define function to handle user input for sub-menu of option 1 "Datos Numéricos"
def handle_input():
    while True:
        help.print_menu_options(list.simulation_menu)
        sub_choice = input("\nIngresa el número de la opción que deseas: ")
            
        match sub_choice:
            case '1':
                get_most_windy_station()
                select = input('\nPress any letter to go back to menu: ')
            case '2':
                hottest_and_coldest()
                select = input('\nPress any letter to go back to menu: ')
            case '3':
                humid_and_dry()
                select = input('\nPress any letter to go back to menu: ')
            case '4':
                average_in_parana()
                select = input('\nPress any letter to go back to menu: ')
            case '5':
                create_libertador()
                select = input('\nPress any letter to go back to menu: ')
            case '0':
                break
            case _:
                print("Opción inválida. Por favor, intenta nuevamente.")
