import requests
from models.save_data import save_weather_to_db
  # sahi import

API_KEY = "25956ea250d4637c33ead5d7e8caa3dc"  # apna API key lagao
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
