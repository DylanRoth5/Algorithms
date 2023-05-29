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

class Position:

    abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        

    def __init__(self,letter='A') -> None:
        self.initial_position = letter
        self.reset()
    
    def reset(self):
        self.x = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        for position, letter in enumerate(self.abecedario):
            if self.initial_position==letter:
                for i in range(position):
                    self.rotate()
                break
        
    def rotate(self):
        self.x.append(self.x[0])
        del self.x[0]
    
    def real_in(self, letter):
        for position, l in enumerate(self.abecedario):
            if letter == l:
                return self.x[position]
    
    def real_out(self,letter):
        for position, l in enumerate(self.x):
            if letter == l:
                return self.abecedario[position]


