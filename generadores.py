from smn import *

# Averiguar:
# ¿En que lugar es el mejor para poner una granja de generadores eólicos?
# Estación meteorológica más cálida del país (campo 'Temperatura máxima (°C)') y la más fria (campo: 'Temperatura mínima (°C)')
# Lugar más húmedo y el más seco del país
# Temperatura promedio durante todo el año en Paraná
# Agregar estación meteorológica de Libertador San Martin (inventar datos)
# Sacar las estaciones que le falten algun dato (dato en null)



def get_values(condition):
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
    sorted_values = sorted(total_values.values(),reverse=True) # make an array that holds the sorted values of the sums
    
    amount_null = 0 # Search null data in sorted values
    for item in sorted_values:
        if item == 0: amount_null+=1

    for i in range(amount_null): # remove from the sorted value null data
        sorted_values.remove(0)

    # print(total_values)
    return total_values,sorted_values

def get_max_value(type_medition):
    total_values,sorted_values = get_values(type_medition)
    for item in total_values: # get Max value of station
        if total_values[item] == sorted_values[0]:
            print(item)
    print(sorted_values[0]) # print max value


def get_min_value(type_medition):
    total_values,sorted_values = get_values(type_medition)
    for item in total_values: # get min value of station
        if total_values[item] == sorted_values[-1]:
            print(item)
    print(sorted_values[-1]) # print min value

def station_index(estation):
    for dict in estadisticas:
        if dict['Estación'] == estation:
            return estadisticas.index(dict)

def get_most_windy_station():
    get_max_value('Velocidad del Viento (km/h)')

def hottest_and_coldest():
    get_max_value('Temperatura máxima (°C)')
    get_min_value('Temperatura mínima (°C)')

def humid_and_dry():
    get_max_value('Humedad relativa (%)')
    get_min_value('Humedad relativa (%)')

def average_in_parana():
    # 'PARANÁ AERO'
    print(station_index('PARANÁ AERO'))
    print(estadisticas[station_index('PARANÁ AERO')])

average_in_parana()

def create_in_libertador():
    print()

def delete_null():
    print()
