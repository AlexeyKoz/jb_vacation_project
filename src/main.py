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
    db: Session = next(get_db())

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
        print("12 - Check if email exists")
        print("13 - Return user by email and password")
        print("14 - Unlike")
        print("15 - Delete a user")
        print("16 - Update vacation")
        print("17 - Delete vacation")
        print("18 - Login")
        print("19 - Get user by id")
        print("20 - Get country by id")
        print("21 - Get vacation by id")
        print("22 - Get role by id")
        print("23 - Update country by id")
        print("24 - Get all Likes")
        print("25 - Delete a Country")
        print("26 - Exit")

        choice = input("Enter option: ")

        if choice == "1":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            password = input("Password: ")
            print("Available roles:")
            roles = role_service.get_all_roles()
            for role in roles:
                print(f"{role.id} - {role.name}")
            role_id = int(input("Enter Role ID: "))
            if role_id == 1:
                print("Error: Cannot create another administrator!")
            else:
                user = user_service.create_user(first_name, last_name, email, password, role_id)
                print("User created:", user.as_dict() if user else "Error")

        elif choice == "2":
            users = user_service.get_all_users()
            print("Users:", [user.as_dict() for user in users])

        elif choice == "3":
            role_name = input("Enter new role name (Admin is restricted): ")
            if role_name.lower() == "admin":
                print("Error: Administrator role already exists and cannot be created again!")
            else:
                role = role_service.create_role(role_name)
                print("Role created:", role.as_dict() if role else "Error")

        elif choice == "4":
            roles = role_service.get_all_roles()
            print("Roles:", [role.as_dict() for role in roles])

        elif choice == "5":
            user_id = int(input("Enter User ID: "))
            print("Available roles:")
            roles = role_service.get_all_roles()
            for role in roles:
                print(f"{role.id} - {role.name}")
            new_role_id = int(input("Enter new Role ID: "))
            updated_user = user_service.update_user_role(user_id, new_role_id)
            if updated_user:
                print("User role updated:", updated_user.as_dict())
            else:
                print("Error updating user role")

        elif choice == "6":
            country_name = input("Country name: ")
            country = country_service.create_country(country_name)
            print("Country created:", country.as_dict() if country else "Error")

        elif choice == "7":
            countries = country_service.get_all_countries()
            print("Countries:", [country.as_dict() for country in countries])

        elif choice == "8":
            country_id = int(input("Country ID: "))
            description = input("Description: ")
            start_date = input("Start date (YYYY-MM-DD): ")
            end_date = input("End date (YYYY-MM-DD): ")
            price = float(input("Price: "))
            image_url = input("Image URL: ")
            vacation = vacation_service.create_vacation(country_id, description, start_date, end_date, price, image_url)
            print("Vacation created:", vacation.as_dict() if vacation else "Error")

        elif choice == "9":
            vacations = vacation_service.get_all_vacations()
            print("Vacations:", [vac.as_dict() for vac in vacations])

        elif choice == "10":
            user_id = int(input("User ID: "))
            vacation_id = int(input("Vacation ID: "))
            like = like_service.add_like(user_id, vacation_id)
            print("Vacation liked:", like.as_dict() if like else "Error")

        elif choice == "11":
            user_id = int(input("User ID: "))
            likes = like_service.get_likes_by_user(user_id)
            print("User's likes:", [like.as_dict() for like in likes])

        elif choice == "12":
            exists = input("Enter email to check: ")
            exists = user_service.check_email_exists(email)
            if exists:
                print("This email is already registered in the system.")
            else:
                print("This email is available.")

        elif choice == "13":
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = user_service.get_user_by_email_and_password(email, password)
            if user:
                print("User found:", user.as_dict())
            else:
                print("Error: User not found, please check your email and password!")


        elif choice == "14":
            user_id = int(input("Enter User ID: "))
            vacation_id = int(input("Enter Vacation ID: "))
            removed = like_service.remove_like(user_id, vacation_id)
            if removed:
                print("Like removed successfully")
            else:
                print("Error: Like not found or could not be removed")

        elif choice == "15":
            user_service.delete_user_by_input()

        elif choice == "16":
            vacation_id = int(input("Enter vacation ID to update: "))
            country_id = int(input("Country ID: "))
            description = input("Description: ")
            start_date = input("Start date (YYYY-MM-DD): ")
            end_date = input("End date (YYYY-MM-DD): ")
            price = float(input("Price: "))
            image_url = input("Image URL: ")
            vacation = vacation_service.update_vacation(vacation_id, country_id, description, start_date, end_date,price, image_url)
            if vacation:
                print("Vacation updated:", vacation.as_dict())
            else:
                print("Error updating vacation.")
        

        elif choice == "17":
            vacation_id = int(input("Enter Vacation ID to delete: "))
            deleted = vacation_service.delete_vacation(vacation_id)
            if deleted:
                print("Vacation and all related likes deleted successfully")
            else:
                print("Error: Vacation not found or could not be deleted")

        elif choice == "18":
            email = input("Enter email: ")
            password = input("Enter password: ")
            user = user_service.login(email, password)
            if user:
                print("User logged in:")
            else:
                print("Login failed, please check your email and password!")

        elif choice == "19":
            user_id = int(input("User ID: "))
            get_user_by_id = user_service.get_user_by_id(user_id)
            print("User found:", get_user_by_id.as_dict() if get_user_by_id else "Error")

        elif choice == "20":
            country_id = int(input("Country ID: "))
            get_country_by_id = country_service.get_country_by_id(country_id)
            print("User found:", get_country_by_id.as_dict() if get_country_by_id else "Error")

        elif choice == "21":
            vacation_id = int(input("Vacation ID: "))
            get_vacation_by_id = vacation_service.get_vacation_by_id(vacation_id)
            print("User found:", get_vacation_by_id.as_dict() if get_vacation_by_id else "Error")

        elif choice == "22":
            role_id = int(input("Role ID: "))
            get_role_by_id = role_service.get_role_by_id(role_id)
            print("User found:", get_role_by_id.as_dict() if get_role_by_id else "Error")

        elif choice == "23":
            country_id = int(input("Enter country ID to update: "))
            country_name = input("Name: ")
            country = country_service.update_country(country_id, country_name)
            if country:
                print("Country updated:", country.as_dict())
            else:
                print("Error updating country.")

        elif choice == "24":
            likes = like_service.get_all_likes()
            print("Users:", [like.as_dict() for like in likes])

        elif choice == "25":
            country_id = int(input("Enter Country ID to delete: "))
            deleted = country_service.delete_country(country_id)
            if deleted:
                print("Country deleted successfully, Make sure to update Vacations in deleted country!")
            else:
                print("Error: Country not found or could not be deleted")

        elif choice == "26":
            print("Exiting...")
            break



        else:
           print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
