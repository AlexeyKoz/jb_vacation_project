from sqlalchemy.orm import Session
from src.models.country import Country


# This class is used to interact with "Country" table in database.
class CountryDAL:
    def __init__(self, db: Session):
        self.db = db

    # This method is used to get all countries from the database.
    def get_all_countries(self):
        try:
            return self.db.query(Country).all()
        except Exception as e:
            print(f"Error getting countries: {e}")
            return []

    # This method is used to get a country by id from database.
    def get_country_by_id(self, country_id: int):
        try:
            return self.db.query(Country).filter(Country.id == country_id).first()
        except Exception as e:
            print(f"Error getting country: {e}")
            return None

    #  This method is used to get a country by its name.
    def get_country_by_name(self, country_name: str):
        try:
            return self.db.query(Country).filter(Country.name == country_name).first()
        except Exception as e:
            print(f"Error getting country: {e}")
            return None

    # This method is used to create a new country in the database.
    def create_country(self, name: str):
        try:
            new_country = Country(name=name)
            self.db.add(new_country)
            self.db.commit()
            self.db.refresh(new_country)
            return new_country
        except Exception as e:
            print(f"Error creating country: {e}")
            self.db.rollback()
            return None


    # This method is used delete a country from the database.
    def delete_country(self, country_id: int):
        try:
            country = self.get_country_by_id(country_id)
            if country:
                self.db.delete(country)
                self.db.commit()
                return True
            return False
        except Exception as e:
            print(f"Error deleting country: {e}")
            self.db.rollback()
            return False

    # This method is used to update a country in the database.
    def update_country(self,country_id: int, name: str):
        try:
            # Fetch the existing country
            country = self.db.query(Country).filter(Country.id == country_id).first()
            country2 = self.db.query(Country).filter(Country.name == name).first()
            if not country and not country2:
                raise ValueError("Vacation not found.")


            # Update the country fields
            country.name = name
            # Commit the changes to the database
            self.db.commit()
            self.db.refresh(country)
            return country

        # Handle the error's
        except ValueError as e:
            print(f"Error updating vacation: {e}")
            self.db.rollback()
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.db.rollback()

            return None