"""
Al principio había puesto "nota1 + nota2 + nota3 / 3"
Por lo que primero se resolvia la división de nota3 / 3 y luego el resto de sumas.
Para arreglarlo he metido las sumas entre paréntesis para que se resuelvan primero
y luego se dividan entre 3.
"""
nota1 = int(input("Introduzca la primera nota: "))
nota2 = int(input("Introduzca la segunda nota: "))
nota3 = int(input("Introduzca la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"El promedio de las  3 notas es {promedio}")
