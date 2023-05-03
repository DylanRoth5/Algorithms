"""
* Título: modelo de simulación de cola de supermercado
* Objetivo: calcular, simuladamente, la cantidad de cajeros para no perder más de 3 clientes por jornada
* Enviar solución por email a alexsandra.cassiano@uap.edu.ar y nicolas.giqueaux@uap.edu.ar
* Grupos de no más de 3 miembros
*
* Consideraciones:
*   -> Una cola por caja
*   -> Cantidad de cajas variables. Usar listas de cajas. Comenzar con una sola caja, luego ir aumentando.
*   -> Cada ejecución del algoritmo representa una jornada de trabajo en donde la cantidad de cajas no varía.
*   -> Para cambiar la cantidad de cajas se deberá detener el programa y parametrizar la cantidad de cajas que se desea.
*   -> Jornada dura 8 horas.
*   -> La frecuencia promedio de ingreso de una persona a la caja durante la jornada es una cada 10 minutos.
*   -> El tiempo que tarda cada caja en atender está entre 3 a 10 minutos. Determinar al azar.
*   -> Las personas tiene distintos grados de paciencia de espera en la cola, 
       si se agota abandona la compra: esperan entren 5 a 15 minutos. 
       Determinar al azar cuando entra a la cola.
*   -> Si un cliente ya está en la caja siendo atendido espera a terminar y no abandona.
*   -> Política de cajas "Primero en entrar, primero en salir"
*   -> Cuando una pesona sale de la caja se saca de la lista y se desplazan todos los elementos restantes. 
       Osea, en el índice 0 del array de la cola de la caja representa a la persona que se está atendiendo,
       cuando esta sale, se saca del array y la persona que estaba en el índice 1 para al 0, la que estaba 
       en el indice 2 pasa al 1 y así sucesivamente
*   -> Iterar cada segundo de las 8 horas de la jornada, es decir que se deberá hacer un bucle que tenga 8(horas) * 60(minutos/h) ciclos.

*   Reporte al final del día:    
*   -> Cantidad de cajas
*   -> Cantidad de personas que abondonan la compra
*   -> Cantidad de personas atendidas
*   -> Promedio de tiempo en caja
*
* https://es.wikipedia.org/wiki/Teor%C3%ADa_de_colas
"""
import math
import random
import time

def generador_persona():
    """
    Usar esta función por minuto para crear la persona que se suman a la cola de una caja
    Uso: p = generador_persona()
    Retorna: una persona o None si no hay nadie para entrar a la cola en ese minuto
    """
    p = None
    probabilidad_de_entrada = random.randint(1, 10)#probabilidad 1 en 10 de entrar a una sola cola
    if(probabilidad_de_entrada == 1):
        p = {
            "grado_de_paciencia" : random.randint(5, 15), #cantidad de minutos que tolera en la cola
            "tiempo_esperando_en_cola" : 0, #contador de iteraciones, si llega a grado_de_paciencia se va.
            "tiempo_esperando_en_caja" : 0, #contador de iteraciones cuando ya está en caja, cuando llegue a tiempo_que_tarda_la_caja, se va
            "tiempo_que_tarda_la_caja" : random.randint(3, 10), #tiempo que le va a tardar la caja en antender a este cliente: de 3 a 10 minutos
            "tiempo_en_tienda" : 0 #contador del tiempo que paso en la tienda
        }
    return p
    
