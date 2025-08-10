import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read keys from .env
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
