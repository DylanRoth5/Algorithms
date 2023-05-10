from parciales.smn import *

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

# get_most_windy_station()

def hottest_and_coldest():
    print('Hottest Station: ',end='')
    get_max_value('Temperatura máxima (°C)')
    print('Coldest Station: ',end='')
    get_min_value('Temperatura mínima (°C)')

# hottest_and_coldest()

def humid_and_dry():
    print('Most Humid Station: ',end='')
    get_max_value('Humedad relativa (%)')
    print('Dryest Station: ',end='')
    get_min_value('Humedad relativa (%)')

# humid_and_dry()

def average_in_parana():
    prom_of_station('PARANÁ AERO','Temperatura (°C)')

# average_in_parana()

def create_libertador():
    libertador = {
    'Estación' : 'Libertador San Martin', 
	'Temperatura (°C)' : {
            'Ene' : 12.8, 'Feb' : 12.5, 'Mar' : 12.4, 'Abr' : 10.9, 'May' : 6.9, 'Jun' : 4.4, 'Jul' : 4.1, 'Ago' : 6.7, 'Sep' : 9.3, 'Oct' : 11.7, 'Nov' : 12.8, 'Dic' : 13.2},
	'Temperatura máxima (°C)' : {
            'Ene' : 20.1, 'Feb' : 19.9, 'Mar' : 19.9, 'Abr' : 19.7, 'May' : 17.3, 'Jun' : 15.6, 'Jul' : 15.4, 'Ago' : 17.4, 'Sep' : 19.2, 'Oct' : 21.1, 'Nov' : 21.7, 'Dic' : 21.3},
	'Temperatura mínima (°C)' : {
            'Ene' : 7.4, 'Feb' : 7.0, 'Mar' : 6.3, 'Abr' : 2.8, 'May' : -3.0, 'Jun' : -6.2, 'Jul' : -6.8, 'Ago' : -4.2, 'Sep' : -1.1, 'Oct' : 2.8, 'Nov' : 5.2, 'Dic' : 6.9},
	'Humedad relativa (%)' : {
            'Ene' : 65.3, 'Feb' : 64.1, 'Mar' : 62.4, 'Abr' : 48.2, 'May' : 34.6, 'Jun' : 31.1, 'Jul' : 30.1, 'Ago' : 31.7, 'Sep' : 34.4, 'Oct' : 45.3, 'Nov' : 52.3, 'Dic' : 59.2},
	'Velocidad del Viento (km/h)' : {
            'Ene' : 6.9, 'Feb' : 7.1, 'Mar' : 6.5, 'Abr' : 6.4, 'May' : 6.0, 'Jun' : 4.9, 'Jul' : 6.6, 'Ago' : 6.6, 'Sep' : 8.6, 'Oct' : 8.7, 'Nov' : 8.8, 'Dic' : 8.3},
	'Nubosidad total (octavos)' : {
            'Ene' : 5.2, 'Feb' : 4.8, 'Mar' : 4.1, 'Abr' : 2.7, 'May' : 1.8, 'Jun' : 1.6, 'Jul' : 1.4, 'Ago' : 1.6, 'Sep' : 2.0, 'Oct' : 3.0, 'Nov' : 3.6, 'Dic' : 4.5},
	'Precipitación (mm)' : {
            'Ene' : 97.5, 'Feb' : 68.4, 'Mar' : 55.9, 'Abr' : 8.2, 'May' : 1.0, 'Jun' : 0.5, 'Jul' : 0.0, 'Ago' : 1.4, 'Sep' : 3.5, 'Oct' : 16.0, 'Nov' : 27.3, 'Dic' : 71.9},
	'Frecuencia de días con Precipitación superior a 0.1 mm' : {
            'Ene' : 15.9, 'Feb' : 12.2, 'Mar' : 9.8, 'Abr' : 2.4, 'May' : 0.3, 'Jun' : 0.1, 'Jul' : 0.0, 'Ago' : 0.4, 'Sep' : 0.9, 'Oct' : 3.5, 'Nov' : 7.4, 'Dic' : 12.7},
    }

    estadisticas.append(libertador)
    print(estadisticas[station_index('Libertador San Martin')])

# create_libertador()

def no_null_data():
    pass

# no_null_data()