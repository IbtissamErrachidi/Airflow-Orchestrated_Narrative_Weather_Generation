import requests
from config import WEATHER_API_KEY


def get_Weather(city):
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_API_KEY}"
  r = requests.get(url)
  if r.status_code == 200:
        return r.json()
  return None

