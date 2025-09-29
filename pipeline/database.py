from sqlalchemy import create_engine, Table, Column, Integer, String, Float, MetaData

engine = create_engine("sqlite:///weather.db")
metadata = MetaData()

weather_table = Table(
    "weather", metadata,
    Column("id", Integer, primary_key=True),
    Column("city", String),
    Column("date", String),
    Column("temp", Float),
    Column("humidity", Integer),
    Column("description", String)
)

metadata.create_all(engine)
