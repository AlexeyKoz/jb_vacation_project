from sqlalchemy import Column, Integer, ForeignKey
from src.dal.base import Base
from sqlalchemy.orm import relationship


# Create a model for the `likes` table
class Like(Base):
    __tablename__ = "likes"

    # Define the columns of the `likes` table
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    vacation_id = Column(Integer, ForeignKey("vacations.id", ondelete="CASCADE"), primary_key=True)

    # Define the representation of the `Like` model
    user = relationship("User")
    vacation = relationship("Vacation")

    # Define the representation of the `Like` model
    def as_dict(self):
        return {
            "user_id": self.user_id,
            "vacation_id": self.vacation_id
        }
