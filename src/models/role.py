from sqlalchemy import Column, Integer, String
from src.dal.base import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), unique=True, nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
