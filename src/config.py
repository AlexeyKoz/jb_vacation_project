from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base
import sys
import locale

# Set the default encoding to UTF-8.
# Without we have bugs with database encoding
# and this is make us sure the db is in UTF-8 format.
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Set the locale to en_US.UTF-8
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


# Url to connect to the database
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/"

# Create the engine to connect to the database
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        print("Successfully connected to the database!")
except Exception as e:
    print(f"Error: {e}")

# Create the tables in the database
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Create the tables in the database
def create_tables():
    Base.metadata.create_all(bind=engine)

# Drop the tables in the database and close the connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

