# Weather_Storyteller

This project generates narrative weather reports based on city names, fetches real-time weather data from the **OpenWeatherMap API**, and uses the **Gemini 1.5 Flash AI model** to produce journal-style reports with practical tips on clothing and activities. Additionally, the project now includes **Airflow DAGs** to automate data processing and report generation, and **Docker** support for easier deployment.

Redis is used as a caching layer to store recent weather reports temporarily with a TTL (e.g., 15 minutes), reducing redundant API calls while maintaining fresh data.

---

## Features

- Input: city name.
- Retrieve current weather data via **OpenWeatherMap API**.
- Cache recent weather reports using **Redis** to speed up responses and reduce API usage.
- Automatically generate engaging narrative weather reports with practical tips.
- Automate report generation with **Airflow DAGs**.
- Run the full system locally or in containers using **Docker** and **docker-compose**.
- Simple web interface built with **Streamlit**.

---

## Project Structure

```text
Weather_Storyteller/
├── .env                  # Environment variables (API keys)
├── Weather_Storyteller/  # Main Python package
│   ├── __init__.py
│   ├── app.py            # Streamlit app
│   ├── cache.py          # Redis cache handling
│   ├── config.py         # Load environment variables
│   ├── get_weather.py    # Fetch weather data
│   ├── utils.py          # Utility functions
│   └── weather_report.py # Generate weather report with LLM
├── dags/                 # Airflow DAGs
│   └── weather_dag.py
├── docker-compose.yaml   # Docker Compose for services
├── Dockerfile            # Docker image for the app
├── logs/                 # Airflow logs
├── requirements.txt      # Python dependencies
└── README.md

```

## Requirements

- Python 3.8 or higher
- Valid API keys (OpenWeatherMap and Google Generative AI)
- Virtual environment recommended
- Docker & Docker Compose (optional for containerized deployment)
- Redis (if running locally outside Docker)


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

> **Note:** The main purpose of this project is **automated weather report generation** via Airflow DAGs and Redis caching. Streamlit is provided only for local testing and manual interaction.

Run the Streamlit application locally (optional):

```bash
streamlit run app.py  # For local testing only
```

Redis initialization for Airflow DAGs (in Docker):

```python
# Initialize Redis client once
r = redis.Redis(host='airflow_weather-redis-1', port=6379, db=0)
# r = redis.Redis(host='localhost', port=6379, db=0)  # for local testing
```

Run Airflow in Docker:

```bash
docker-compose up --build
```

The Airflow DAG is scheduled to run **daily at 7:00 AM**:

```python
schedule='0 7 * * *'
``

Access the apps at:

* Streamlit: [http://localhost:8501](http://localhost:8501)  # optional
* Airflow UI: [http://localhost:8080](http://localhost:8080)


