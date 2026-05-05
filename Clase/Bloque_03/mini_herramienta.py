"""
mini_herramienta.py
Programa de consola con menú que combina módulos estándar (math, os)
y una librería externa (requests) para realizar distintas operaciones.
"""

import math
import os

import requests


def calculos_matematicos():
    """Pide un número al usuario y muestra su raíz cuadrada, factorial y potencia al cuadrado."""
    try:
        numero = int(input("\nIntroduce un número: "))
        print("Raíz cuadrada:", math.sqrt(numero))
        print("Factorial:", math.factorial(numero))
        print("Potencia al cuadrado:", math.pow(numero, 2))
    except ValueError:
        print("❌ Debes introducir un número entero válido.")


def explorador_directorios():
    """Muestra el directorio actual, lista sus archivos y permite crear una nueva carpeta."""
    print("\nDirectorio actual:", os.getcwd())
    print("Archivos en la carpeta:")
    for nombre in os.listdir("."):
        print("-", nombre)

    respuesta = input("¿Quieres crear una nueva carpeta? (s/n): ").strip().lower()
    if respuesta == "s":
        nombre_carpeta = input("Introduce el nombre de la carpeta: ").strip()
        try:
            os.mkdir(nombre_carpeta)
            print("✅ Carpeta creada con éxito.")
        except FileExistsError:
            print("❌ Ya existe una carpeta con ese nombre.")
        except PermissionError:
            print("❌ No tienes permisos para crear la carpeta.")
    else:
        print("Volviendo al menú...")


def consulta_api():
    """Realiza una petición GET a la API de GitHub y muestra el resultado."""
    url = "https://api.github.com"
    print(f"\nPetición a {url}")
    try:
        respuesta = requests.get(url)
        print("Código de estado:", respuesta.status_code)
        print("Tamaño de la respuesta:", len(respuesta.text), "caracteres")
        print("Contenido (200 caracteres):")
        print(respuesta.text[:200])
    except requests.ConnectionError:
        print("❌ No se pudo conectar. Comprueba tu conexión a internet.")


def menu():
    """Muestra el menú principal de opciones."""
    print("\n--- Menú de Herramientas ---")
    print("1. Cálculos matemáticos")
    print("2. Explorador de directorios")
    print("3. Consulta a API (requests)")
    print("4. Salir")


# ──────────────────────────────────────────
# Programa principal
# ──────────────────────────────────────────

while True:
    menu()
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        calculos_matematicos()

    elif opcion == "2":
        explorador_directorios()

    elif opcion == "3":
        consulta_api()

    elif opcion == "4":
        print("\n👋 ¡Hasta la próxima!")
        break

    else:
        print("❌ Opción no válida. Elige entre 1 y 4.")
