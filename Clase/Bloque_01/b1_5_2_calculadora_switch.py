num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
oper = (input('Escoge un operador (suma, resta, multiplicacion, division): '))

match oper:
    case "suma":
        print(num1 + num2)
    case "resta":
        print(num1 - num2)
    case "multiplicacion":
        print(num1 * num2)
    case "division":
        print(num1 / num2)
    case  _:
        print("Escoge un operador valido")
