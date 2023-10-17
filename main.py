from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API, open_weather_token
from datetime import datetime
from function import city_to_coordinates, weather_smile

import requests


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Done')

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет, напиши мне название города, что бы узнать погоду в нём!")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        lat, lon = city_to_coordinates(message.text, open_weather_token)
        r_wheather = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric"
        )
        data_weather = r_wheather.json()
        temp_info = data_weather['main']
        sun_info = data_weather['sys']
        weather_info = data_weather['weather'][0]
        wind_info = data_weather['wind']
        await message.reply(f"--------{datetime.now().strftime('%d.%m.%Y %H:%M')}--------\n\n\n"
                            f"Погода в городе {message.text}\n"
                            f"{weather_smile[weather_info['main']]}\n"
                            f"Температура: {round(temp_info['temp'],1)}℃\n"
                            f"Ощущается как: {round(temp_info['feels_like'],1)}℃\n"
                            f"Максимальная температура за день: {round(temp_info['temp_max'],1)}℃\n" 
                            f"Минимальная температура за день: {round(temp_info['temp_min'],1)}℃\n"
                            f"Ветер: {round(wind_info['speed'],1)} м\с\n" 
                            f"Влажность: {temp_info['humidity']}%\n"
                            f"Давление: {temp_info['pressure']} мм.рт.ст\n"
                            f"Время восхода солнца: {datetime.fromtimestamp(sun_info['sunrise']).strftime('%H:%M:%C')}\n"
                            f"Время захода солнца: {datetime.fromtimestamp(sun_info['sunset']).strftime('%H:%M:%C')}\n"
                            f"Продолжительность дня: {datetime.fromtimestamp(sun_info['sunset']) - datetime.fromtimestamp(sun_info['sunrise'])}\n\n\n"
                            f"--------Хорошего дня!--------")
    except Exception as ex:
        print(ex)
        await message.reply(f"Введено некоректное название города!\nПровертье правильность ввода!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

