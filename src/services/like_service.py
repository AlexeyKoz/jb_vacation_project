from sqlalchemy.orm import Session
from src.dal.like_dal import LikeDAL

class LikeService:
    def __init__(self, db: Session):
        self.like_dal = LikeDAL(db)

    def get_likes_by_user(self, user_id: int):
        return self.like_dal.get_likes_by_user(user_id)

    def get_all_likes(self):
        return self.like_dal.get_all_likes()

    def get_likes_by_vacation(self, vacation_id: int):
        return self.like_dal.get_likes_by_vacation(vacation_id)

    def add_like(self, user_id: int, vacation_id: int):
        existing_like = self.like_dal.get_likes_by_user(user_id)
        for like in existing_like:
            if like.vacation_id == vacation_id:
                raise ValueError("User has already liked this vacation")
        return self.like_dal.add_like(user_id, vacation_id)

    def remove_like(self, user_id: int, vacation_id: int):
        return self.like_dal.remove_like(user_id, vacation_id)