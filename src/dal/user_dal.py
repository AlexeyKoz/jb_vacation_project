from sqlalchemy.orm import Session
from src.models.user import User


# This class is used to interact with the database
class UserDAL:
    def __init__(self, db: Session):
        self.db = db


    # This method is used to get a user by its id.
    def get_user_by_id(self, user_id: int):
        try:
            return self.db.query(User).filter(User.id == user_id).first()
        except Exception as e:
            print(f"Error getting user: {e}")
            return None



    # This method is used to get a user by its email.
    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()



    # This method is used to get all users from the database.
    def get_all_users(self):
        try:
            return self.db.query(User).all()
        except Exception as e:
            print(f"Error getting users: {e}")
            return []


    # This method is used to create a new user in the database.
    def create_user(self, first_name: str, last_name: str, email: str, password: str, role_id: int):
        try:
            new_user = User(first_name=first_name, last_name=last_name, email=email, password=password, role_id=role_id)
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return new_user
        except Exception as e:
            print(f"Error creating user: {e}")
            self.db.rollback()
            return None


    # This method is used to delete a user from the database.
    def delete_user(self, user_id: int):
        try:
            user = self.get_user_by_id(user_id)
            if user:
                self.db.delete(user)
                self.db.commit()
                return True
            return False
        except Exception as e:
            print(f"Error deleting user: {e}")
            self.db.rollback()
            return False


    # This method is used to update a user's role in the database.
    def update_user_role(self, user_id: int, new_role_id: int):
                try:
                    user = self.db.query(User).filter(User.id == user_id).first()
                    if not user:
                        return None
                    user.role_id = new_role_id
                    self.db.commit()
                    self.db.refresh(user)
                    return user
                except Exception as e:
                    print(f"Error updating user role: {e}")
                    self.db.rollback()
                    return None

    # This method is used to check if an email already exists in the database.
    def check_email_exists(self, email: str):
        try:
            return self.db.query(User).filter(User.email == email).first() is not None
        except Exception as e:
            print(f"Error checking email: {e}")
            return False


    # This method is used to recive all user data by recognized email and password.
    def get_user_by_email_and_password(self, email: str, password: str):
        try:
            return self.db.query(User).filter(User.email == email, User.password == password).first()
        except Exception as e:
            print(f"Error retrieving user: {e}")
            return None


    # This method is used to login a user by email and password.
    def login(self, email: str, password: str):
        try:
            user = self.get_user_by_email_and_password(email, password)
            if user:
                return user
            return None
        except Exception as e:
            print(f"Error logging in: {e}")
            return None