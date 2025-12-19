estudiantes = {
    "Ana": [8, 7, 9],
    "Luis": [7, 6, 8],
    "Marta": [9, 10, 9],
    "Carlos": [6, 7, 5],
    "Laura": [10, 9, 10]
}

iterador_estudiantes = iter(estudiantes)

while True:
    try:
        nombre = next(iterador_estudiantes)
        notas = estudiantes[nombre]

        promedio = round(sum(notas) / len(notas), 2)

        if promedio < 5:
            estado = "Reprobado"
        elif 5 <= promedio < 6.5:
            estado = "En recuperación"
        else:
            estado = "Aprobado"

        print(f"{nombre} - Notas: {notas}, Promedio: {promedio}, Estado: {estado}")

    except StopIteration:
        break
