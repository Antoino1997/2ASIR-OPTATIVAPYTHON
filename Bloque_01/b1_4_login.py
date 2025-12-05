usuario_correcto = "admin"
contraseña_correcta = "1234"

usuario_introducido = input("Introduzca el nombre de usuario: ")
contraseña_introducida = input("Introduzca una contraseña: ")

if (usuario_introducido == usuario_correcto) and (contraseña_introducida == contraseña_correcta):
    print("Acceso concedido")
else:
    print("Acceso denegado")
