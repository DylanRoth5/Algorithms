print("Ejemplo básico de Listas enlazadas con POO en Python")
print("---")

class Letra:
    siguiente_letra = None
    def __init__(self, letra):
        self.letra = letra
    
raiz = Letra("A")

raiz.siguiente_letra = Letra("B")

raiz.siguiente_letra.siguiente_letra = Letra("C")

def mostrar_lista(x):
    while x != None:
        print(x.letra)
        x = x.siguiente_letra

mostrar_lista(raiz)
   
    
"""
Práctica:
---------
1) Hacer una función para agregar un elemento más al final de la lista
2) Hacer una función para sacar un elemento al final de la lista
3) Hacer una función para sacar un elemento al comienzo de la lista
4) Hacer una función para sacar un elemento en la posición x de la lista
   (reenlazar los objetos detrás)
5) Hacer una función para agregar un elemento más en la posición x de la lista   
"""
