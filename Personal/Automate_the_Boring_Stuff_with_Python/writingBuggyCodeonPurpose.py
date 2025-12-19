# 1. NameError: name 'spam' is not defined
# Ocurre cuando llamas a algo que no existe.
# print(spam)

# 2. ValueError: invalid literal for int() with base 10: 'five'
# Ocurre al intentar convertir texto no numérico en entero.
# number = int('five')

# 3. SyntaxError: invalid syntax. (Maybe you meant '=='...?)
# Ocurre al usar un solo '=' en un 'if'.
# if 5 = 5: print("Error")

# 4. SyntaxError: unterminated string literal
# Ocurre al olvidar cerrar unas comillas.
# print("Hola mundo)

# 5. NameError: name 'true' is not defined. Did you mean: 'True'?
# Ocurre por no poner la mayúscula inicial en los booleanos.
# valor = true

# 6. IndentationError: expected an indented block after 'if'
# Ocurre cuando el bloque de código no tiene sangría.
# if True:
# print("Fallo de sangría")

# 7. TypeError: can only concatenate str (not "int") to str
# Ocurre al sumar (pegar) un String + Int.
# print("Nota: " + 10)

# 8. TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Ocurre al sumar un Int + String (el orden importa para el mensaje).
# print(10 + " puntos")