a = int(input("a = "))
b = int(input("b = "))

def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b

def restar(a, b):
    """Devuelve la resta de a y b."""
    return a - b

def multiplicar(a, b):
    """Devuelve la multiplicación de a por b."""
    return a * b

def dividir(a, b):
    """Devuelve la división de a entre b, controlando las divisiónes por 0."""
    if b != 0:
        return a / b
    else:
        return 0

print("La suma es:", sumar(a, b))
print("La resta es:", restar(a, b))
print("La multiplicación es:", multiplicar(a, b))
print("La división es:", dividir(a, b))
