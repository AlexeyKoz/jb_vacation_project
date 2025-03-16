from sqlalchemy.orm import Session
from src.dal.country_dal import CountryDAL


# Create a service for handle "countries" logic validation
class CountryService:
    def __init__(self, db: Session):
        self.country_dal = CountryDAL(db)

    # Methods for getting all countries
    def get_all_countries(self):
        return self.country_dal.get_all_countries()

    # Methods for getting  specific country by id
    def get_country_by_id(self, country_id: int):
        return self.country_dal.get_country_by_id(country_id)

    # Methods for getting specific country by its name
    def get_country_by_name(self, country_name: str):
        return self.country_dal.get_country_by_name(country_name)

    # Method to create a new country
    def create_country(self, name: str):
        existing_country = self.country_dal.get_country_by_name(name)
        if existing_country:
            raise ValueError("Country already exists")
        return self.country_dal.create_country(name)

    # Method to delete a country
    def delete_country(self, country_id: int):
        return self.country_dal.delete_country(country_id)

    # Method to update a country
    def update_country(self, country_id: int, country_name: str):
        return self.country_dal.update_country(country_id, country_name)
