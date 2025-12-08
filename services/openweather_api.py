import datetime
import os

import requests
from datetime import datetime
from config import Config #wszystkie dane z tek klasy są dostepne po kropce Config.
from tools import convert_to_celsius, ms_to_kmh

def fetch_weather(): #tworzymy funkcję, którą wywołamy w main
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={Config.QUERY}&appid={Config.API_KEY}"

        res = requests.get(url)
        data = res.json() #konwersja danych na takie, które możemy odczytać
        weather = {
            "temp" : convert_to_celsius(data["main"]["temp"]),
            "temp_feels_like" : convert_to_celsius(data["main"]["feels_like"]),
            "pressure" : data["main"]["pressure"],
            "humidity" : data["main"]["humidity"],
            "description" : data["weather"][0]["description"],
            "clouds" : data["clouds"]["all"],
            "place" : data["name"],
            "wind":ms_to_kmh(data["wind"]["speed"]),
            "cloudiness": data["clouds"]["all"],
            "time" : datetime.fromtimestamp(data["dt"]).strftime("%H:%M:%S %d-%m-%Y")
        }

        return weather

    except Exception as e:
        print(e)
