from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        print("Successfully connected to the database!")
except Exception as e:
    print(f"Error: {e}")

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

