compras = []

"""Recorre 5 veces la interacción para añadir 5 objetos a la lista."""
for objeto in range(5):
    compras.append(input(f"Introduzca el objeto {objeto + 1}: "))

"""Imprime la lista con los 5 objetos añadidos."""
print("Aqui tiene la lista con los objetos que ha introducido:", compras)

"""Elimina el objeto que se introduce y se imprime la lista sin el objeto."""
compras.remove(input("Introduzca el objeto que quiere eliminar: "))
print("Aqui tiene la lista sin el objeto:", compras)

"""Se ordena la lista alfabéticamente y se imprime."""
compras.sort()
print("Aqui tiene la lista ordenada:", compras)
