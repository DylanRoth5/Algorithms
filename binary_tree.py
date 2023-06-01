class Node:
    valor = ""
    left = None
    right = None
    def __init__(self, valor):
        self.valor = valor
        
#crear arbol de las diapositivas de clase        
raiz = Node("F")

raiz.left = Node("B")
raiz.left.left = Node("A")
raiz.left.right = Node("D")
raiz.left.right.left = Node("C")
raiz.left.right.right = Node("E")

raiz.right = Node("G")
raiz.right.right = Node("I")
raiz.right.right.left = Node("H")

def inorden(n):
    #pasar por nodo izquierdo
    if(n.left):
        inorden(n.left)
    #visitar nodo
    print(n.valor)
    #pasar por nodo derecho
    if(n.right):
        inorden(n.right)
        
def preorden(n):
    # visitar nodo
    print(n.valor)
    # pasar nodo izquierdo
    if(n.left):
        preorden(n.left)
    # pasar nodo derecho
    if(n.right):
        preorden(n.right)
    

#test
inorden(raiz)
print()
preorden(raiz)
