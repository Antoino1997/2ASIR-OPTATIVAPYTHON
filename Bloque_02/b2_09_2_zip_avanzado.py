estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]
resultado_final = {}

for a, b, c, d in zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica):
    promedio = round((b + c + d) / 3, 2)
    estado = []

    if promedio < 5:
        estado = "Reprobado"
    elif 5 <= promedio < 6.5:
        estado = "En recuperación"
    else:
        estado = "Aprobado"

    resultado_final.update({a: {"Matemáticas": b, "Física": c, "Química": d, "Promedio": promedio, "Estado": estado}})

    print(a, "-", "Matemáticas:", b, "Física:", c, "Química:", d, "Promedio:", promedio, "Estado:", estado)
