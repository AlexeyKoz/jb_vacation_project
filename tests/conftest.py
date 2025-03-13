import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.dal.base import Base
import locale
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


# Connection to database
TEST_DATABASE_URL = "postgresql://postgres:1234@localhost:5432/test_db?client_encoding=utf8"


@pytest.fixture(scope="function")
def db_session():
    """Create and erase a new database session for a test."""
    engine = create_engine(TEST_DATABASE_URL)
    TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

    # Create all tables before testing
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()

    yield session  # Give a session to the test

    session.rollback()  # Remove all changes from the session
    session.close()
    Base.metadata.drop_all(bind=engine)  # Delete all tables after the test
