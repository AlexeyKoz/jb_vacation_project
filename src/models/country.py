from sqlalchemy import Column, Integer, String
from src.dal.base import Base


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
