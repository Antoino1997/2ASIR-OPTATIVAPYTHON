'''
En este ejercicio voy a agregar pprint para que la salida del código sea legible,
si lo ejecutase como un print normal daría como resultado una línea donde están todos los reportes,
en cambio si uso pprint cada reporte es su propio bloque.
'''

import random
from pprint import pprint

def get_random_weather_data():
    temp = random.uniform(-50, 50)
    feels_like = temp + random.uniform(-10, 10)

    weather_dict = {
        'temp': temp,
        'feels_like': feels_like,
        'humidity': random.randint(0, 100),
        'pressure': random.randint(990, 1010)
    }

    return weather_dict

all_weather_reports = []

for i in range(100):
    data = get_random_weather_data()
    all_weather_reports.append(data)

pprint(all_weather_reports)