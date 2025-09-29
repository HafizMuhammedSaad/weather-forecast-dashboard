# check_db.py
from models.database import SessionLocal, Weather, Forecast

session = SessionLocal()
print("---- Weather table ----")
rows_w = session.query(Weather).order_by(Weather.id.desc()).limit(5).all()
for r in rows_w:
    print(r.id, r.city, r.temperature, r.description, r.timestamp)

print("\n---- Forecast table (last 10) ----")
rows_f = session.query(Forecast).order_by(Forecast.id.desc()).limit(10).all()
for r in rows_f:
    print(r.id, r.city, r.date, r.temp_day, r.temp_min, r.temp_max, r.humidity, r.condition)

session.close()
