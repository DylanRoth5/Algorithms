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

import random
import string
# Tienes que descargar a libreria nltk para una lista de todas las palabras en ingles. para esto en consola >> pip install nltk
# import nltk
# nltk.download() # de las listas elegi todas las que se llamen 'words' para descargar. esto solo lo tienes que hacer una ves.
from nltk.corpus import words
word_list = words.words()


phrase = input('write the phrase you want to cipher: ')

ranint = random.randrange(25)

abcedary = string.ascii_lowercase

def cipher_cesar(phrase: str,alt = 0):
    phrase = phrase.lower()
    ciphered_phrase = ''

    if alt == 0:
        alt = ranint
    print(ranint)

    for letter in phrase:
        for letterABC in abcedary:
            if letter == letterABC:
                letter_index = abcedary.index(letterABC)+alt
                if letter_index > 25:
                    letter_index -=25      
                ciphered_phrase+=abcedary[letter_index]
        if letter == ' ':
            ciphered_phrase+=' '
    
    
    return ciphered_phrase

def decipher(code):
    decoded_phrase = ''
    
    alt = 0
    while alt<26:
        for letter in code:
            for letterABC in abcedary:
                if letter == letterABC:
                    letter_index = abcedary.index(letterABC)-alt
                    if letter_index < 0:
                        letter_index +=25      
                    decoded_phrase+=abcedary[letter_index]
            if letter == ' ':
                break
        for word in word_list:
            if word == decoded_phrase:
                offset = alt
        decoded_phrase = ''
        alt +=1
    
    print(offset)

    for letter in code:
        for letterABC in abcedary:
            if letter == letterABC:
                letter_index = abcedary.index(letterABC)-offset
                if letter_index > 25:
                    letter_index -=25      
                decoded_phrase+=abcedary[letter_index]
        if letter == ' ':
            decoded_phrase+=' '
    
    return decoded_phrase


print(phrase)
code = cipher_cesar(phrase)
print(code)
decode = decipher(code)
print(decode)