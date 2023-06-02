# Simulador de la máquina cifradora Enigma

# Objetivos
# 1) Emular por software mediante un algoritmo, utilizando todo lo aprendido en la
#       asignatura, el funcionamiento de una máquina cifradora de la segunda guerra mundial
#       Enigma pero con algunas consideraciones para simplificar el modelo.
# 2) Generar un mecanismo de cifrado.
# 3) Generar un mecanismo de descifrado.
# 4) Aprender de la historia universal y de la historia de la computación.


# Consideraciones:
#   Para simplificar el modelo se usará sin el Ring Setting ni plugboard.
#   Los rotores a usar son I, IV, V del modelo Engima I (Ver combinaciones en
#       https://en.wikipedia.org/wiki/Enigma_rotor_details). En ese orden.
#   El reflector a usar es el marcado como REFLECTOR B (Ibid)
#   Se recomienda “crear” la máquina con el tubo y la impresión del PDF con los rotores
#       para testing y análisis.
#   El proceso de cifrado o descifrado puede comenzar en cualquier posición del rotor.
#   El rotor gira una posición a la siguiente letra del abecedario de forma ascendente y
#       entonces se procesa el circuito.
#   Usar Objetos y Clases

# class Position:

#     abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        

#     def __init__(self,letter='A') -> None:
#         self.initial_position = letter
#         self.reset()
    
#     def reset(self):
#         self.x = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#         for position, letter in enumerate(self.abecedario):
#             if self.initial_position==letter:
#                 for i in range(position):
#                     self.rotate()
#                 break
        
#     def rotate(self):
#         self.x.append(self.x[0])
#         del self.x[0]
    
#     def real_in(self, letter):
#         for position, l in enumerate(self.abecedario):
#             if letter == l:
#                 return self.x[position]
    
#     def real_out(self,letter):
#         for position, l in enumerate(self.x):
#             if letter == l:
#                 return self.abecedario[position]


# class Rotor_V:
#     position = None
#     entry = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#     out = ["V", "Z", "B", "R", "G", "I", "T", "Y", "U", "P", "S", "D", "N", "H", "L", "X", "A", "W", "M", "J", "Q", "O", "F", "E", "C", "K"]
        
#     def __init__(self, initial_pos="A"):
#         self.position = Position(initial_pos)

#     def code(self, letter):
#         letter = self.position.real_in(letter)
#         for pos, l in enumerate(self.entry):
#             if letter == l:
#                 letter = self.out[pos]
#                 break
#         return letter
    
#     def decode(self, letter):        
#         for pos, l in enumerate(self.out):
#             if letter == l:
#                 letter = self.entry[pos]
#                 break
#         letter = self.position.real_out(letter)
#         return letter

# class Rotor_IV:
#     position = None
#     entry = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#     out = ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B']
        
#     def __init__(self, initial_pos="A"):
#         self.position = Position(initial_pos)

#     def code(self, letter):
#         letter = self.position.real_in(letter)
#         for pos, l in enumerate(self.entry):
#             if letter == l:
#                 letter = self.out[pos]
#                 break
#         return letter
    
#     def decode(self, letter):        
#         for pos, l in enumerate(self.out):
#             if letter == l:
#                 letter = self.entry[pos]
#                 break
#         letter = self.position.real_out(letter)
#         return letter
    
# class Rotor_I:
#     position = None
#     entry = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#     out = ["E","K","M","F","L","G","D","Q","V","Z","N","T","O","W","Y","H","X","U","S","P","A","I","B","R","C","J"]
        
#     def __init__(self, initial_pos="A"):
#         self.position = Position(initial_pos)

#     def code(self, letter):
#         letter = self.position.real_in(letter)
#         for pos, l in enumerate(self.entry):
#             if letter == l:
#                 letter = self.out[pos]
#                 break
#         return letter
    
#     def decode(self, letter):        
#         for pos, l in enumerate(self.out):
#             if letter == l:
#                 letter = self.entry[pos]
#                 break
#         letter = self.position.real_out(letter)
#         return letter


# rotorV  = Rotor_V("B")
# rotorIV = Rotor_IV("A")
# rotorI  = Rotor_I("C")

# frase = input("Ingrese una frase: ").upper()

# code = ""
# rotations = 0
# for letra in frase:
#     if letra != " ":
#         rotorV.position.rotate()
#         rotations+=1
#         code += rotorV.code(letra)
#     else:
#         code += " "




# print("Code: " + code)

# rotorV.position.reset()

# decoded = ""
# for letra in code:
#     if letra != " ":
#         rotorV.position.rotate()
#         decoded += rotorV.decode(letra)
#     else:
#         decoded += " "
        
# print("Decoded: " + decoded)


abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

rotorI     = ["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J"]
rotorIV    = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B']
rotorV     = ["V", "Z", "B", "R", "G", "I", "T", "Y", "U", "P", "S", "D", "N", "H", "L", "X", "A", "W", "M", "J", "Q", "O", "F", "E", "C", "K"]

def rotate(rotor):
    x      = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for letter in rotor:
        if rotor[rotor.index(letter)] != rotor[-1]:
            x[rotor.index(letter)] = rotor[rotor.index(letter)+1]
        else: x[rotor.index(letter)] = rotor[0] 
    return x

ins = 'hola'

ins = ins.upper()


# print(rotate(rotorI))
rotation = 0
phase_one = ''
for item in ins:
    for letter in abecedario:
        if letter == item:
            # print(letter,abecedario.index(letter))
            rotorI = rotate(rotorI)
            rotation += 1
            # print(rotorI[abecedario.index(letter)])
            phase_one+= rotorI[abecedario.index(letter)]
            

phase_two = ''
for item in phase_one:
    for letter in abecedario:
        if letter == item:
            # print(phase_one.index(letter)+1) 
            # print(letter,abecedario.index(letter)-(phase_one.index(letter)+1))

            # print(rotorIV[abecedario.index(letter)-(phase_one.index(letter)+1)])
            phase_two+= rotorIV[abecedario.index(letter)-(phase_one.index(letter)+1)]





print(ins)
print(phase_one)
print(phase_two)