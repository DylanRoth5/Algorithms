#
#   Classes
#       Enigma
#       Keyboard
#       Rotor
#       Reflector
#

"""

Bibliografia:
    Joshua Zeitsoff: 
    https://www.youtube.com/playlist?list=PLe6eaTVou9VQoL5vGFJCH3r6bJbh04hao

    Pagina de CS61b Proyecto 1:  
    https://inst.eecs.berkeley.edu/~cs61b/fa18/materials/proj/proj1/index.html

    Coding casowary:
    https://www.youtube.com/playlist?list=PLBLV84VG7Md9EtoV2fYyTeomWyLD2-X75

Configuracion:    
    Reflector: B
    Rotors: I, IV, V
    Key: AAA
    Ring setting: AAA (No lo he hecho aun)
    Message: A => I
"""

from keyboard import Keyboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma

# componentes
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")        
KB = Keyboard()

#definir maquina enigma
enigma = Enigma(B,I,IV,V,KB)

#set key
key = input("Escribe una llave de tres letras: ")
key = key.upper()
enigma.set_key(key)

# cifrar un mensaje
message = input('Escribe el mensaje para cifrar o descifrar: ')
message = message.upper()
code=''
for letter in message:
    code += enigma.encipher(letter)

# Chequear respuesta con la siguiente pagina
# http://mckoss.com/enigma-simulator-js/
print(code)

