from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.dal.base import Base

# This class represents the "users" model.
class User(Base):
    __tablename__ = "users"

    # Each user has id, first_name, last_name, email, password, and role_id.
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"))

    role = relationship("Role")

    # This method is used to return the user as a dictionary for manual menu testing.
    def as_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "role_id": self.role_id
        }
