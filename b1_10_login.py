"""
Programa sencillo de gestión de usuarios en memoria.

Este programa permite:
1. Registrar usuarios con email y contraseña.
2. Validar los datos introducidos (email y contraseña).
3. Iniciar sesión verificando el email y la contraseña.
4. Salir del programa.

Los usuarios se almacenan en un diccionario en memoria (no se guardan en disco).
"""

# Diccionario para almacenar usuarios registrados: {email: contraseña}
usuarios = {}

while True:
    # Menú principal
    print("\n===== MENÚ PRINCIPAL =====")
    print("[1] Registrarse")
    print("[2] Iniciar sesión")
    print("[3] Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\n--- REGISTRO DE USUARIO ---")

        # Registro de email
        while True:
            identifer = input("Introduce tu email: ")

            # Validaciones del email
            if len(identifer) < 3:
                print("❌ El email debe tener al menos 3 caracteres.")
                continue
            if "@" not in identifer:
                print("❌ El email debe contener '@'.")
                continue
            if not (".com" in identifer or ".es" in identifer or ".net" in identifer):
                print("❌ El email debe contener una extensión válida (.com, .es, .net).")
                continue
            if ("!" in identifer or "#" in identifer or "$" in identifer or "%" in identifer or
                    "&" in identifer or "*" in identifer or "?" in identifer or "," in identifer):
                print("❌ El email no debe contener símbolos especiales (!#$%&*?, etc.)")
                continue
            if identifer in usuarios:
                print("⚠️ Este email ya está registrado.")
                continue
            break

        # Registro de contraseña
        while True:
            password = input("Crea una contraseña: ")

            # Validaciones de contraseña
            if len(password) < 8:
                print("❌ La contraseña debe tener al menos 8 caracteres.")
                continue

            # Debe contener al menos una mayúscula
            for c in password:
                if "A" <= c <= "Z":
                    break
            else:
                print("❌ La contraseña debe contener al menos una mayúscula.")
                continue

            # Debe contener al menos un número
            for c in password:
                if "0" <= c <= "9":
                    break
            else:
                print("❌ La contraseña debe contener al menos un número.")
                continue

            # Debe contener al menos un símbolo especial
            for c in password:
                if c in "!@#$%&*?,":
                    break
            else:
                print("❌ La contraseña debe contener al menos un símbolo especial (!@#$%&*?, etc.)")
                continue

            break  # Si pasa todas las validaciones

        # Guardar usuario en el diccionario
        usuarios[identifer] = password
        print("✅ Usuario registrado.")

    elif opcion == "2":
        print("\n--- INICIO DE SESIÓN ---")
        identifer = input("Email: ")

        # Comprobar si el usuario existe
        if identifer not in usuarios:
            print("Acceso denegado ⛔")
            continue

        # Intentos de inicio de sesión
        intentos = 3
        while intentos > 0:
            password = input("Contraseña: ")
            if password == usuarios[identifer]:
                print("Acceso concedido ✅")
                break
            else:
                intentos -= 1
                print(f"❌ Contraseña incorrecta. Te quedan {intentos} intento(s).")

        if intentos == 0:
            print("Demasiados intentos fallidos 🚫. Regresando al menú principal.")

    elif opcion == "3":
        print("👋 Saliendo del programa...")
        break
    else:
        print("⚠️ Opción no válida. Intenta de nuevo.")