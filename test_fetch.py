from models.pipeline import fetch_current_and_forecast
from models.save_data import save_current_weather, save_forecast

city = "Karachi"

res = fetch_current_and_forecast(city)

if "error" in res:
    print("❌ ERROR:", res["error"])
else:
    print("🌍 CITY:", res["city"])
    print("CURRENT:", res["current"])
    print("DAILY (first 2):", res["daily"][:2])

    # ✅ Save to DB
    save_current_weather(res["city"], res["current"])
    save_forecast(res["city"], res["daily"])
