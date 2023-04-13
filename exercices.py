#programa que muestre N elementos de la secuencia de fibonacci

# n = int(input('numero de elementos a mostrar de fibonacci'))
# index = int(0)
# a = 0
# b = 1
# sum = a+b
# print(f'{a} -> {b}',end='')
# while (index<n):
#     sum = a+b
#     print(f' -> {b}',end='')
#     a = b
#     b = sum
#     index = index + 1

#funcion que recibiendo la longitud de los tres lados de un triangulo nos diga si es escaleno, equilatero o isoseles

# a = int(input(''))
# b = int(input(''))
# c = int(input(''))
# if a<(b+c) and b<(a+c) and c<(a+b):
#   print('Si a =',a,', b =',b,'y c =',c,' entonces si se puede hacer un triangulo')
#   if a==b==c:
#     print('Equilatero')
#   elif a==b or b==c or a==c:
#     print('Isósceles')
#   else:
#     print('Escaleno')
# else:
#   print('Si a =',a,', b =',b,'y c =',c,' entonces no se puede hacer un triangulo')

#funcion que recibiendo un numero <= 1000 lo convierta en numero romano y muestre el resultado por pantalla

# def intToRoman(num):
#     m = ["", "M", "MM", "MMM"]
#     c = ["", "C", "CC", "CCC", "CD", "D",
#          "DC", "DCC", "DCCC", "CM "]
#     x = ["", "X", "XX", "XXX", "XL", "L",
#          "LX", "LXX", "LXXX", "XC"]
#     i = ["", "I", "II", "III", "IV", "V",
#          "VI", "VII", "VIII", "IX"]
    
#     thousands = m[num // 1000]
#     hundreds = c[(num % 1000) // 100]
#     tens = x[(num % 100) // 10]
#     ones = i[num % 10]
  
#     ans = (thousands + hundreds +
#            tens + ones)
  
#     return ans

# if __name__ == "__main__":
#     number = int(input('pon tu numero para converir: '))
#     print(intToRoman(number))

def convertir(entero):
    nat=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    rom=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

    romano=''
    nat = entero
    i=0

    while i<13:
        for x in range (entero//nat[i]):
            romano += rom[i]
            entero -= nat[i]
        i+=1
    return romano

print(convertir(int(59)))
