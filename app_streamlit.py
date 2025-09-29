import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from models.save_data import save_current_weather, save_forecast

API_KEY = "604a1aefddf14ed6c7fbdcad7332f771"
BASE_URL = "https://api.openweathermap.org/data/2.5"

# Current Weather fetch with error handling
def get_current_weather(city):
    try:
        url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }
    except:
        return None

# Forecast fetch with error handling
def get_forecast(city):
    try:
        url = f"{BASE_URL}/forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        forecast_list = []
        for item in data["list"]:
            date = item["dt_txt"].split(" ")[0]
            forecast_list.append({
                "date": date,
                "temp_day": item["main"]["temp"],
                "temp_min": item["main"]["temp_min"],
                "temp_max": item["main"]["temp_max"],
                "humidity": item["main"]["humidity"],
                "condition": item["weather"][0]["description"]
            })
        return forecast_list
    except:
        return None

# Analytics
def get_hottest_coldest_day(forecast_data):
    df = pd.DataFrame(forecast_data)
    hottest = df.loc[df['temp_day'].idxmax()]
    coldest = df.loc[df['temp_day'].idxmin()]
    return hottest, coldest

def plot_temp_trend(forecast_data):
    df = pd.DataFrame(forecast_data)
    fig, ax = plt.subplots()
    ax.plot(df["date"], df["temp_day"], marker="o", label="Avg Temp")
    ax.plot(df["date"], df["temp_min"], linestyle="--", label="Min Temp")
    ax.plot(df["date"], df["temp_max"], linestyle="--", label="Max Temp")
    ax.set_title("Temperature Trend (Next 5 Days)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature °C")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

# ----------------- Streamlit App -----------------
st.title("Weather Forecast Dashboard")

city = st.text_input("Enter city name:", "Karachi")

if st.button("Get Weather"):
    current = get_current_weather(city)
    forecast = get_forecast(city)

    if not current:
        st.error("Invalid city name or API issue. Try again.")
    else:
        st.subheader("Current Weather")
        st.write(f"City: {current['city']}")
        st.write(f"Temperature: {current['temperature']}°C")
        st.write(f"Humidity: {current['humidity']}%")
        st.write(f"Wind: {current['wind']} m/s")
        st.write(f"Condition: {current['description']}")

        save_current_weather(
            current["city"],
            current["temperature"],
            current["description"]
        )
        st.success("Current weather saved to DB!")

    if not forecast:
        st.warning("Forecast data not available.")
    else:
        st.subheader("5-Day Forecast")
        df_forecast = pd.DataFrame(forecast[:5])
        st.dataframe(
        df_forecast[["date", "temp_day", "temp_min", "temp_max", "humidity", "condition"]],
        width="stretch"
        )


        save_forecast(city, forecast[:5])
        st.success("Forecast saved to DB!")

        hottest, coldest = get_hottest_coldest_day(forecast[:5])
        st.subheader("Analytics")
        st.write(f"Hottest Day: {hottest['date']} → {hottest['temp_day']}°C ({hottest['condition']})")
        st.write(f"Coldest Day: {coldest['date']} → {coldest['temp_day']}°C ({coldest['condition']})")

        st.subheader("Temperature Trend")
        plot_temp_trend(forecast[:5])
