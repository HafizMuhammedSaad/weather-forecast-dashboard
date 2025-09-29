# init_db.py
from models.database import Base, engine

print("👉 Creating tables in SQL Server...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")
