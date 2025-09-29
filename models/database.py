# models/database.py
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Date
from sqlalchemy.orm import sessionmaker, declarative_base
import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, '..', 'weather.db')}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Weather(Base):
    __tablename__ = "weather"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(Float)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class Forecast(Base):
    __tablename__ = "forecast"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    date = Column(Date)   # ✅ yahan string nahi chalega
    temp_day = Column(Float)
    temp_min = Column(Float)
    temp_max = Column(Float)
    humidity = Column(Float)
    condition = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(bind=engine)
