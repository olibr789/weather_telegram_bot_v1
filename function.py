from config import open_weather_token
import requests
def city_to_coordinates(city, open_weather_token):
    r_coordinates = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={open_weather_token}")
    data_coordinates = r_coordinates.json()
    latitude = data_coordinates[0]['lat']
    longitude = data_coordinates[0]['lon']
    return latitude, longitude

city_to_coordinates('Тверь', open_weather_token)
print(city_to_coordinates('Тверь', open_weather_token))