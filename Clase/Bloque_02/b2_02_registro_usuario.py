def registrar_usuario(nombre, edad, ciudad="Madrid"):
    """Muestra los datos básicos del usuario."""
    print(f"Usuario: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

# Llamadas válidas
registrar_usuario("Antonio", 28, "Huelva") #Posicionales
registrar_usuario("Antonio", 28) #Ciudad omitida

registrar_usuario(ciudad="Huelva", nombre="Antonio", edad=28) #Argumentos desordenados
