print("Ejemplo básico de Programación Orientada a Objetos en Python")
print("---")

class Animal:

    #método especial que se ejecuando cuando se instancia la clase
    def __init__(self, name):
        #asignar atributo
        self.name = name
        self._age = 0

    @staticmethod
    def autor():
        return "Autores: Curso de AyED - FACEA - UAP"
        
    #atributo de clase: es compartido entre todas las instancias
    locomocion = "Acuática" 
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, x):
        self._age = x
        
#Uso de un método estático, no hace falta instanciar la clase
print(Animal.autor())

#Instancias

perro = Animal("rocko")
gato = Animal("Michifuz")

print("Nombres:")
perro.name = "Rocko"
perro.age = 5 #property read-only unless setter
print(perro.name)
print(gato.name)



print("Locomoción")
print(perro.locomocion)
print(gato.locomocion)
Animal.locomocion = "Terrestre"
print(perro.locomocion)
print(gato.locomocion)



