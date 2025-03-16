from sqlalchemy import Column, Integer, ForeignKey
from src.dal.base import Base
from sqlalchemy.orm import relationship

# This class represents the "likes" model.
class Like(Base):
    __tablename__ = "likes"

    # Each like has a user_id and a vacation_id.
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    vacation_id = Column(Integer, ForeignKey("vacations.id", ondelete="CASCADE"), primary_key=True)

    user = relationship("User")
    vacation = relationship("Vacation")

    # This method is used to return the like as a dictionary for manual menu testing.
    def as_dict(self):
        return {
            "user_id": self.user_id,
            "vacation_id": self.vacation_id
        }
