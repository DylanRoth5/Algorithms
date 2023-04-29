from smn import *

# Averiguar:
# ¿En que lugar es el mejor para poner una granja de generadores eólicos?
# Estación meteorológica más cálida del país (campo 'Temperatura máxima (°C)') y la más fria (campo: 'Temperatura mínima (°C)')
# Lugar más húmedo y el más seco del país
# Temperatura promedio durante todo el año en Paraná
# Agregar estación meteorológica de Libertador San Martin (inventar datos)
# Sacar las estaciones que le falten algun dato (dato en null)

# Advertencia: Soy bastante inconsistente con el idioma, hay cosas en ingles y cosas en español

def get_sum_of_values(condition):
    total_values = {}
    for estacion in estadisticas: # Access station
        for key in estacion: # Access type of value
            sum_values = 0
            for month in estacion[condition]: # Access individual values then Sum every value from that type on the station
                value = (estacion[condition][month])
                if value == None: sum_values += 0
                else: sum_values += value
            sum_values = round(sum_values,2)
        total_values[estacion['Estación']]=sum_values # make a separate dictionary to hold the sum of values based on station 
    return total_values

def get_sorted_values(total_values):
    sorted_values = sorted(total_values.values(),reverse=True) # make an array that holds the sorted values of the sums
    
    amount_null = 0 # Search null data in sorted values
    for item in sorted_values:
        if item == 0: amount_null+=1

    for i in range(amount_null): # remove from the sorted value null data
        sorted_values.remove(0)
    # Saco todas las estaciones que le faltan algun dato porque me molestan para tomar mediciones
    return sorted_values # De este modo tambien cumplo con la ultima consigna desde el principio

def get_max_value(type_medition):
    total_values = get_sum_of_values(type_medition)
    sorted_values = get_sorted_values(total_values)
    for item in total_values: # get Max value of station
        if total_values[item] == sorted_values[0]:
            print(item)
    print(type_medition,' Average: ',end='')
    print(round(sorted_values[0]/12,2)) # print max value


def get_min_value(type_medition):
    total_values = get_sum_of_values(type_medition)
    sorted_values = get_sorted_values(total_values)
    for item in total_values: # get min value of station
        if total_values[item] == sorted_values[-1]:
            print(item)
    print(type_medition,' Average: ',end='')
    print(round(sorted_values[-1]/12,2)) # print min value

# from Teo's code
def station_index(estation):
    for dict in estadisticas:
        if dict['Estación'] == estation:
            return estadisticas.index(dict)

def prom_of_station(station,type_medition):
    total_values = get_sum_of_values(type_medition)
    print(station)
    print(type_medition,' Average: ',end='')
    print(round(total_values[station]/12,2))

def get_most_windy_station():
    print('Most Windy Station: ',end='')
    get_max_value('Velocidad del Viento (km/h)')

get_most_windy_station()

def hottest_and_coldest():
    print('Hottest Station: ',end='')
    get_max_value('Temperatura máxima (°C)')
    print('Coldest Station: ',end='')
    get_min_value('Temperatura mínima (°C)')

hottest_and_coldest()

def humid_and_dry():
    print('Most Humid Station: ',end='')
    get_max_value('Humedad relativa (%)')
    print('Dryest Station: ',end='')
    get_min_value('Humedad relativa (%)')

humid_and_dry()

def average_in_parana():
    prom_of_station('PARANÁ AERO','Temperatura (°C)')

average_in_parana()

def create_in_libertador():
    print()

