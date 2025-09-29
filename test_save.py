from models.save_data import save_current_weather, save_forecast

# dummy data
city = "Karachi"
current = {
    "temp": 31.5,
    "condition": "clear sky"
}

daily = [
    {"date": "2025-09-28", "temp_day": 30.2, "temp_min": 27.0, "temp_max": 33.1, "humidity": 70, "condition": "cloudy"},
    {"date": "2025-09-29", "temp_day": 31.0, "temp_min": 28.0, "temp_max": 34.5, "humidity": 65, "condition": "sunny"},
]

# save to DB
save_current_weather(city, current)
save_forecast(city, daily)
