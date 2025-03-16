from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.dal.base import Base

# Create a model for the `users` table
class User(Base):
    __tablename__ = "users"


    # Define the columns of the `users` table
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id", ondelete="CASCADE"))
    role = relationship("Role")


    # Define the representation of the `User` model
    def as_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "role_id": self.role_id
        }
