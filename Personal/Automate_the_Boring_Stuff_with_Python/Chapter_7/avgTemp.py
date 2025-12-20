import random

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

def get_average_temperature(weather_data):
    total_temp = 0

    for entry in weather_data:
        total_temp += entry['temp']

    average = total_temp / len(weather_data)
    return average

all_weather_reports = []

for i in range(100):
    data = get_random_weather_data()
    all_weather_reports.append(data)

avg_result = get_average_temperature(all_weather_reports)

print(f"The average temperature is: {avg_result:.2f} °C")