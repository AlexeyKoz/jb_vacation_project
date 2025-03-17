from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base
import sys
import locale

# Set the default encoding to UTF-8 to prevent encoding errors
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Set the locale to en_US.UTF-8 to prevent encoding errors
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Create a connection to the database
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/project_db"

# Create a connection to the database
engine = create_engine(DATABASE_URL)

# Check if the connection was successful
try:
    with engine.connect() as connection:
        print("Successfully connected to the database!")
except Exception as e:
    print(f"Error: {e}")

# Create a session to interact with the database
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

#Function to create test database tables
def create_tables():
    Base.metadata.create_all(bind=engine)

# Get connection to the database for testing and close connection in the end.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

