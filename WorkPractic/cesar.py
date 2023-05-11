# Objetivo:
# 1) Generar un algoritmo que permita el ingreso de una frase y nro de desplazamiento x y le aplique el cifrado César.
# 2) Algoritmo del camino inverso al punto 1
# 3) Puntos extras: un algoritmo que con solo ingresar la frase cifrada logre encontrar el nro de desplazamiento que se usó y la descifre.

# Reglas de cifrado:
# 1) Usar el método de cifrado César
# 2) Usar palabras del diccionario en español
# 3) Se puede desplazar arbitrariamente el alfabeto
# 4) Separar espacios entre palabras
# 5) No codificar los espacios
# 6) Se sugiere usar una frase de algún famoso inspiradora
# 7)“Soy optimista, no veo que sea útil ser otra cosa” WChurchill

def cifrado_cesar():
    # word = input('Input para cifrar')
    phrase = 'soy optimista'

def cifrado_cesar(frase, desplazamiento):
    resultado = ""
    
    # Iterar a través de cada carácter en la frase
    for caracter in frase:
        # Verificar si el carácter es una letra
        if caracter.isalpha():
            # Obtener el código ASCII del carácter y restar el código base
            codigo_base = ord('a') if caracter.islower() else ord('A')
            codigo = ord(caracter) - codigo_base
            
            # Aplicar el desplazamiento y asegurarse de que esté dentro del rango de letras
            nuevo_codigo = (codigo + desplazamiento) % 26
            
            # Obtener el nuevo carácter y añadirlo al resultado
            nuevo_caracter = chr(nuevo_codigo + codigo_base)
            resultado += nuevo_caracter
        else:
            # Si el carácter no es una letra, añadirlo al resultado sin cambios
            resultado += caracter
    
    return resultado

def descifrado_cesar(frase_cifrada, desplazamiento):
    resultado = ""

    # Iterar a través de cada carácter en la frase cifrada
    for caracter in frase_cifrada:
        # Verificar si el carácter es una letra
        if caracter.isalpha():
            # Obtener el código ASCII del carácter y restar el código base
            codigo_base = ord('a') if caracter.islower() else ord('A')
            codigo = ord(caracter) - codigo_base

            # Aplicar el desplazamiento inverso y asegurarse de que esté dentro del rango de letras
            nuevo_codigo = (codigo - desplazamiento) % 26

            # Obtener el nuevo carácter y añadirlo al resultado
            nuevo_caracter = chr(nuevo_codigo + codigo_base)
            resultado += nuevo_caracter
        else:
            # Si el carácter no es una letra, añadirlo al resultado sin cambios
            resultado += caracter

    return resultado

def descifrado_cesar_auto(frase_cifrada):
    palabras_comunes = ['hola', 'mundo', 'hoy', 'bien', 'gracias', 'soy']  # Lista de palabras comunes en el idioma correspondiente

    for desplazamiento in range(26):
        resultado = ""

        for caracter in frase_cifrada:
            if caracter.isalpha():
                codigo_base = ord('a') if caracter.islower() else ord('A')
                codigo = ord(caracter) - codigo_base

                nuevo_codigo = (codigo - desplazamiento) % 26
                nuevo_caracter = chr(nuevo_codigo + codigo_base)
                resultado += nuevo_caracter
            else:
                resultado += caracter

        # Verificar si la frase descifrada contiene algunas palabras comunes
        palabras_encontradas = [palabra for palabra in palabras_comunes if palabra in resultado.lower()]

        if len(palabras_encontradas) > 0:
            return desplazamiento, resultado

    return None, None



frase_original = 'soy optimista'
desplazamiento = 7


frase_cifrada = cifrado_cesar(frase_original, desplazamiento)
print("Frase cifrada:", frase_cifrada)
frase_descifrada = descifrado_cesar(frase_cifrada, desplazamiento)
print("Frase descifrada:", frase_descifrada)


desplazamiento, frase_descifrada = descifrado_cesar_auto(frase_cifrada)

if desplazamiento is not None:
    print("Número de desplazamiento encontrado:", desplazamiento)
    print("Frase descifrada:", frase_descifrada)
else:
    print("No se encontró el número de desplazamiento.")