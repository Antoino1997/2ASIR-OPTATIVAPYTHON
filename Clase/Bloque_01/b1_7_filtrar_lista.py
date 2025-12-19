"""Lista de nombres"""
lista = ["Antonio", "Pepe", "Roddy", "Ivan", "Pablo", "Jesus", "Adrian"] #Lista con los nombres que queremos recorrer

"""Bucle que recorre todas las entradas del array"""
for nombre in lista: #for que recoge todos los datos del array
    if nombre.startswith(("A", "a")): #if para coger los nombres que empiezan por "A" o por "a"
        continue #Se salta esa entrada
    print(nombre) #Muestra por pantalla la lista de nombres actualizada
