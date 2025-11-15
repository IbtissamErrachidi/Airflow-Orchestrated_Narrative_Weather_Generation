import requests
from Weather_Storyteller.config import WEATHER_API_KEY



def get_Weather(city):
      """
      Fetches weather data from OpenWeatherMap API.

      Parameters:
      city (str): Name of the city to get weather data for.

      Returns:
      dict: JSON response containing weather details such as temperature,
            humidity, wind speed, sunrise/sunset times, etc.
      """
      
      url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_API_KEY}"
      r = requests.get(url)
      if r.status_code == 200:
            return r.json()
      return None

