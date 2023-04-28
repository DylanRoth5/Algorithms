from smn import *

# Averiguar:
# ¿En que lugar es el mejor para poner una granja de generadores eólicos?
# Estación meteorológica más cálida del país (campo 'Temperatura máxima (°C)') y la más fria (campo: 'Temperatura mínima (°C)')
# Lugar más húmedo y el más seco del país
# Temperatura promedio durante todo el año en Paraná
# Agregar estación meteorológica de Libertador San Martin (inventar datos)
# Sacar las estaciones que le falten algun dato (dato en null)



def get_most_wind(veriable):
    total_values = {}
    for estacion in estadisticas:
        index= 0
        for key in estacion:
            sum_values = 0
            for month in estacion[veriable]:
                value = (estacion[veriable][month])
                # if(index == 0):
                    # print(f'{value}|',end='')
                if value == None:
                    sum_values += 0
                else:
                    sum_values += value
            index+=1
            sum_values = round(sum_values,2)
        # print()
        total_values[estacion['Estación']]=sum_values
        # print(estacion['Estación'])
        # print(sum_values)
    print(len(total_values.items()))

get_most_wind('Velocidad del Viento (km/h)')

def hottest_and_coldest():
    print()

def humid_and_dry():
    print()

def average_in_parana():
    print()

def create_in_libertador():
    print()

def delete_null():
    print()





# i=1
# prom_velocidades = []
# lugares = []
# for place in estadisticas:
#     # print(f'{i} - ', end='')
#     i+=1
#     # print(place['Estación'])
#     suma_velocidades=0
#     for mes in place['Velocidad del Viento (km/h)']:
#         # print(f' {mes}:',end='')
#         velocidad = str(place['Velocidad del Viento (km/h)'][mes])
#         # print(velocidad,end='')
#         if (velocidad == "None"):
#             suma_velocidades = float(0.0)
#         else:
#             suma_velocidades += float(velocidad)
#     prom_velocidades.append(suma_velocidades/12)

# i=0
# for place in estadisticas:
#     # print(place['Estación'],end='')
#     # print(f':{round(prom_velocidades[i],2)}        ',end='')
#     if i == 0:
#         lugares.append({place['Estación'] : round(prom_velocidades[i],2)})
#         print("\033[92m" + f'{round(prom_velocidades[i],2)}' + "\033[0m")
#     else:
#         for prom_vel in lugares:
#             if prom_velocidades[i] < prom_velocidades[i-1]:
#                 print("\033[91m" + f'{round(prom_velocidades[i],2)} es menor que {round(prom_velocidades[i-1],2)}' + "\033[0m")
#                 # lugares.append({place['Estación'] : round(prom_velocidades[i],2)})
#             elif prom_velocidades[i] > prom_velocidades[i-1]:
#                 print("\033[92m" + f'{round(prom_velocidades[i],2)} es mayor que {round(prom_velocidades[i-1],2)}' + "\033[0m")
#                 # lugares.insert({place['Estación'] : round(prom_velocidades[i],2)})
            

    
#     i+=1

# print(lugares)
# # print(lugares[{}].sort())

