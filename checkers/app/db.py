from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

db_credentials = {
    "drivername": os.getenv("DB_DRIVER"),
    "username": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),   # make sure it's int
    "database": os.getenv("DB_NAME"),
}

print(db_credentials)  # 🔍 debug check

# Build DB URL
DATABASE_URL = URL.create(**db_credentials)

# Create engine
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for ORM models
Base = declarative_base()
