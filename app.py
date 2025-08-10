import streamlit as st
from weather_report import generate_weather_report



st.title("Bulletin météo IA")

city = st.text_input("Enter the city name")

if city:
    result = generate_weather_report(city)
    st.write(result)
