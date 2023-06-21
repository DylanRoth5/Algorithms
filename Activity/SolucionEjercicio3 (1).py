class Node:
    valor = ""
    left = None
    right = None
    id = None
    def __init__(self, valor):
        self.valor = valor
        
#crea la arbol del ejercicio 3
raiz = Node("A")
raiz.left = Node("B")
raiz.left.left = None
raiz.left.right = Node("D")
raiz.left.right.left = Node("G")
raiz.left.right.right = Node("H")
raiz.left.right.right.left = Node("J")
raiz.left.right.right.right = None

raiz.right = Node("C")
raiz.right.left = Node("E")
raiz.right.left.left = Node("I")
raiz.right.left.right = None
raiz.right.left.left.left = Node("K")
raiz.right.left.left.right = None
raiz.right.right = Node("F")

def print_pre_order(tree) :
  if tree == None : return
  print (tree.valor, end=" ")
  print_pre_order(tree.left)
  print_pre_order(tree.right)

def print_in_order(tree) :
  if tree == None: return
  print_in_order(tree.left)
  print (tree.valor, end=" ")
  print_in_order(tree.right)

def print_post_order(tree) :
  if tree == None : return
  print_post_order(tree.left)
  print_post_order(tree.right)
  print (tree.valor, end=" ")
  
def amplitud_order(cola,tree,nivel) :
  if tree == None: return
  # print (nivel,tree.valor)
  cola.append((nivel,tree.valor))
  nivel += 1
  amplitud_order(cola,tree.left,nivel)
  amplitud_order(cola,tree.right,nivel)
  return cola

def print_amplitud(tree):
  cola = []
  amplitud_order(cola,raiz,0)
  cola.sort()
  for index,value in cola:
    print(value,end=' ')

   
   


# test
print("Pré Order")
print_pre_order(raiz)
print("\n\nIn Order")
print_in_order(raiz)
print("\n\nPost Order")
print_post_order(raiz)
print("\n\nAmplitud Order")
print_amplitud(raiz)
