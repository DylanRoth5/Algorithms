
atributos = [{'name':'dylan','age':19},{'name':'Susan','age':42},
             {'name':'Ron','age':37},{'name':'Ana','age':51},
             {'name':'Ronny','age':13},{'name':'Bet','age':84}]

def dictionary():
    print(atributos)
    end = input('Press any key to exit this exercise')

def ages_dictionary():
    for item in atributos:
        print(item['age'])
    end = input('Press any key to exit this exercise')

def ages_and_index():
    for item in atributos:
        print(atributos.index(item),item['age'])
    end = input('Press any key to exit this exercise')

def prime():
    number = int(input('Input a Prime Number: '))
    is_divisible=0
    for i in range(number+1):
        # print(i,number)
        if i>0 and ((number%i)==0):
            # print(f'es divisible por {i}')
            is_divisible+=1  
    if is_divisible == 2:
        print('Es Primo')
    else:
        print('No es primo')
    end = input('Press any key to exit this exercise')

def current_age():
    print('dictionary')
    end = input('Press any key to exit this exercise')

def matrix():
    print('matrix NxN')
    end = input('Press any key to exit this exercise')

def write_matrix():
    print('Matrix to write')
    end = input('Press any key to exit this exercise')


# ages_dictionary()
# ages_and_index()
prime()