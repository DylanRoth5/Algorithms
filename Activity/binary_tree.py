class Node:
    valor = ""
    left = None
    right = None
    def __init__(self, valor):
        self.valor = valor
        
#crear arbol de las diapositivas de clase        
# raiz = Node("F")

# raiz.left = Node("B")
# raiz.left.left = Node("A")
# raiz.left.right = Node("D")
# raiz.left.right.left = Node("C")
# raiz.left.right.right = Node("E")

# raiz.right = Node("G")
# raiz.right.right = Node("I")
    # raiz.right.right.left = Node("H")

raiz = Node(8)

raiz.left = Node(9)
raiz.right = Node(5)

raiz.left.left = Node(11)
raiz.left.right = Node(7)

raiz.left.left.left = Node(15)
raiz.left.left.right = Node(20)

raiz.left.left.left.left = Node(19)
raiz.left.left.right.left = Node(21)

raiz.left.right = Node(7)

raiz.left.right.left = Node(3)
raiz.left.right.right = Node(1)

raiz.left.right.left.left = Node(2)

raiz.right.left = Node(6)
raiz.right.right = Node(12)


raiz.right.left.left = Node(4)
raiz.right.left.right = Node(14)

raiz.right.right.left = Node(17)
raiz.right.right.right = Node(18)

raiz.right.left.left.left = Node(13)
raiz.right.left.right.left = Node(10)

raiz.right.right.left.left = Node(16)


def inorden(n):
    #pasar por nodo izquierdo
    if(n.left):
        inorden(n.left)
    #visitar nodo
    print(' ',n.valor,end='')
    #pasar por nodo derecho
    if(n.right):
        inorden(n.right)
        
def preorden(n):
    # visitar nodo
    print(' ',n.valor,end='')
    # pasar nodo izquierdo
    if(n.left):
        preorden(n.left)
    # pasar nodo derecho
    if(n.right):
        preorden(n.right)
    

#test
# preorden(raiz)
# print('\n')
# inorden(raiz)

def postorden(n):
    # pasar nodo izquierdo
    if(n.left):
        postorden(n.left)
    # pasar nodo derecho
    if(n.right):
        postorden(n.right)
    # visitar nodo
    print(' ',n.valor,end='')


def anchura(n):
    # pasar nodo izquierdo
    
    if(n.left):
        preorden(n.left)
    # pasar nodo derecho
    if(n.right):
        preorden(n.right)
    # visitar nodo
    

abecedario = Node('A') 
abecedario.left = Node('B') 
abecedario.left.right = Node('D')
abecedario.left.right.left = Node('G')
abecedario.left.right.right = Node('H')
abecedario.left.right.right.left = Node('J')  
abecedario.right = Node('C')    
abecedario.right.right = Node('F')
abecedario.right.left = Node('E')    

preorden(abecedario)
print('\n')
inorden(abecedario)
print('\n')
postorden(abecedario)