#************************************************************************
#MOTOR PRINCIPAL
#Bucle que representa lo que sucede en cada minuto de la jornada laboral
#Cada iteración representa lo que sucede en un minuto de la jornada
def open_market():
    minuto = 0 #variable contador para llevar la cuenta de los minutos transcurridos del día laboral
    fin_de_la_jornada = 8 * 60 #variable que marca el fin de las 8 horas de trabajo
    cantidad_personas_abandonaron = 0
    cantidad_personas_atendidas = 0
    promedio_tiempo_cajas = 0

    fila = []
    minutos = 0
    hora = 8

    cajas = [
        [], #cola de la caja 1
        [], #cola de la caja 2
    ]

    cant_atendidos = [
        [],
        [],
    ]

    promedio_tiempo_de_atencion = []

    cantidad_de_cajas = len(cajas) #para determinar con cuantas cajas se trabaja una jornada


    print('\nEl Supermercado trabaja de corrido desde las 8am hasta las 4pm (8horas)\n')

    while(minuto <= fin_de_la_jornada): 
        minuto = minuto + 1
        time.sleep(0.005)
        minutos = minutos+1
        if(minutos==60):
            hora = hora+1
            minutos = 0
        tiempo= f'{hora}:{minutos}'
        #LOGICA DE LA ENTRADA A COLA
        #¿en este minuto ingresa un persona a la caja?:
        p = generador_persona()
        if(p):
            print("A las "+str(tiempo)+" entro una persona a fila: esperara = " + str(p["grado_de_paciencia"]) + " min | retrasara = " + str(p["tiempo_que_tarda_la_caja"])+" min")
            fila.append(p)
            
        #LOGICA DE LA PACIENCIA
        #incrementar a todos los contadores de la personas en cola 1 minuto, evaluar si supera el límite de paciencia, sacar de la cola de ser necesario
        for persona in fila:
            persona["tiempo_esperando_en_cola"] +=1
            persona["tiempo_en_tienda"] +=1
            if(persona["tiempo_esperando_en_cola"] > persona["grado_de_paciencia"]):
                print('\033[31m' + 'A las '+ str(tiempo) + ' una persona se canso de esperar y se fue...' + '\033[0m')
                cantidad_personas_abandonaron+=1
                fila.pop(fila.index(persona))


        #LOGICA DE LA SALIDA DE CAJA
        #incrementar el contador de la persona que está en caja en 1 minuto. evaluar si ya llega al fin de tiempo determinado para atendderlo
        for caja in cajas:

            if ((len(caja)==0) and (len(fila)>0)): #checkeo que haya una caja disponible y que haya personas en la fila
                index = 0
                for persona in fila: #chequeo cada persona en la fila (probablemente se puede optimizar, esta es la forma mas sencilla que encontre)
                    if(index == 0): #tomo la primera persona en la fila
                        entrante = persona
                        index+=1        
                caja.append(entrante) #la primera persona entra a la caja
                print('\033[34m' + 'A las '+ str(tiempo) + ' una persona entro a la caja ' + str(cajas.index(caja)+1) + '\033[0m')
                fila.pop(0) #saco a la primera persona de la fila porque ahora esta en la caja
            
            if (len(caja)==1): #chequeo si tiene a una persona la caja
                for persona in caja: 
                    if(persona["tiempo_esperando_en_caja"] == persona["tiempo_que_tarda_la_caja"]): # chequeo si la persona termino
                        cantidad_personas_atendidas+=1
                        cant_atendidos[cajas.index(caja)] += '1'
                        print('\033[32m' + 'A las '+ str(tiempo) + ' una persona salio atendido de la caja ' + str(cajas.index(caja)+1) + '\033[0m')
                        promedio_tiempo_de_atencion += str(persona["tiempo_en_tienda"])
                        caja.pop(0) #la persona atendida sale de la caja
                    else:
                        persona["tiempo_esperando_en_caja"]+=1 #si no termino se aumenta el tiempo que estuvo en caja        
                        persona["tiempo_en_tienda"] +=1 #aumenta el tiempo que paso en la tienda

    #chequeo cuantas personas quedaron en la fila al terminar la jornada
    largo_de_fila = len(fila) 
    if(largo_de_fila>0):
        #si queda alguien en la fila al cierre del supermercado se fuerza el abandono
        cantidad_personas_abandonaron += largo_de_fila
        fila.clear()
    
    sum_tiempo_de_atencion=0
    len_tiempo_de_atencion=0

    for numero in promedio_tiempo_de_atencion:
        sum_tiempo_de_atencion += int(numero)
        len_tiempo_de_atencion +=1

    promedio_tiempo_cajas = round((sum_tiempo_de_atencion)/len_tiempo_de_atencion,2)
    

    conversion_del_promedio = promedio_tiempo_cajas
    while conversion_del_promedio>0:
        conversion_del_promedio-=1
    
    minutos_del_promedio = round(promedio_tiempo_cajas-conversion_del_promedio)
    segundos_del_promedio = round(conversion_del_promedio*60)
    segundos_del_promedio = segundos_del_promedio*-1

    print("\nCantidad cajas: " + str(cantidad_de_cajas))
    print("Abandonaron: " + str(cantidad_personas_abandonaron))
    print("Atendidos: " + str(cantidad_personas_atendidas))
    i=0
    for caja in cant_atendidos:
        print(f"    Atendidos en caja {i+1}: " + str(len(cant_atendidos[i])))
        i+=1
    print("Promedio de tiempo de atención: " + str(minutos_del_promedio) + f" minutos y {segundos_del_promedio} segundos")

