from models.database import engine, Weather
from sqlalchemy import text

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1 AS test"))
        for row in result:
            print("✅ Database connected successfully! Test result:", row.test)
except Exception as e:
    print("❌ Database connection failed:", e)
