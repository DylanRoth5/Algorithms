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


data = [9, 5, 1, 4, 3]
print('Original: ')
print(data)
insertion_sort(data)
print('Ordenado: ')
print(data)
