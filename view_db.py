from models.database import SessionLocal, Weather

session = SessionLocal()
rows = session.query(Weather).all()

print(f"✅ Total rows: {len(rows)}")
for r in rows:
    print(f"{r.id} | {r.city} | {r.temperature}°C | {r.description} | {r.timestamp}")
