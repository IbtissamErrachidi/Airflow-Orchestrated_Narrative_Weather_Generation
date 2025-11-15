import google.generativeai as genai
from Weather_Storyteller.config import GOOGLE_API_KEY
from Weather_Storyteller.get_weather import get_Weather
from Weather_Storyteller.cache import r, CACHE_DURATION
from Weather_Storyteller.utils import unix_to_local_time
import json


def generate_weather_report(city):
    """
    Generates a weather report for a given city, using cached data if available and recent.
    
    Returns:
        dict: Structured weather data with AI-generated narrative report.
    """
    city_key = city.strip().lower()
     
    cached_response = r.get(city_key)
    if cached_response:
        return json.loads(cached_response.decode())

    genai.configure(api_key=GOOGLE_API_KEY)

    data = get_Weather(city)

    if not data or "name" not in data:
        return {"error": "City not found. Please check the name and try again."}

    timezone_offset = data.get("timezone", 0)

    params = {
        "city": data["name"],
        "description": data["weather"][0]["description"].capitalize(),
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
        "pressure": data["main"]["pressure"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "clouds": data["clouds"]["all"],
        "sunrise": unix_to_local_time(data["sys"]["sunrise"], timezone_offset),
        "sunset": unix_to_local_time(data["sys"]["sunset"], timezone_offset)
    }

    # Prompt pour l'IA
    template = f"""
Here is the weather data for the city of {params['city']}:
- Current temperature: {params['temp']}°C
- Feels like: {params['feels_like']}°C
- Minimum temperature: {params['temp_min']}°C
- Maximum temperature: {params['temp_max']}°C
- Pressure: {params['pressure']} hPa
- Humidity: {params['humidity']}%
- Weather description: {params['description']}
- Wind speed: {params['wind_speed']} m/s
- Cloud coverage: {params['clouds']}%
- Sunrise time: {params['sunrise']}
- Sunset time: {params['sunset']}

Please write a **concise weather report** in 4-6 sentences for a daily email bulletin,
with **short clothing and activity advice**.
"""


    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(template)


    weather_report = {
        "city": params["city"],
        "temp": params["temp"],
        "feels_like": params["feels_like"],
        "temp_min": params["temp_min"],
        "temp_max": params["temp_max"],
        "pressure": params["pressure"],
        "humidity": params["humidity"],
        "description": params["description"],
        "wind_speed": params["wind_speed"],
        "clouds": params["clouds"],
        "sunrise": params["sunrise"],
        "sunset": params["sunset"],
        "narrative": response.text
    }


    
    r.setex(city_key, CACHE_DURATION, json.dumps(weather_report))

    return weather_report
