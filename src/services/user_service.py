from sqlalchemy.orm import Session
from src.dal.user_dal import UserDAL
import re


# Create a service for handle "User" logic validation
class UserService:
    def __init__(self, db: Session):
        self.user_dal = UserDAL(db)

    # Methods for getting all users
    def get_all_users(self):
        return self.user_dal.get_all_users()

    # Methods for getting specific user by id
    def get_user_by_id(self, user_id: int):
        return self.user_dal.get_user_by_id(user_id)

    # Methods for creating a new user exept admin with couple rules:
    def create_user(self, first_name: str, last_name: str, email: str, password: str, role_id: int):
        existing_user = self.user_dal.get_user_by_email(email)

        # Rule1: Check if user with this email already exists
        if existing_user:
            raise ValueError("User with this email already exists")

        #  Rule2: Check if email is in a valid format
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format")

        # Rule3: Check if password is at least 4 digits long
        if len(password) < 4:
            raise ValueError("Password must be at least 4 digits long")

        # Rule4: Check if all required fields are filled
        if not first_name or not last_name or not email or not password or not role_id:
            raise ValueError("Failed to create user: please make sure you've filled all the required fields")

        return self.user_dal.create_user(first_name, last_name, email, password, role_id)


    # Method to delete user by id
    def delete_user_by_input(self):
        try:
            user_id = int(input("Enter User ID to delete: "))
            success = self.delete_user(user_id)  # Now this method exists!
            if success:
                print(f"User with ID {user_id} deleted successfully.")
            else:
                print("Error: User not found or could not be deleted.")
        except ValueError:
            print("Invalid input! Please enter a valid numeric User ID.")


    # Method to delete user
    def delete_user(self, user_id: int):
        return self.user_dal.delete_user(user_id)


    # Method to update user role
    def update_user_role(self, user_id: int, new_role_id: int):
        if new_role_id == 1:
            raise ValueError("Cannot assign administrator role manually")
        user = self.user_dal.update_user_role(user_id, new_role_id)
        return user

    # Method to check if email exists
    def check_email_exists(self, email: str):
            return self.user_dal.check_email_exists(email)

    #
    def get_user_by_email_and_password(self, email: str, password: str):
        if not password.isdigit() or len(password) < 4:
            raise ValueError("Password must be at least 4 digits long")

        return self.user_dal.get_user_by_email_and_password(email, password)

    # Method to checking if the email is in a valid format
    def is_valid_email(self, email: str):
        """Сhecks if the email is in a valid format"""
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None


    # Method to login
    def login(self, email: str, password: str):
        if email == "" or password == "":
            raise ValueError("Please enter email and password")
        elif not self.is_valid_email(email):
            raise ValueError("Invalid email format")
        elif len(password) < 4:
            raise ValueError("Password must be at least 4 digits")
        return self.user_dal.login(email, password)