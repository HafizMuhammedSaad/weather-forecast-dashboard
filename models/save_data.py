from models.database import SessionLocal, Weather, Forecast
from datetime import datetime

# ✅ Current Weather save karne ka function
def save_current_weather(city, temperature, description):
    session = SessionLocal()
    try:
        weather = Weather(
            city=city,
            temperature=temperature,
            description=description,
            timestamp=datetime.utcnow()
        )
        session.add(weather)
        session.commit()
    except Exception as e:
        session.rollback()
        print("Save failed:", e)
    finally:
        session.close()


# ✅ Forecast save karne ka function
def save_forecast(city, forecast_data):
    session = SessionLocal()
    try:
        for day in forecast_data:
            forecast = Forecast(
                city=city,
                date=datetime.strptime(day["date"], "%Y-%m-%d").date(),  # string → date
                temp_day=day["temp_day"],
                temp_min=day["temp_min"],
                temp_max=day["temp_max"],
                humidity=day["humidity"],
                condition=day["condition"],
                timestamp=datetime.utcnow()
            )
            session.add(forecast)
        session.commit()
    except Exception as e:
        session.rollback()
        print("Save failed:", e)
    finally:
        session.close()
