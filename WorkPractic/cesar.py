# Objetivo:
# 1) Generar un algoritmo que permita el ingreso de una frase y nro de desplazamiento x y le aplique el cifrado César.
# 2) Algoritmo del camino inverso al punto 1
# 3) Puntos extras: un algoritmo que con solo ingresar la frase cifrada logre encontrar el nro de desplazamiento que se usó y la descifre.

# Reglas de cifrado:
# 1) Usar el método de cifrado César
# 2) Usar palabras del diccionario en español
# 3) Se puede desplazar arbitrariamente el alfabeto
# 4) Separar espacios entre palabras
# 5) No codificar los espacios
# 6) Se sugiere usar una frase de algún famoso inspiradora
# 7)“Soy optimista, no veo que sea útil ser otra cosa” WChurchill

# Esto no es mas necesario
# Tienes que descargar a libreria nltk para una lista de todas las palabras en ingles. para esto en consola >> pip install nltk
# import nltk
# nltk.download() # de las listas elegi todas las que se llamen 'words' para descargar. esto solo lo tienes que hacer una ves.
# from nltk.corpus import words
# word_list = words.words()

import random
import string
from palabras import array

word_list = array
ranint = random.randrange(26)
abcedary = string.ascii_lowercase

lettersABC = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
exeptions = ' ','.',',','\"','\'','“','”','ú','ñ'

def cipher_cesar(phrase: str,alt = 0):
    phrase = phrase.lower()
    ciphered_phrase = ''
    if alt == 0:
        alt = ranint

    for letter in phrase:
        for letterABC in abcedary:
            if letter == letterABC:
                letter_index = abcedary.index(letterABC)+alt
                if letter_index >=  26:
                    letter_index -= 26
                ciphered_phrase+=abcedary[letter_index]
        for ex in exeptions:
            if letter == ex:
                ciphered_phrase += ex
    return ciphered_phrase

def decipher(code):
    decoded_phrase = []
    phrase = ''
    offset = 0

    while offset< len(lettersABC):
        for letter in code:
            for abc in lettersABC:
                if letter == abc:
                    letter_index = lettersABC.index(letter)-offset
                    phrase+=(lettersABC[letter_index])
                    if letter_index<0:
                        letter_index+= len(lettersABC)
            for ex in exeptions:
                if letter == ex:
                    phrase += ex
        decoded_phrase.append(phrase)
        phrase = ''
        offset+=1

    frequency = {}
    for phrase in decoded_phrase:
        frequency[phrase] = 0

    for word in array:
        wordSpace = f' {word} '
        for phrase in decoded_phrase:
            if wordSpace in phrase:
                frequency[phrase]+=1

    sorted = []
    for value in frequency.values():
        if value >0:
            sorted.append(int(value))
    sorted.sort(reverse=True)

    getting_there = True
    got_there='no'
    while getting_there == True:
        for value in sorted:
            for phrase in frequency:
                if frequency[phrase]==value:
                    print(phrase)
                    got_there = input('Es esta la decodificacion correcta? yes/no ')
                    if got_there == 'yes':
                        correct_phrase = phrase
                        getting_there = False
                        break  
            if got_there == 'yes':
                getting_there = False
                break 
    
    return correct_phrase

# Frases para probar:
    # “Soy optimista, no veo que sea útil ser otra cosa” WChurchill
    # “No cuentes los días, haz que los días cuenten.”
    # “El amor no tiene cura, pero es la cura para todos los males.” ...
    # “El mejor momento del día es ahora.” ...
    # “Sé el cambio que quieres ver en el mundo.” ...
    # “Piensa, sueña, cree y atrévete.” ...
    # El sentido de la vida es tener valores, no cosas de valor.

print("""

Menu Codigo Cesar (Escribe 2 palabras o mas en español)
1. codificar un texto
2. decodificar un texto
0. salir

""")
while True:
    
    choice = input("Ingresa el número de la opción que deseas: ")
    
    match choice:
        case "1":
            phrase = input('\nwrite the phrase you want to cipher: ')

            print('==========================\n'+cipher_cesar(phrase)+'\n==========================')
        case  "2":
            code = input('\nwrite the phrase you want to decipher: ')
            print('==========================\n'+decipher(code)+'\n==========================')
        case  "0":
            print("\n¡Adiós!")
            exit()
        case _:
            print("Opción inválida. Por favor, intenta nuevamente.")
        
    print("""
    Menu Codigo Cesar (Escribe 2 palabras o mas en español)
    1. codificar un texto
    2. decodificar un texto
    0. salir
    """)
