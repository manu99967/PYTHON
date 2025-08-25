
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

db_credentials = {
    "drivername": "postgresql+psycopg",
    "username": "postgres.riwswfjumjztqurzzask",
    "password": "www.proxynova.com999",
    "host": "aws-0-ap-south-1.pooler.supabase.com",
    "port": 5432,
    "database": "postgres"
}

# Build DB URL
DATABASE_URL = URL.create(**db_credentials)

# Create engine
engine = create_engine(DATABASE_URL, echo=True, future=True)

