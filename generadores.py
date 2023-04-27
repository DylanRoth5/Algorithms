# estadisticas = array(
#     array(
#         'Estación' => 'Nombre de la estación',
#         'Temperatura (°C)' => array('Ene' => '12.8', 'Feb' => '12.5', 'Mar' => '12.4', 'Abr' => '10.9', 'May' => '6.9', 'Jun' => '4.4', 'Jul' => '4.1', 'Ago' => '6.7', 'Sep' => '9.3', 'Oct' => '11.7', 'Nov' => '12.8', 'Dic' => '13.2'),
#         'Temperatura máxima (°C)' => array('Ene' => '20.1', 'Feb' => '19.9', 'Mar' => '19.9', 'Abr' => '19.7', 'May' => '17.3', 'Jun' => '15.6', 'Jul' => '15.4', 'Ago' => '17.4', 'Sep' => '19.2', 'Oct' => '21.1', 'Nov' => '21.7', 'Dic' => '21.3'),
#         'Temperatura mínima (°C)' => array('Ene' => '7.4', 'Feb' => '7.0', 'Mar' => '6.3', 'Abr' => '2.8', 'May' => '-3.0', 'Jun' => '-6.2', 'Jul' => '-6.8', 'Ago' => '-4.2', 'Sep' => '-1.1', 'Oct' => '2.8', 'Nov' => '5.2', 'Dic' => '6.9'),
#         'Humedad relativa (%)' => array('Ene' => '65.3', 'Feb' => '64.1', 'Mar' => '62.4', 'Abr' => '48.2', 'May' => '34.6', 'Jun' => '31.1', 'Jul' => '30.1', 'Ago' => '31.7', 'Sep' => '34.4', 'Oct' => '45.3', 'Nov' => '52.3', 'Dic' => '59.2'),
#         'Velocidad del Viento (km/h)' => array('Ene' => '6.9', 'Feb' => '7.1', 'Mar' => '6.5', 'Abr' => '6.4', 'May' => '6.0', 'Jun' => '4.9', 'Jul' => '6.6', 'Ago' => '6.6', 'Sep' => '8.6', 'Oct' => '8.7', 'Nov' => '8.8', 'Dic' => '8.3'),
#         'Nubosidad total (octavos)' => array('Ene' => '5.2', 'Feb' => '4.8', 'Mar' => '4.1', 'Abr' => '2.7', 'May' => '1.8', 'Jun' => '1.6', 'Jul' => '1.4', 'Ago' => '1.6', 'Sep' => '2.0', 'Oct' => '3.0', 'Nov' => '3.6', 'Dic' => '4.5'),
#         'Precipitación (mm)' => array('Ene' => '97.5', 'Feb' => '68.4', 'Mar' => '55.9', 'Abr' => '8.2', 'May' => '1.0', 'Jun' => '0.5', 'Jul' => '0.0', 'Ago' => '1.4', 'Sep' => '3.5', 'Oct' => '16.0', 'Nov' => '27.3', 'Dic' => '71.9'),
#         'Frecuencia de días con Precipitación superior a 0.1 mm' => array('Ene' => '15.9', 'Feb' => '12.2', 'Mar' => '9.8', 'Abr' => '2.4', 'May' => '0.3', 'Jun' => '0.1', 'Jul' => '0.0', 'Ago' => '0.4', 'Sep' => '0.9', 'Oct' => '3.5', 'Nov' => '7.4', 'Dic' => '12.7'),
#     )
# )

from smn import *

# Averiguar:
# ¿En que lugar es el mejor para poner una granja de generadores eólicos?
# Estación meteorológica más cálida del país (campo 'Temperatura máxima (°C)') y la más fria (campo: 'Temperatura mínima (°C)')
# Lugar más húmedo y el más seco del país
# Temperatura promedio durante todo el año en Paraná
# Agregar estación meteorológica de Libertador San Martin (inventar datos)
# Sacar las estaciones que le falten algun dato (dato en null)
i=1
prom_velocidades = []
lugares = []
for place in estadisticas:
    # print(f'{i} - ', end='')
    i+=1
    # print(place['Estación'])
    suma_velocidades=0
    for mes in place['Velocidad del Viento (km/h)']:
        # print(f' {mes}:',end='')
        velocidad = str(place['Velocidad del Viento (km/h)'][mes])
        # print(velocidad,end='')
        if (velocidad == "None"):
            suma_velocidades = float(0.0)
        else:
            suma_velocidades += float(velocidad)
    prom_velocidades.append(suma_velocidades/12)

i=0
for place in estadisticas:
    # print(place['Estación'],end='')
    # print(f':{round(prom_velocidades[i],2)}        ',end='')
    if i == 0:
        lugares.append({place['Estación'] : round(prom_velocidades[i],2)})
        print("\033[92m" + f'{round(prom_velocidades[i],2)}' + "\033[0m")
    else:
        for prom_vel in lugares:
            if prom_velocidades[i] < prom_velocidades[i-1]:
                print("\033[91m" + f'{round(prom_velocidades[i],2)} es menor que {round(prom_velocidades[i-1],2)}' + "\033[0m")
                # lugares.append({place['Estación'] : round(prom_velocidades[i],2)})
            elif prom_velocidades[i] > prom_velocidades[i-1]:
                print("\033[92m" + f'{round(prom_velocidades[i],2)} es mayor que {round(prom_velocidades[i-1],2)}' + "\033[0m")
                # lugares.insert({place['Estación'] : round(prom_velocidades[i],2)})
            

    
    i+=1

print(lugares)
# print(lugares[{}].sort())

