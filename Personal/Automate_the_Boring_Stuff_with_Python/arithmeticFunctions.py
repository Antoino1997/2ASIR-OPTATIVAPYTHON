def plus_one(number):
    return number + 1

def add(number1, number2):
    total_sum = number1
    for i in range(number2):
        total_sum = plus_one(total_sum)
    return total_sum

def multiply(number1, number2):
    total_product = 0

    for i in range(number2):
        total_product = add(total_product, number1)

    return total_product

print(f"Sum -> 4 + 3: {add(4, 3)}")
print(f"Multiplication -> 4 * 3: {multiply(4, 3)}")

# DEBUGGING
# En caso de que queramos ver el flujo de operaciones, tenemos que introducir prints dentro de los loops para ver lo que hace paso a paso
# He incluido \n para que se vea el flujo de bloques de operaciones

def plus_one(number):
    return number + 1

def add(number1, number2):
    print(f"\n--- Sumando {number1} + {number2} ---")
    total_sum = number1
    for i in range(number2):
        total_sum = plus_one(total_sum)
        print(f"Paso {i+1}: He llamado a plus_one, ahora el total es {total_sum}")
    return total_sum

def multiply(number1, number2):
    print(f"\n=== Multiplicando {number1} * {number2} ===")
    total_product = 0
    for i in range(number2):
        total_product = add(total_product, number1)
        print(f"Resultado parcial tras sumar {number1} (vuelta {i+1}): {total_product}")
    return total_product

resultado = multiply(4, 3)
print(f"\nResultado final: {resultado}")