lista = []

"""Recorre 5 veces la interacción para añadir 5 objetos a la lista."""
for objeto in range(5):
    lista.append(input(f"Introduzca el objeto {objeto}: "))

"""Imprime la lista con los 5 objetos añadidos."""
print("Aqui tiene la lista con los objetos que ha introducido:", lista)

"""Elimina el objeto que se introduce y se imprime la lista sin el objeto."""
lista.remove(input("Introduzca el objeto que quiere eliminar: "))
print("Aqui tiene la lista sin el objeto:", lista)

"""Se ordena la lista alfabéticamente y se imprime."""
lista.sort()
print("Aqui tiene la lista ordenada:", lista)

