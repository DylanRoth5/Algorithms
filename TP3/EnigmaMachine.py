#
#   Classes
#       Keyboard
#       Rotor
#       Reflector
#

"""
Reflector: B
Rotors: I, IV, V
Plugboard: None
Key: AAA
Ring setting: 
Message: A => I
"""
from keyboard import Keyboard
from TP3.rotor import Rotor
from TP3.reflector import Reflector
from TP3.enigma import Enigma

# componentes
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")        
KB = Keyboard()

#definir maquina enigma
enigma = Enigma(B,I,IV,V,KB)

#set key
enigma.set_key('DOG')
enigma.r3.show()
enigma.r2.show()
enigma.r1.show()
# cifrar un mensaje
message = "test"
message = message.upper()
code=''
for letter in message:
    code += enigma.encipher(letter)

print(code)

