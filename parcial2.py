
# Ejercicio 1
# -----------------------------------------------

class Jugador:

    def __init__(self,nombre,peso,goles,partidos):
        self.nombre = nombre
        self.peso = peso
        self.goles = goles
        self.partidos = partidos
        self.set_prom()

    def set_prom(self):
        self.prom_gxp = round(self.goles/self.partidos,2)

    def __str__(self):
        self.set_prom()
        return self.nombre + "," + str(self.peso)+ "KG," + str(self.goles)+ " goles," + str(self.partidos)+ " partidos,"+ str(self.prom_gxp)+ " GxP."

    #llamado por el operador ==
    def __eq__(self, otra_persona):
        self.set_prom()
        otra_persona.set_prom()
        return self.prom_gxp == otra_persona.prom_gxp

    #llamado por el operador !=
    def __ne__(self, otra_persona):
        self.set_prom()
        otra_persona.set_prom()
        return self.prom_gxp != otra_persona.prom_gxp

    #llamado por el operador >
    def __gt__(self, otra_persona):
        self.set_prom()
        otra_persona.set_prom()
        return self.prom_gxp > otra_persona.prom_gxp

    #llamado por el operador <
    def __lt__(self, otra_persona):
        self.set_prom()
        otra_persona.set_prom()
        return self.prom_gxp < otra_persona.prom_gxp

    #llamado por el operador >=
    def __ge__(self, otra_persona):
        self.set_prom()
        otra_persona.set_prom()
        return self.prom_gxp >= otra_persona.prom_gxp

    #llamado por el operador <=
    def __le__(self, otra_persona):
        self.set_prom()
        otra_persona.set_prom()
        return self.prom_gxp <= otra_persona.prom_gxp
    

def ordenar_burbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

jugadores = [
    Jugador('Messi',70,1000,800),
    Jugador('DiMaría',73,700,900),
    Jugador('Martinez',91,0,200),
    Jugador('Paredes',82,50,450)]

# para probar si se cambia dinamicamente o no
# jugadores[2].goles += 1500
# jugadores[0].partidos += 1500

ordenar_burbuja(jugadores)
print()
print('Ordenado por GxP ascendente:')
for j in jugadores:
    print(j)
print()

# Ejercicio 2
# -----------------------------------------------

class Tag:
    def __init__(self, n, i):
        self.tag = n
        self.id = i
        self.childs = []

html = Tag("html", None)
html.childs.append(Tag("head", None))
html.childs.append(Tag("body", None))
html.childs[1].childs.append(Tag("header", None))
html.childs[1].childs.append(Tag("article", None))
html.childs[1].childs.append(Tag("footer", None))

html.childs[1].childs[1].childs.append(Tag("div", "content"))
html.childs[1].childs[1].childs[0].childs.append(Tag("p", "text"))

def recorrer(r, sangria = ""):
    id = ''
    if r.id != None:
        id = f' id="{r.id}"'
    print(sangria + f'<{r.tag}{id}>')
    s2 = sangria
    sangria += "    "    
    for i in r.childs:
        recorrer(i, sangria)
    print(s2 + f'</{r.tag}>')

recorrer(html,'')
print()


# Ejercicio 3
# -----------------------------------------------

'''
Si tengo una lista con N cantidad de elementos y la 
estaba ordenando con un algoritmo de complejidad O(n^2). 
Mañana tendrá N+1 elemento y tengo la posibilidad de 
aplicar un algoritmo de ordenación de complejidad O(n): 
    ¿me conviene cambiar el tipo de algortimo o 
    sigo con el que estaba?

Respuesta:
    Te combiene cambiar de algoritmo, porque en el primer algoritmo
    la complejidad aumenta exponencialmente, es decir que llegara 
    el momento donde poner un solo item mas se hara demaciado costoso 
    para ordenar y en vez de llevarte segundos llevara minutos y despues horas.

    Con el algoritmo de O(n) la complejidad aumentara linealmente, 
    por lo que si bien sigue aumentando con el tiempo, siempre sera mas escalable
    que el primer algoritmo.

    para representarlo mejor:

    siendo n la longitud
    O(n^2) => n+1 = n*n
    O(n) => n+1 = n+m siendo m una constante
'''