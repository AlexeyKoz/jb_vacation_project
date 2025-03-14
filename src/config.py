from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base
import sys
import locale

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

DATABASE_URL = "postgresql://postgres:1234@localhost:5432"

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

