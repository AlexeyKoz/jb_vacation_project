from sqlalchemy import Column, Integer, String
from src.dal.base import Base

# Create a model for the `countries` table
class Country(Base):
    __tablename__ = "countries"

    #  Define the columns of the `countries` table
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

    # Define the representation of the `Country` model
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
