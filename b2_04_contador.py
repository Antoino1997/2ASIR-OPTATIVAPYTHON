contador = 0

def incrementar():
    """Incrementa en 1 el contador."""
    global contador
    contador += 1

def decrementar():
    """Decrementa en 1 el contador."""
    global contador
    contador -= 1

def mostrar_contador():
    """Imprime el valor actual del contador."""
    print(contador)

incrementar()
incrementar()
decrementar()
mostrar_contador()
