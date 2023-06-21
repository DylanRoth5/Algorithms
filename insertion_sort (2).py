def insertion_sort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
              
        #Iterara e ir comparando el valor rescatado con cada elemento de la izquierda
        #hasta encontrar un valor menor a este
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Ubicar el valor rescatado justo por delante del valor menor a este
        array[j + 1] = key
        print(array)


data = [20, 11, 16, 9, 12, 14, 17, 19, 13, 15]

print('Original: ')
print(data)
insertion_sort(data)
print('Ordenado: ')
print(data)
