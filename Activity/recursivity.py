from datetime import date
from dateutil import relativedelta
import Tools.terminal_help as help

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
        if i>0 and ((number%i)==0):
            is_divisible+=1  
    if is_divisible == 2:
        print('Es Primo')
    else:
        print('No es primo')
    end = input('Press any key to exit this exercise')

def current_age():
    input_date = help.get_date()
    current_date = date.today()
    print(input_date)
    print(current_date)
    diff = (relativedelta.relativedelta(current_date,input_date))
    print('your current age is:',diff.years)
    end = input('Press any key to exit this exercise')

def matrix():
    N = int(input('Crear matriz de NxN siendo N = '))
    matrix=[] #define empty matrix
    row=[] #Mistake position 
    for i in range(N): #total row is 3
        row=[] #Credits for Hassan Tariq for noticing it missing
        for j in range(N): #total column is 3
            row.append(0) #adding 0 value for each column for this row
        matrix.append(row) #add fully defined column into the row
    for row in matrix:
        print(row)
    end = input('Press any key to exit this exercise')

def write_matrix():
    N = int(input('Crear matriz de NxN siendo N = '))
    matrix=[] #define empty matrix
    row=[] #Mistake position 
    for i in range(N): #total row is 3
        row=[] #Credits for Hassan Tariq for noticing it missing
        for j in range(N): #total column is 3
            row.append(int(input())) #adding 0 value for each column for this row
        matrix.append(row) #add fully defined column into the row
    for row in matrix:
        print(row)
    end = input('Press any key to exit this exercise')


# ages_dictionary()
# ages_and_index()
# prime()
# current_age()