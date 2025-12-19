'''
Programa que contiene una lista de los números del 1 hasta el 20.
Luego genera listas con los cuadrados, los pares, los que son mayor que 10 y
un diccionario con el número original y su doble.
Finalmente se muestran todas las listas por pantallas
'''

lista = [n for n in range(1, 21)]
cuadrados = [n ** 2 for n in lista]
pares = [n for n in lista if (n) % 2 == 0]
mayorque10 = [n for n in lista if n > 10]
doble = {n: n * 2 for n in lista}

print("Lista original:", lista)
print("Lista con los números al cuadrado:", cuadrados)
print("Lista con los números pares:", pares)
print("Lista con los números mayores que 10:", mayorque10)
print("Diccionario con el número y su doble:", doble)
