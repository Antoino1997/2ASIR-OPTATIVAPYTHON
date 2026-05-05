"""
gestor_notas.py
Programa de consola para gestionar un archivo de notas (notas.txt).
Permite ver, añadir y eliminar notas, con manejo de excepciones y
uso de la instrucción with para asegurar el cierre automático de ficheros.
"""

ARCHIVO = "notas.txt"


def leer_notas():
    """Lee todas las notas del archivo y las devuelve como lista."""
    modo = "r"
    try:
        with open(ARCHIVO, modo, encoding="utf-8") as f:
            notas = f.readlines()
        # Eliminar saltos de línea sobrantes
        notas = [nota.strip() for nota in notas if nota.strip()]
        return notas
    except FileNotFoundError:
        return None
    except PermissionError:
        print("❌ No tienes permisos para acceder al archivo.")
        return []


def crear_archivo_vacio():
    """Crea el archivo de notas vacío si no existe."""
    modo = "w"
    try:
        with open(ARCHIVO, modo, encoding="utf-8") as f:
            pass  # Solo se crea el archivo vacío
        print("📄 Archivo creado vacío automáticamente.")
    except PermissionError:
        print("❌ No tienes permisos para crear el archivo.")


def mostrar_notas(notas):
    """Muestra todas las notas numeradas por pantalla."""
    if not notas:
        print("(No hay notas guardadas.)")
    else:
        print("\nNotas actuales:")
        for i, nota in enumerate(notas, start=1):
            print(f"{i}. {nota}")


def anadir_nota(texto):
    """Añade una nueva nota al final del archivo."""
    modo = "a"
    try:
        with open(ARCHIVO, modo, encoding="utf-8") as f:
            f.write(texto + "\n")
        print("✅ Nota guardada con éxito.")
    except FileNotFoundError:
        print("❌ El archivo no existe.")
    except PermissionError:
        print("❌ No tienes permisos para escribir en el archivo.")


def eliminar_nota(numero):
    """Elimina la nota correspondiente al número indicado."""
    notas = leer_notas()
    if notas is None:
        print("❌ El archivo no existe.")
        return
    if numero < 1 or numero > len(notas):
        print("❌ Número de nota inválido.")
        return
    notas.pop(numero - 1)
    # Reescribir el archivo con las notas restantes
    modo = "w"
    try:
        with open(ARCHIVO, modo, encoding="utf-8") as f:
            for nota in notas:
                f.write(nota + "\n")
        print("✅ Nota eliminada correctamente.")
    except PermissionError:
        print("❌ No tienes permisos para modificar el archivo.")


def menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Menú ---")
    print("1. Ver notas")
    print("2. Añadir nota")
    print("3. Eliminar nota")
    print("4. Salir")


# ──────────────────────────────────────────
# Programa principal
# ──────────────────────────────────────────

print("📓 Gestor de Notas")

# Al iniciar: comprobar si el archivo existe
notas_iniciales = leer_notas()

if notas_iniciales is None:
    print("⚠️  El archivo no existe.")
    crear_archivo_vacio()
else:
    print(f"Archivo encontrado: {ARCHIVO}")
    mostrar_notas(notas_iniciales)

# Bucle principal del menú
while True:
    menu()
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        # Ver notas
        notas = leer_notas()
        if notas is not None:
            mostrar_notas(notas)

    elif opcion == "2":
        # Añadir nota
        texto = input("\nEscribe la nueva nota: ").strip()
        if texto:
            anadir_nota(texto)
        else:
            print("❌ No puedes añadir una nota vacía.")

    elif opcion == "3":
        # Eliminar nota
        notas = leer_notas()
        if notas is not None:
            mostrar_notas(notas)
            try:
                numero = int(input("\nNúmero de nota a eliminar: ").strip())
                eliminar_nota(numero)
            except ValueError:
                print("❌ Debes introducir un número válido.")

    elif opcion == "4":
        # Salir
        print("\n👋 ¡Hasta la próxima!")
        break

    else:
        print("❌ Opción no válida. Elige entre 1 y 4.")
