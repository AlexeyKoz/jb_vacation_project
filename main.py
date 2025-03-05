from sqlalchemy.orm import Session
from src.dal.config import SessionLocal
from src.services.user_service import UserService
from src.services.role_service import RoleService
from src.services.country_service import CountryService
from src.services.vacation_service import VacationService
from src.services.like_service import LikeService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def main():
    db: Session = next(get_db())  #

    user_service = UserService(db)
    role_service = RoleService(db)
    country_service = CountryService(db)
    vacation_service = VacationService(db)
    like_service = LikeService(db)

    while True:
        print("\nChoose an option:")
        print("1 - Create a new user (non-admin)")
        print("2 - Get all users")
        print("3 - Create a new role")
        print("4 - Get all roles")
        print("5 - Update user role")
        print("6 - Create a new country")
        print("7 - Get all countries")
        print("8 - Create a new vacation")
        print("9 - Get all vacations")
        print("10 - Like a vacation")
        print("11 - Get likes by user")
        print("12 - Exit")

        choice = input("Enter option: ")

        if choice == "12":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
