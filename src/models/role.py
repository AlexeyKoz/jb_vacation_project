from sqlalchemy import Column, Integer, String
from src.dal.base import Base

# Create a model for the `roles` table
class Role(Base):
    __tablename__ = "roles"


    # Define the columns of the `roles` table
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True, nullable=False)


    # Define the representation of the `Role` model
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
