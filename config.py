import os
from dotenv import load_dotenv

load_dotenv()


WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
