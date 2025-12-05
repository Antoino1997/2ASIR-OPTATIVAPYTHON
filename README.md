# 2ASIR-OPTATIVAPYTHON

Esto es un repositorio que contiene las actividades de Python de 2ºASIR

## BLOQUE 1
Ejercicio | Descripción
----------|------------
[Ejercicio1](Bloque_01/b1_1_presentacion.py) | Pide el nombre y la edad al usuario y muestra un mensaje personalizado.
[Ejercicio2](Bloque_01/b1_2_calculadora_simple.py) | Calcula y muestra las seis operaciones aritméticas básicas (suma, resta, multiplicación, división, módulo y potencia) entre dos variables numéricas.
[Ejercicio3](Bloque_01/b1_3_conversor_datos.py) | Solicita nombre, edad y altura al usuario, realizando la conversión de tipos necesaria (int y float), y muestra los datos formateados.
[Ejercicio4](Bloque_01/b1_4_login.py) | Simula un inicio de sesión: pide usuario y contraseña, y usa operadores lógicos para verificar si coinciden con las credenciales predefinidas ("admin", "1234").
[Ejercicio5_1](Bloque_01/b1_5_1_calculadora_condicional.py) | Calculadora condicional: Pide dos números y una operación (suma, resta, multiplicación o división), y usa la estructura if/elif/else para ejecutar y mostrar el resultado.
[Ejercicio5_2](Bloque_01/b1_5_2_calculadora_switch.py) | Calculadora con match-case: Pide dos números y una operación, y usa la estructura match-case para ejecutar y mostrar el resultado de la operación seleccionada.
[Ejercicio6](Bloque_01/b1_6_contador_regresivo.py) | Contador regresivo con while: Solicita un número al usuario y utiliza un bucle while para contar desde ese número hasta 0, terminando con el mensaje "¡Despegue!".
[Ejercicio7](Bloque_01/b1_7_filtrar_lista.py) | Filtrado de lista con for y continue: Define una lista de nombres y usa un bucle for junto con continue para mostrar solo aquellos nombres que no empiecen por 'A'.
[Ejercicio8](Bloque_01/b1_8_tabla_multiplicar.py) | Genera la tabla de multiplicar (del 1 al 10) de un número introducido por el usuario, utilizando un bucle.
[Ejercicio9](Bloque_01/b1_9_analizador_notas.py) | Analizador de notas y depuración: Pide tres notas, calcula el promedio, e intencionalmente contiene un error lógico que debe ser encontrado y corregido usando el modo de depuración de IntelliJ.
[Ejercicio10](Bloque_01/b1_10_login.py) | Sistema de Registro e Inicio de Sesión: Crea un programa basado en menú (while y if/elif/else) con funciones de registro (validación estricta de email/contraseña) y login (3 intentos máximos), poniendo en práctica todos los conceptos del Bloque 1.

