import google.generativeai as genai
from config import GOOGLE_API_KEY  # Import API key
from get_weather import get_Weather


def generate_weather_report(city):
    
    genai.configure(api_key=GOOGLE_API_KEY)

    data = get_Weather(city)

    if not data or "name" not in data:
        return f" City not found. Check the name and try again."


    template = """
Voici les données météo pour la ville de {ville} :
- Température actuelle : {temp}°C
- Température ressentie : {temp_ressentie}°C
- Température minimale : {temp_min}°C
- Température maximale : {temp_max}°C
- Pression : {pression} hPa
- Humidité : {humidite}%
- Description : {description}
- Vent : {vent_vitesse} m/s
- Couverture nuageuse : {couverture_nuageuse}%
- Lever du soleil : {lever_soleil}
- Coucher du soleil : {coucher_soleil}

Peux-tu écrire un texte narratif "façon journal météo" qui raconte cette météo de manière claire et agréable ?
Donne aussi des conseils pratiques sur les vêtements et activités adaptées.

Texte :
"""

    params = {
        "ville": data["name"],
        "description": data["weather"][0]["description"],
        "temp": data["main"]["temp"],
        "temp_ressentie": data["main"]["feels_like"],
        "temp_min": data["main"]["temp_min"],
        "temp_max": data["main"]["temp_max"],
        "pression": data["main"]["pressure"],
        "humidite": data["main"]["humidity"],
        "vent_vitesse": data["wind"]["speed"],
        "couverture_nuageuse": data["clouds"]["all"],
        "lever_soleil": data["sys"]["sunrise"],
        "coucher_soleil": data["sys"]["sunset"]
    }

    prompt = template.format(**params)

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)


    return response.text
