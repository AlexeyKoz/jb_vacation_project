from sqlalchemy import Column, Integer, String
from src.dal.base import Base

# This class represents the "countries" model .
class Country(Base):
    __tablename__ = "countries"

    # Each country has id and name.
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

    # This method is used to return the country as a dictionary for manual menu testing.
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
