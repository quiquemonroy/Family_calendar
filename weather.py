import json
from datetime import datetime
import requests
from LOCAL import API_KEY, lat, lon


def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang={'ES'}&units=metric"
    response = requests.get(url)
    print(response)
    data = json.loads(response.text)
    weather = {"icon": data["weather"][0]["icon"],
               "description": data["weather"][0]["description"],
               "t_min": round(data["main"]["temp_min"]),
               "t_max": round(data["main"]["temp_max"]),
               "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).time().strftime("%H:%M"),
               "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M"), }
    return weather


if __name__ == "__main__":
    print(get_weather())
