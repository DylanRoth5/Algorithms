"""
Generadores eólicos
===================

Datos reales obtenidos de: https://www.smn.gob.ar/descarga-de-datos
Valores promedios mensuales por estación meteorológica desde 1981 a 2010 (29 años)

Averiguar:
----------
1) ¿En qué lugar es el mejor para poner una granja de generadores eólicos?
2) Estación meteorológica más cálida del país y mes (campo 'Temperatura máxima (°C)')
   y la más fria (campo: 'Temperatura mínima (°C)')
3) Lugar y mes más húmedo y el más seco del país
4) Temperatura promedio durante todo el año en Paraná
5) Agregar estación meteorológica de Libertador San Martin (inventar datos)
6) Sacar las estaciones que le falten algun dato (dato en null)

Los datos están estruturados como segue:
estadisticas = [ Estacion1, Estacion2, Estacion3... EstacionN ]

EstacionN = {
    Estación: Nombre de la Estación   #0
    Temperatura média (°C): Valores, #1
    Temperatura máxima (°C) : Valores, #2
    Temperatura mínima (°C): Valores, #3
    Humedad relativa (%) : Valores, #4
    Velocidad del Viento (km/h) : Valores, #5
    Nubosidad total (octavos) : Valores, #6
    Precipitación (mm) : Valores, #7
    Frecuencia de días con Precipitación superior a 0.1 mm : Valores #8

}

Donde Valores representa todos los meses les año y su respectivo valor de medición
Valores={'Ene':float,...,'Dec':float }


"""
import datos

def mediaValores(valores:dict):
    i=0
    total=0
    for k,v in valores.items():
        if v!=None:
            total+=v
        i+=1
    return total/i

def totalValores(valores:dict):
    total=0
    for v in valores.values():
        if v != None:
            total+=v
    return total

def maxValores(valores:dict):
    max=0;
    for v in valores.values():
        if v!=None and v>max:
            max=v
    return max

def minValores(valores:dict):
    min=0;
    for v in valores.values():
        if v!=None and v<min:
            min=v
    return min

estadisticas = datos.estadisticas

#1) ¿En qué lugar es el mejor para poner una granja de generadores eólicos?
#percorrer las estaciones y mostrar la estación com media de vento major
def preguntaUno():
    estacao: dict
    nome_mejor_estacion = ""
    media_mejor_estacion = 0

    for estacion in estadisticas:

        media_estacion = 0
        nome_estacion = ""

        indice_values = 0
        for k,v in estacion.items():
            #Nombre de la Estación está en la posición 0
            if indice_values==0 :
                nome_estacion = v
            # Velocidad del Viento (km/h) está en la posición 5
            if indice_values==5 :
                media_estacion = mediaValores(v)
                if media_estacion > media_mejor_estacion:
                    media_mejor_estacion = media_estacion
                    nome_mejor_estacion = nome_estacion

            indice_values+=1

    print("Respuesta 1: \n     Mejor Lugar Para Poner Una Estacion:  " + str(nome_mejor_estacion) )
    print("    Velocidade Media De Los Ventos:  " + str(media_mejor_estacion) )




#2) Estación meteorológica más cálida del país y mes (campo 'Temperatura máxima (°C)') y la más fria (campo: 'Temperatura mínima (°C)')
#percorrer las estaciones y mostrar la estación com temperatura máxima y mínima
def preguntaDos():
    estacao: dict
    nome_estacion_mas_caliente = ""
    nome_estacion_mas_fria=""
    max_temperatura_estacao = 0
    min_temperatura_estacao=0

    for estacion in estadisticas:
        nome_estacion_caliente=""
        nome_estacion_fria=""
        major_temperatura_estacao=0
        menor_temperatura_estacao=0

        indice_values = 0
        for v in estacion.values():
            #Nombre de la Estación
            if indice_values==0:
                nome_estacion_fria = v
                nome_estacion_caliente = v

            # Temperatura máxima (°C)
            if indice_values==2:
                major_temperatura_estacao = maxValores(v)
                if major_temperatura_estacao != None and major_temperatura_estacao > max_temperatura_estacao:
                    max_temperatura_estacao= major_temperatura_estacao
                    nome_estacion_mas_caliente = nome_estacion_caliente

            # Temperatura mínima (°C)
            if indice_values==3:
                menor_temperatura_estacao = minValores(v)
                if(menor_temperatura_estacao != None and menor_temperatura_estacao < min_temperatura_estacao):
                    min_temperatura_estacao=menor_temperatura_estacao
                    nome_estacion_mas_fria = nome_estacion_fria

            indice_values+=1

    print("\nRespuesta 2: \n    Nombre De La Estación Mas Caliente:  " + str(nome_estacion_mas_caliente) )
    print("    La Mas Alta Temperatura Encontrada:  " + str(max_temperatura_estacao) )
    print("    Nombre De La Estación Mas Fria:  " + str(nome_estacion_mas_fria) )
    print("    La Mas Fria Temperatura Encontrada:  " + str(min_temperatura_estacao) )



preguntaUno()
preguntaDos()

        











