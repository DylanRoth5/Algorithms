from Tools.terminal_help import *

def ten_animal_string():
    string = ['monkey','elefant','Okapi','Wolf','Fossa','Blue Dragon','Spider Crab','Loris', 'Rabbit', 'Axolotl']
    print(string)

def animal_string_print():
    string = ['monkey','elefant','Okapi','Wolf','Fossa','Blue Dragon','Spider Crab','Loris', 'Rabbit', 'Axolotl']
    print(string[slice(None, None, None)])

def string_to_list():
    string = 'monkey,elefant,Okapi,Wolf,Fossa,Blue Dragon,Spider Crab,Loris,Rabbit,Axolotl'
    lista = string.split(',')
    print(lista)

def string_order():
    string = ['monkey', 'elefant', 'Okapi', 'Wolf', 'Fossa', 'Blue Dragon', 'Spider Crab', 'Loris', 'Rabbit', 'Axolotl']
    string.sort()
    print(string)

def array_of_five():
    my_array = [1, 2, 3, 4, 5]
    print(my_array)

def tour_array():
    my_array = [1, 2, 3, 4, 5]
    for element in my_array:
        print(element)

def sum_array_elements():
    my_array = [1, 2, 3, 4, 5]
    sum_of_array = sum(my_array)
    print(sum_of_array)

def add_on_arrays():
    my_array = [1, 2, 3, 4, 5]
    my_array.insert(2, 6)
    my_array = my_array + [7, 8]
    my_array[2:2] = [9, 10]
    my_array.extend([11, 12])
    print(my_array)

