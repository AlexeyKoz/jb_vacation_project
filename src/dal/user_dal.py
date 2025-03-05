from sqlalchemy.orm import Session
from src.models.user import User

class UserDAL:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, user_id: int):
        try:
            return self.db.query(User).filter(User.id == user_id).first()
        except Exception as e:
            print(f"Error getting user: {e}")
            return None

    def get_all_users(self):
        try:
            return self.db.query(User).all()
        except Exception as e:
            print(f"Error getting users: {e}")
            return []

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



    def check_email_exists(self, email: str):
        try:
            return self.db.query(User).filter(User.email == email).first() is not None
        except Exception as e:
            print(f"Error checking email: {e}")
            return False