## BLOQUE 2
Ejercicio | Descripción
----------|------------
[Ejercicio1](Bloque_02/b2_01_menu_principal.py) | Define y usa una función mostrar_menu() que presenta al menos 3 opciones. La función es llamada dos veces desde el programa principal, demostrando la reutilización de código.
[Ejercicio2](Bloque_02/b2_02_registro_usuario.py) | Gestión de Argumentos en Funciones: Crea una función registrar_usuario con un argumento por defecto, y demuéstrala llamándola con argumentos posicionales, nombrados y omitiendo el argumento por defecto.
[Ejercicio3](Bloque_02/b2_03_calculadora.py) | Calculadora Modular: Implementa cuatro funciones separadas (sumar, restar, multiplicar, dividir) para operaciones básicas, incluyendo el control explícito de la división por cero.
[Ejercicio4](Bloque_02/b2_04_contador.py) | Manejo de Variables Globales: Implementa tres funciones (incrementar, decrementar, mostrar_contador) que modifican y acceden a una variable global (contador) utilizando la palabra clave global.
[Ejercicio5](Bloque_02/b2_05_gestion_lista.py) | Gestión de Lista de Compras: Crea una lista vacía, añade 5 productos con append(), elimina uno con remove(), y finalmente muestra la lista ordenada alfabéticamente con sort().
[Ejercicio6](Bloque_02/b2_06_informacion_persona.py) | Tuplas y Desempaquetado: Define una tupla con datos personales y demuestra el desempaquetado de sus elementos en variables separadas para su posterior visualización.
[Ejercicio7](Bloque_02/b2_07_agenda.py) | Gestión de Agenda con Diccionarios: Solicita 3 contactos (nombre como clave y teléfono como valor) para añadirlos a un diccionario. Luego, permite al usuario buscar un contacto por su nombre.
[Ejercicio8](Bloque_02/b2_08_analisis_numeros.py) | Comprensiones de Listas y Diccionarios: Genera una lista de 20 números y usa comprensiones (list comprehensions) para crear listas de cuadrados, pares, y mayores de 10, además de un diccionario que mapea cada número con su doble.
[Ejercicio9_1](Bloque_02/b2_09_1_zip.py) | Uso de zip(): Combina tres listas (nombres, notas_matematicas, notas_fisica) utilizando la función zip() para iterar sobre ellas simultáneamente y mostrar un informe de notas por estudiante.
[Ejercicio9_2](Bloque_02/b2_09_2_zip_avanzado.py) | Reporte de notas con zip() y Diccionarios: Usa zip() para combinar cuatro listas de datos. Calcula el promedio de cada estudiante y, aplicando lógica condicional, determina su estado ("Aprobado", "En recuperación", "Reprobado"). Almacena todos los datos en un diccionario anidado.
[Ejercicio10_1](Bloque_02/b2_10_1_enumerate.py) | Uso de enumerate(): Itera sobre una lista de nombres para mostrar el índice y el valor de cada elemento, y luego convierte el resultado de enumerate en una lista de tuplas (índice, valor).
[Ejercicio10_2](Bloque_02/b2_10_2_enumerate_avanzado.py) | Reporte avanzado con enumerate() y zip(): Combina las listas de estudiantes y notas usando zip() y enumerate(start=1) para generar un informe indexado. El script calcula el promedio y asigna la calificación final (Aprobado, etc.) a cada estudiante.
[Ejercicio11_2](Bloque_02/b2_11_2_iteradores_mejorado.py) | teradores Manuales y Reporte: Crea un iterador sobre las claves de un diccionario de estudiantes y notas. Recorre el iterador manualmente usando next() dentro de un bucle while True con manejo de StopIteration, y calcula el promedio y estado (Aprobado, etc.) para generar un reporte final.
[Ejercicio_Final](Bloque_02/b2_people_crud_menu.py) | Sistema CRUD de Personas: Implementa un menú interactivo (while con match-case) para gestionar datos personales. Utiliza un diccionario anidado (people) donde el NIF/DNI es la clave principal y el valor es otro diccionario con los datos (name, age, city, profession). Implementa las funciones Crear (C), Buscar (R), Actualizar (U) y Eliminar (D).

## EXAMEN 1
Ejercicio | Descripción
----------|------------
[Ejercicio1](Examen_01/actividad_1.py) | Define internamente una lista fija de lenguajes de programación. La función cuenta cuántas veces aparece nombre_elemento en esa lista. Muestra un mensaje indicando el número de apariciones si el elemento existe, o un mensaje de "no está" si no aparece. Debe ser llamada 3 veces desde el programa principal con los valores "python", "java" y "ruby".
[Ejercicio2](Examen_01/actividad_2.py) | Crea un diccionario inicial llamado persona con las claves "nombre", "edad" y "ciudad". Muestra los valores iniciales con un formato específico. Posteriormente, añade la clave "profesion" y elimina la clave "ciudad". Finalmente, itera sobre el diccionario resultante y muestra todas las claves y valores en formato clave: valor.
[Ejercicio3](Examen_01/actividad_3.py) | Define internamente una lista valores = [10, 20, 30, 40] y crea un iterador a partir de ella con iter(valores). Utiliza un bucle while para iterar , obteniendo cada elemento con next(it, None). La parada del bucle debe basarse únicamente en el valor None devuelto por next() al agotarse el iterador. Muestra cada elemento en el formato exacto "Valor: <elemento>". No se permite usar for ni StopIteration.
