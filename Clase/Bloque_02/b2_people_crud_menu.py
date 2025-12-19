people = {}  # Main dictionary: {nif: {name, age, city, profession}}


def create_person():
    """Create a new person and add to the dictionary."""
    nif = input("Introduce tu DNI: ")

    people[nif] = {
        "name" : input("Introduce tu nombre: "),
        "age" : input("Introduce tu edad: "),
        "city" : input("Introduce tu ciudad: "),
        "profession" : input("Introduce tu trabajo: ")
    }

def read_people():
    """Display searched registered people."""
    nif = input("Introduce el DNI a buscar: ")
    if nif in people:
        print(f"El DNI {nif} existe, esta es la información:")
        print(people[nif])
    else:
        print("DNI no encontrado.")

def read_list():
    """Display searched list"""
    search_id = int(input("Introduce el número de DNIs a buscar: "))
    lista = []

    for i in range(search_id):
        nif = input("Introduce el DNI a añadir a la lista: ")
        lista.append(nif)

    for i in lista:
        print(i)
        print(people[i])

def update_person():
    """Update information of an existing person."""
    nif = input("Introduce el DNI a actualizar: ")
    if nif in people:
        dato_key = input("Introduce el dato a cambiar (name, age, city, profession): ")
        if dato_key in people[nif]:
            dato_valor = input("Introduce el nuevo valor: ")

            people[nif].update({dato_key : dato_valor})
        else:
            print(f"{dato_key} no es un apartado")
    else:
        print(f"{nif} no encontrado")


def delete_person():
    """Delete a person by ID."""
    nif = input("Introduce el DNI a eliminar: ")

    del people[nif]


# 🔸 Main menu
option = ""

while option != "5":
    print("\n=== PEOPLE CRUD MENU ===")
    print("1. Create person")
    print("2. Read people")
    print("3. Read multiple peoples")
    print("4. Update person")
    print("5. Delete person")
    print("6. Exit")

    option = input("Choose an option: ")

    match option:
        case "1":
            create_person()
        case "2":
            read_people()
        case "3":
            read_list()
        case "4":
            update_person()
        case "5":
            delete_person()
        case "6":
            print("Exiting program...")
        case _:
            print("Invalid option. Please choose 1–5.")
