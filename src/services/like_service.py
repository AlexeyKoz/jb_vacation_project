from sqlalchemy.orm import Session
from src.dal.like_dal import LikeDAL

# Create a service for handle "like" logic validation
class LikeService:
    def __init__(self, db: Session):
        self.like_dal = LikeDAL(db)


    # Methods for getting like by specific user
    def get_likes_by_user(self, user_id: int):
        return self.like_dal.get_likes_by_user(user_id)

    # Methods for getting all likes
    def get_all_likes(self):
        return self.like_dal.get_all_likes()

    # Methods for getting like by specific vacation
    def get_likes_by_vacation(self, vacation_id: int):
        return self.like_dal.get_likes_by_vacation(vacation_id)

    # Method to add like by specific user
    def add_like(self, user_id: int, vacation_id: int):
        existing_like = self.like_dal.get_likes_by_user(user_id)
        for like in existing_like:
            if like.vacation_id == vacation_id:
                raise ValueError("User has already liked this vacation")
        return self.like_dal.add_like(user_id, vacation_id)


    # Method to remove like by specific user
    def remove_like(self, user_id: int, vacation_id: int):
        return self.like_dal.remove_like(user_id, vacation_id)