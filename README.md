# Weather_Storyteller
  
  This project generates a weather report narrative based on city name.It fetches real-time weather data from the free OpenWeatherMap API, then uses a large language model (LLM) to create a journal-style weather report including practical advice about clothes and activities.

  ## Features

  
- Input: city name.
- Retrieve current weather data via OpenWeatherMap API.
- Automatically generate a clear and engaging narrative weather report.
- Include practical tips on clothing and activities based on the weather.
- Simple user interface built with Streamlit.


---

## Project Structure

Weather_Storyteller/
├── .env # Environment variables (API keys)
├── config.py # Load environment variables
├── get_weather.py # Function to call weather API
├── weather_report.py # Generate weather report using LLM
└── app.py # Streamlit app (user interface)


## Requirements

- Python 3.8 or higher
- Valid API keys (OpenWeatherMap and Google Generative AI)
- Virtual environment recommended

---

## Installation

1. Clone this repository:
```bash
git clone https://github.com/IbtissamErrachidi/Weather_Storyteller.git
cd Weather_Storyteller

python -m venv venv
source venv/Scripts/activate   # Windows PowerShell
# or
source venv/bin/activate       # Linux/macOS
pip install -r requirements.txt # Install dependencies
```
2. Environment Variables
```bash
#Create a .env file in the root folder with your API keys
WEATHER_API_KEY=your_openweathermap_api_key
GOOGLE_API_KEY=your_google_generativeai_api_key
```

## Usage

```bash
streamlit run app.py #Run the Streamlit application
```

