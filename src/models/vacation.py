from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship
from src.dal.base import Base

# This class represents the "vacations" model.
class Vacation(Base):
    __tablename__ = "vacations"

    # Each vacation has id, country_id, description, start_date, end_date, price, and image_url.
    id = Column(Integer, primary_key=True, index=True)
    country_id = Column(Integer, ForeignKey("countries.id", ondelete="CASCADE"))
    description = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    image_url = Column(String)

    country = relationship("Country")


    # This method is used to return the vacation as a dictionary for manual menu testing.
    def as_dict(self):
        return {
            "id": self.id,
            "country_id": self.country_id,
            "description": self.description,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "price": float(self.price),
            "image_url": self.image_url,
        }
