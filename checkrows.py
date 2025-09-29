from models.database import SessionLocal, Weather

session = SessionLocal()
count = session.query(Weather).count()
print("Total rows in Weather table:", count)
session.close()
