# clean_db.py
from models.database import SessionLocal, Weather
from sqlalchemy import or_

def clean_db():
    session = SessionLocal()
    try:
        deleted = session.query(Weather).filter(
            or_(Weather.temperature == None, Weather.description == None)
        ).delete(synchronize_session=False)
        session.commit()
        print(f"🧹 Deleted {deleted} rows with missing values.")
    except Exception as e:
        print("❌ Error while cleaning:", e)
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    clean_db()
