from sqlalchemy import Column, Integer, ForeignKey
from src.dal.base import Base
from sqlalchemy.orm import relationship


class Like(Base):
    __tablename__ = "likes"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    vacation_id = Column(Integer, ForeignKey("vacations.id", ondelete="CASCADE"), primary_key=True)

    user = relationship("User")
    vacation = relationship("Vacation")

    def as_dict(self):
        return {
            "user_id": self.user_id,
            "vacation_id": self.vacation_id
        }
