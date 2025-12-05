def recorrer_iterador() -> None:
    valores = [10, 20, 30, 40]
    it = iter(valores)
    elemento = next(it, None)

    while elemento is not None:
        print(f"Valor: {elemento}")
        elemento = next(it, None)

recorrer_iterador()