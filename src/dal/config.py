from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import engine, SessionLocal
from src.dal.base import Base

# its basic configuration for the database connection.
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/project_db"

# Create a connection to the database
engine = create_engine(DATABASE_URL)

# Create a session to interact with the database
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# Create a base class for all ORM models
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create the database tables
def create_tables():
    Base.metadata.create_all(bind=engine)
