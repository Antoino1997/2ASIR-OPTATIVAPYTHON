'''
Se pide al usuario introducir 3 contactos para introducirlos en un diccionario.
Luego se le pide buscar al usuario un contacto mediante el nombre.
'''

agenda = {}

for objeto in range(3):
    key = input("Introduce nombre: ")
    value = input("Introduce teléfono: ")
    agenda[key]=value

print("Agenda completa:")
for clave, valor in agenda.items():
    print(clave, ":", valor)

buscar = agenda.get(input("Buscar contacto: "), "Contacto no encontrado")
print(buscar)
