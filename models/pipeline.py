import requests
from config import OPENWEATHER_API_KEY
import pandas as pd
from datetime import datetime

# free endpoints
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def fetch_current_and_forecast(city_name, days=7):
    # --- current weather ---
    params = {"q": city_name, "units": "metric", "appid": OPENWEATHER_API_KEY}
    r = requests.get(WEATHER_URL, params=params, timeout=10)
    if r.status_code != 200:
        return {"error": f"Weather failed: {r.status_code}"}
    current_payload = r.json()

    city_resolved = current_payload.get("name")
    lat = current_payload.get("coord", {}).get("lat")
    lon = current_payload.get("coord", {}).get("lon")

    current = {
        "temp": current_payload["main"].get("temp"),
        "feels_like": current_payload["main"].get("feels_like"),
        "humidity": current_payload["main"].get("humidity"),
        "wind_speed": current_payload["wind"].get("speed"),
        "condition": current_payload["weather"][0].get("description"),
    }

    # --- 5 day / 3 hour forecast ---
    params = {"q": city_name, "units": "metric", "appid": OPENWEATHER_API_KEY}
    r = requests.get(FORECAST_URL, params=params, timeout=10)
    if r.status_code != 200:
        return {"error": f"Forecast failed: {r.status_code}"}
    forecast_payload = r.json()

    # group forecast list into daily max/min
    daily_map = {}
    for entry in forecast_payload["list"]:
        dt = datetime.utcfromtimestamp(entry["dt"]).date()
        t = entry["main"]["temp"]
        h = entry["main"]["humidity"]
        desc = entry["weather"][0]["description"]

        if dt not in daily_map:
            daily_map[dt] = {"temps": [], "hums": [], "descs": []}
        daily_map[dt]["temps"].append(t)
        daily_map[dt]["hums"].append(h)
        daily_map[dt]["descs"].append(desc)

    daily_structured = []
    for d, vals in list(daily_map.items())[:days]:
        daily_structured.append({
            "date": d.isoformat(),
            "temp_day": sum(vals["temps"]) / len(vals["temps"]),
            "temp_min": min(vals["temps"]),
            "temp_max": max(vals["temps"]),
            "humidity": sum(vals["hums"]) / len(vals["hums"]),
            "condition": max(set(vals["descs"]), key=vals["descs"].count)
        })

    return {
        "city": city_resolved,
        "lat": lat,
        "lon": lon,
        "current": current,
        "daily": daily_structured,
    }
