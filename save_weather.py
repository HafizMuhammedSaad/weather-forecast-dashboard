import os
import requests
from dotenv import load_dotenv
from models.save_data import save_weather_to_db

load_dotenv()  # .env file se keys load karega

API_KEY = os.getenv("OPENWEATHER_API_KEY")  # ab yahan se key lega
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("📌 API Response:", data)  # Debugging
        return data
    else:
        print("❌ Error fetching weather:", response.status_code)
        return None

if __name__ == "__main__":
    city = "Karachi"
    weather_data = fetch_weather(city)
    if weather_data:
        save_weather_to_db(city, weather_data)
