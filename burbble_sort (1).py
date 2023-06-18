lista = [6,5,3,1,8,7,2,4]

def ordenar_burbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            print("---")
            print("i: " + str(i) + " - j: " + str(j) + " => " + str(lista))
            print(str().rjust(j*3+16) + "-  -")
            if lista[j] > lista[j+1]:
                print("    Intercambiando: " + str(lista[j]) + " : " + str(lista[j+1]))
                #swap
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                #lista[j], lista[j+1] = lista[j+1], lista[j]
    
"""
#Burbuja abreviado (muy mala performance)
def ordenar(lista):
    j = 0
    while(j < len(lista) - 1):
        if lista[j] > lista[j+1]:            
            lista[j], lista[j+1] = lista[j+1], lista[j]
            j = -1
        j += 1
"""        

         
#print("Antes: " + str(lista))
ordenar_burbuja(lista)
#ordenar(lista)
print("Despúes: " + str(lista))

"""
Ejercicios:
1) crear una clase Persona con los atributos nombre y edad
2) crear una lista y en la lista agregar 5 instancias de Persona diferentes
3) aplicar la ordenación a la lista
"""

