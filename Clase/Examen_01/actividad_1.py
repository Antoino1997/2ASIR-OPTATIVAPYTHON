def contar_apariciones(nombre_elemento:  str) -> None:
    elementos = ["python", "java", "python", "c", "python", "go", "java"]
    if nombre_elemento in elementos:
        elemento_contado = elementos.count(nombre_elemento)
        if elemento_contado >= 1:
            print(f"El elemento {nombre_elemento} aparece {elemento_contado} veces")
        else:
            return
    else:
        print(f"El elemento {nombre_elemento} no está en la lista")



contar_apariciones("python")
contar_apariciones("java")
contar_apariciones("ruby")
