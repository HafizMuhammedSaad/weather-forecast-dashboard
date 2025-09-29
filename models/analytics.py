# pipeline/analytics.py
from models.database import SessionLocal, Forecast
from sqlalchemy import func
from datetime import date

def hottest_and_coldest(city, days=None):
    session = SessionLocal()
    try:
        q = session.query(Forecast).filter(Forecast.city == city)
        if days:
            q = q.order_by(Forecast.date.desc()).limit(days)
            rows = q.all()
        else:
            rows = q.all()

        if not rows:
            return None

        hottest = max(rows, key=lambda r: (r.temp_max or -9999))
        coldest = min(rows, key=lambda r: (r.temp_min or 9999))
        return {
            "hottest": {
                "date": hottest.date,
                "temp_max": hottest.temp_max,
                "condition": hottest.condition
            },
            "coldest": {
                "date": coldest.date,
                "temp_min": coldest.temp_min,
                "condition": coldest.condition
            }
        }
    finally:
        session.close()
