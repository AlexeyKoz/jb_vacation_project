import sys
import os

# Add the src folder to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy.orm import Session
from src.dal.config import SessionLocal
from src.services.user_service import UserService
from src.services.role_service import RoleService
from src.services.country_service import CountryService
from src.services.vacation_service import VacationService
from src.services.like_service import LikeService
from src.maual_menu import run_manual_menu


# Database session generator
def get_db():
    """Creates a new database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Main function to start the project
def main():
    db: Session = next(get_db())

    # Initialize services
    user_service = UserService(db)
    role_service = RoleService(db)
    country_service = CountryService(db)
    vacation_service = VacationService(db)
    like_service = LikeService(db)

    # Run manual menu
    run_manual_menu(user_service, role_service, country_service, vacation_service, like_service)


if __name__ == "__main__":
    main()
