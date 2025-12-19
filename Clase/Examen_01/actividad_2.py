def gestionar_persona() -> None:
    persona = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}

    print("nombre:", persona.get("nombre"))
    print("edad:", persona.get("edad"))
    print("ciudad:", persona.get("ciudad"))

    persona.update({"profesion":"Ingeniera"})

    persona.pop("ciudad")

    for clave, valor in persona.items():
        print(f"{clave}: {valor}")

gestionar_persona()