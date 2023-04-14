def print_menu_options(options_list):
    for index, option in enumerate(options_list):
        if index == 0:
            print("\n" + option.upper() + "\n")
        elif index == len(options_list) - 1:
            print("0. " + option + "\n")
        else:
            print(f"{index}. {option}")
    print()



menu = ['Menu Principal',
        'Datos Numéricos',
     'Datos Booleanos y Strings',
     'Manipulación de Strings',
     'Funciones, Condicionales, iteración y recursividad'
     'Salir']

print_menu_options(menu)