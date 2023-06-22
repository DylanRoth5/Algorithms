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

def print_pre_order(tree,word) :
  if tree == None : 
    # print(word)
    return
  word+=tree.valor
  print_pre_order(tree.left,word)
  print_pre_order(tree.right,word)
  print(word)

def print_in_order(tree,word) :
  if tree == None : 
    print(word)
    return
  word+=tree.valor
  print_in_order(tree.left,word)
  print_in_order(tree.right,word)

def print_post_order(tree,word) :
  if tree == None : 
    print(word)
    return
  word+=tree.valor 
  print_post_order(tree.left,word)
  print_post_order(tree.right,word)
  
def amplitud_order(cola,tree,nivel) :
  if tree == None: return
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
# print("Pré Order")
# print_pre_order(raiz)
# print("\n\nIn Order")
# print_in_order(raiz)
# print("\n\nPost Order")
# print_post_order(raiz)
# print("\n\nAmplitud Order")
# print_amplitud(raiz)

def print_words(node, current_word=""):
    if node is None:
        return
    current_word += node.valor
    
    if node.left is None and node.right is None:
        print(current_word)
    
    print_words(node.left, current_word)
    print_words(node.right, current_word)

words = Node('B')

words.left = Node('U')
words.right = Node('I')

words.left.left = Node('E')
words.right.left = Node('E')
words.left.right = Node('R')
words.right.right = Node('L')

words.left.left.left = Node('N')
words.right.left.left = Node('N')
words.right.right.left = Node('B')
words.left.right.right = Node('R')

words.left.left.left.left = Node('O')
words.left.left.left.right = Node('A')
words.right.right.left.left = Node('A')
words.left.right.right.left = Node('A')
words.left.right.right.right = Node('O')


words.left.left.left.right = Node('S')
words.left.right.right.right = Node('S')
words.right.right.left.left = Node('O')


# test
print("Pré Order")
word = ''
print_pre_order(words,word)
print("\n\nIn Order")
print_in_order(words,word)
print("\n\nPost Order")
print_post_order(words,word)
# print("\n\nAmplitud Order")
# print_amplitud(raiz)
print("\n\nprint words:")
print_words(words)

def caminos(raiz, word = ""):
    word += raiz.valor
    if(raiz.left):
        caminos(raiz.left, word)
    if(word[-1] != raiz.valor and raiz.valor != "R"):
        word += raiz.valor
    if(raiz.right):
        caminos(raiz.right, word)
    if(raiz.left == None and raiz.right == None):
        print(word)



n = Node('B')
n.left = Node('U')
n.left.left = Node('E')
n.left.left.left = Node('N')
n.left.left.left.left = Node('O')
n.left.left.left.right = Node('A')
n.left.left.left.right.right = Node('S')
n.left.right = Node('R')
n.left.right.right = Node('R')
n.left.right.right.left = Node('A')
n.left.right.right.right = Node('O')
n.left.right.right.right.left = Node('S')
n.right = Node('I')
n.right.left = Node('E')
n.right.left.left = Node('N')
n.right.right = Node('L')
n.right.right.right = Node('B')
n.right.right.right.right = Node('A')
n.right.right.right.right.right = Node('O')

print()
caminos(n)