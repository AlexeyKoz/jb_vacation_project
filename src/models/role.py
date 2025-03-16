from sqlalchemy import Column, Integer, String
from src.dal.base import Base

# This class represents the "roles" model.
class Role(Base):
    __tablename__ = "roles"

    # Each role has id and name.
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True, nullable=False)

    # This method is used to return the role as a dictionary for manual menu testing.
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
