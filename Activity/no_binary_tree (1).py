class Node:
    valor = ""
    subnodes = None
    def __init__(self, valor):
        self.valor = valor
        self.subnodes = []
        
#https://es.wikipedia.org/wiki/Taxonom%C3%ADa#/media/Archivo:Taxonomia-y-filogenia.gif
raiz = Node("Transporte")
raiz.subnodes.append(Node("Automotor"))
raiz.subnodes.append(Node("Ciclomotor"))
raiz.subnodes.append(Node("Bicicleta"))
raiz.subnodes.append(Node("Cuadrúpedo"))

raiz.subnodes[0].subnodes.append(Node("Terrestre"))
raiz.subnodes[0].subnodes.append(Node("Aéreo"))
raiz.subnodes[0].subnodes.append(Node("Matítimo"))

raiz.subnodes[0].subnodes[0].subnodes.append(Node("Autos"))
raiz.subnodes[0].subnodes[0].subnodes.append(Node("Tren"))
raiz.subnodes[0].subnodes[0].subnodes.append(Node("Colectivos"))

raiz.subnodes[3].subnodes.append(Node("Caballo"))
raiz.subnodes[3].subnodes.append(Node("Camello"))
raiz.subnodes[3].subnodes.append(Node("Mula"))


def recorrer(r, sangria = ""):
    print(sangria + r.valor + "\n")
    sangria += "  "    
    for i in r.subnodes:
        recorrer(i, sangria)
    
recorrer(raiz)

"""
Para agregar:
1) medios de transporte aéreos
2) bajo "Autos" agregar marcas de autos
"""
