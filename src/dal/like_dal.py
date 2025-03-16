from sqlalchemy.orm import Session
from src.models.like import Like

# This class is used to interact with "like" table in database
class LikeDAL:
    def __init__(self, db: Session):
        self.db = db


    # This method is used to see all likes from specific user in the database.
    def get_likes_by_user(self, user_id: int):
        try:
            return self.db.query(Like).filter(Like.user_id == user_id).all()
        except Exception as e:
            print(f"Error getting likes for user {user_id}: {e}")
            return []

    # This method is used to get all likes from the database by all users.
    def get_all_likes(self):
        try:
            return self.db.query(Like).all()
        except Exception as e:
            print(f"Error getting users: {e}")
            return []

    # This method is used to see all likes for a specific vacation.
    def get_likes_by_vacation(self, vacation_id: int):
        try:
            return self.db.query(Like).filter(Like.vacation_id == vacation_id).all()
        except Exception as e:
            print(f"Error getting likes for vacation {vacation_id}: {e}")
            return []

    # This method is used to add a new like from specific user to specific vacation.
    def add_like(self, user_id: int, vacation_id: int):
        try:
            existing_like = self.db.query(Like).filter(
                Like.user_id == user_id, Like.vacation_id == vacation_id
            ).first()
            if existing_like:
                print(f"User {user_id} already liked vacation {vacation_id}")
                return None

            new_like = Like(user_id=user_id, vacation_id=vacation_id)
            self.db.add(new_like)
            self.db.commit()
            return new_like
        except Exception as e:
            print(f"Error adding like: {e}")
            self.db.rollback()
            return None

    # This method is used to remove a like from specific user to specific vacation.
    def remove_like(self, user_id: int, vacation_id: int):
        try:
            like = self.db.query(Like).filter(
                Like.user_id == user_id, Like.vacation_id == vacation_id
            ).first()
            if like:
                self.db.delete(like)
                self.db.commit()
                return True
            return False
        except Exception as e:
            print(f"Error removing like: {e}")
            self.db.rollback()
            return False
