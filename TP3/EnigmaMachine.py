class Enigma:
    def __init__(self,re,r1,r2,r3,kb):
        self.re = re
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.kb = kb

    def set_key(self,key):
        self.r1.rotate_to(key[0])
        self.r2.rotate_to(key[1])
        self.r3.rotate_to(key[2])

    def encipher(self,letter):
        # rotate https://www.youtube.com/watch?v=W6NfcxP8ffY&ab_channel=JoshuaZeitsoff
        # double stepping https://www.youtube.com/watch?v=5StZlF-clPc&t=24s&ab_channel=JoshuaZeitsoff
        if self.r2.left[0] == self.r2.notch and self.r3.left[0] == self.r3.notch:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r2.left[0] == self.r2.notch: # esta es la parte del double stepping
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r3.left[0] == self.r3.notch:
            self.r2.rotate()
            self.r3.rotate()
        else:
            self.r3.rotate()
        
        #pass signal
        signal = self.kb.forward(letter)
        signal = self.r3.forward(signal)
        signal = self.r2.forward(signal)
        signal = self.r1.forward(signal)
        signal = self.re.reflect(signal)
        signal = self.r1.backward(signal)
        signal = self.r2.backward(signal)
        signal = self.r3.backward(signal)
        letter = self.kb.backward(signal)
        return letter

class Keyboard:
    def forward(self,letter):
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        return signal

    def backward(self,signal):
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter

class Reflector:
    def __init__(self,wiring):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
    
    def reflect(self,signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

class Rotor:
    def __init__(self,wiring,notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notch = notch

    def forward(self,signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self,signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def rotate(self, N = 1):
        for i in range(N):
            self.left = self.left[1:] + self.left[0]
            self.right = self.right[1:] + self.right[0]

    def rotate_to(self,letter):
        N = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate(N)


# componentes
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")        
KB = Keyboard()

# definir maquina enigma
enigma = Enigma(B,I,IV,V,KB)

# set key
key = input("Escribe una llave de tres letras: ")
key = key.upper()
enigma.set_key(key)

# cifrar un mensaje
message = input('Escribe el mensaje para cifrar o descifrar: ')
message = message.upper()
code=''
for letter in message:
    code += enigma.encipher(letter)

# se puede chequear respuesta con la siguiente pagina
# http://mckoss.com/enigma-simulator-js/
print(code)

"""
Bibliografia:
    Joshua Zeitsoff: 
    https://www.youtube.com/playlist?list=PLe6eaTVou9VQoL5vGFJCH3r6bJbh04hao

    Pagina de CS61b Proyecto 1:  
    https://inst.eecs.berkeley.edu/~cs61b/fa18/materials/proj/proj1/index.html
"""