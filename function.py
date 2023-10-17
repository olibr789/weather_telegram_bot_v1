import datetime
from config import open_weather_token
import requests
from pprint import pprint

weather_smile = {
        "Thunderstorm": "Гроза \U000026C8",
        "Drizzle": "Мелкий дождь \U0001F4A7",
        "Rain": "Дождь \U0001F327",
        "Snow": "Снег \U0001F328",
        "Atmosphere": "Туманность \U0001F301",
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601"
    }

def city_to_coordinates(city, open_weather_token):
    r_coordinates = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={open_weather_token}")
    data_coordinates = r_coordinates.json()
    latitude = data_coordinates[0]['lat']
    longitude = data_coordinates[0]['lon']
    return latitude, longitude

def five_days_weather(city, open_weather_token):
    weather_smile = {
            "Thunderstorm": "Гроза \U000026C8",
            "Drizzle": "Мелкий дождь \U0001F4A7",
            "Rain": "Дождь \U0001F327",
            "Snow": "Снег \U0001F328",
            "Atmosphere": "Туманность \U0001F301",
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601"
        }
    lat, lon = city_to_coordinates(city,open_weather_token)
    r_weather = requests.get(
        f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric"
    )
    data = r_weather.json()
    print(f"Погода в городе {city} на ближайшие 5 дней\n"
          f"//////////////////////////////////////////////")
    try:
        i = 0
        while True:
            temp = data['list'][i]['dt_txt']
            if (temp[8:10] == datetime.date.today().strftime('%d')):
                i += 1
            else:
                if (temp[11:13] == '09') or (temp[11:13] == '21'):
                    if temp[11:13] == '09':
                        print(f"Погода на {temp[:10]}\n"
                              f"Температура утром: {round(data['list'][i]['main']['temp'],1)}℃"
                              f" {weather_smile[data['list'][i]['weather'][0]['main']]}\n"
                              f"Будет ощущатся как: {round(data['list'][i]['main']['feels_like'],1)}℃\n"
                              f"Ветер: {round(data['list'][i]['wind']['speed'],1)} м\с\n"
                              )
                    else:
                        print(f"Температура вечером: {round(data['list'][i]['main']['temp'],1)}℃"
                              f" {weather_smile[data['list'][i]['weather'][0]['main']]}\n"
                              f"Будет ощущатся как: {round(data['list'][i]['main']['feels_like'],1)}℃\n"
                              f"Ветер: {round(data['list'][i]['wind']['speed'],1)} м\с\n"
                              f"//////////////////////////////////////////////")
                i += 1
    except:
        print("Проверьте введенные данные!")

