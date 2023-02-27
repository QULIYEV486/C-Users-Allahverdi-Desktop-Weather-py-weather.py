import requests

pre_result = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m')

result = pre_result.json()

print(f"weather: {result['current_weather']['temperature']}")

print(f"weather: {result['current_weather']['windspeed']}")

print(f"weather: {result['current_weather']['winddirection']}")

print(f"weather: {result['current_weather']['weathercode']}")

print(f"weather: {result['current_weather']['time']}")

print(f"weather: {result ['hourly_units']['time']}")


     
print("\n")
