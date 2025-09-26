num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
oper = (input('Escoge un operador (suma, resta, multiplicacion, division): '))

if oper == "suma":
    print(num1 + num2)
elif oper == "resta":
    print(num1 - num2)
elif oper == "multiplicacion":
    print(num1 * num2)
elif oper == "division":
    print(num1 / num2)
else:
    print("Escoge un operador valido")

