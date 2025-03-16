from sqlalchemy.orm import Session
from src.dal.country_dal import CountryDAL


# Create a service for the `countries` table
class CountryService:
    def __init__(self, db: Session):
        self.country_dal = CountryDAL(db)

    # Methods of getting all countries
    def get_all_countries(self):
        return self.country_dal.get_all_countries()

    # Methods to get a country by id
    def get_country_by_id(self, country_id: int):
        return self.country_dal.get_country_by_id(country_id)

    # Method to create a country
    def create_country(self, name: str):
        existing_country = self.country_dal.get_country_by_id(id)
        if existing_country:
            raise ValueError("Country already exists")
        return self.country_dal.create_country(name)

    # Method to delete a country
    def delete_country(self, country_id: int):
        return self.country_dal.delete_country(country_id)
