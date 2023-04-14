# Define function to print menu
def print_menu():
    print("MENU")
    print("1. Datos Numéricos")
    print("2. Datos Bolean y String")
    print("3. Manipulación de Strings")
    print("4. Funciones, Condicionales, iteración y recursividad")
    print("0. Salir\n")

# Define function to handle user input
def handle_input(choice):
    match choice:
        case "1":
            print("Has elegido Datos Numéricos")
        case "2":
            print("Has elegido Datos Bolean y String")
        case "3":
            print("Has elegido Manipulación de Strings")
        case "4":
            print("Has elegido Funciones, Condicionales, iteración y recursividad")
        case "0":
            print("¡Adiós!")
            exit()
        case _:
            print("Opción inválida. Por favor, intenta nuevamente.")

# Print menu initially
print_menu()

# Keep prompting user for input until they choose to exit
while True:
    choice = input("Ingresa el número de la opción que deseas: ")
    handle_input(choice)
    print_menu()
