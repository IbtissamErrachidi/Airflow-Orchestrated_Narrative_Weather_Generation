import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from Weather_Storyteller.weather_report import generate_weather_report

st.title("🌤 Bulletin météo IA")

city = st.text_input("Entrez le nom de la ville")

if city:
    result = generate_weather_report(city)
    
    if "error" in result:
        st.error(result["error"])
    else:
        # Affichage des principales mesures
        col1, col2, col3 = st.columns(3)
        col1.metric("Température 🌡", f"{result['temp']}°C", f"Ressenti: {result['feels_like']}°C")
        col2.metric("Humidité 💧", f"{result['humidity']}%")
        col3.metric("Vent 🌬", f"{result['wind_speed']} m/s")
        
        # Autres détails
        st.write(f"**Description météo:** {result['description']}")
        st.write(f"**Température min/max:** {result['temp_min']}°C / {result['temp_max']}°C")
        st.write(f"**Pression:** {result['pressure']} hPa")
        st.write(f"**Couverture nuageuse:** {result['clouds']}%")
        st.write(f"**Lever du soleil:** {result['sunrise']} | **Coucher du soleil:** {result['sunset']}")
        
        # Narrative IA
        st.markdown("---")
        st.subheader("📝 Rapport météo détaillé")
        st.markdown(result['narrative'])
