from sqlalchemy.orm import Session
from src.models.vacation import Vacation
from datetime import datetime
from src.models.like import Like


# This class is used to interact with the "vacations" table in the database
class VacationDAL:
    def __init__(self, db: Session):
        self.db = db

    # This method is used to get all vacations from the database.
    def get_all_vacations(self):
        try:
            return self.db.query(Vacation).order_by(Vacation.start_date).all()  # Ordering by start_date
        except Exception as e:
            print(f"Error getting vacations: {e}")
            return []

    # This method is used to get a vacation by its id from the database.
    def get_vacation_by_id(self, vacation_id: int):
        try:
            return self.db.query(Vacation).filter(Vacation.id == vacation_id).first()
        except Exception as e:
            print(f"Error getting vacation: {e}")
            return None

    # This method is used to create a new vacation with a couple of rules.
    def create_vacation(self, country_id: int, description: str, start_date, end_date, price: float, image_url: str):
        try:
            # Convert start_date and end_date to datetime.date if they are strings
            if isinstance(start_date, str):
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            if isinstance(end_date, str):
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

            # Rule 1: Price can't be above 10,000 or negative
            if price < 0 or price > 10000:
                raise ValueError("Price must be between 0 and 10,000.")

            # Rule 2: Start date can't be after end date
            if start_date >= end_date:
                raise ValueError("Start date must be before end date.")

            # Rule 3: Start date can't be in the past
            if start_date < datetime.today().date():
                raise ValueError("Start date cannot be in the past.")

            # If all rules pass, create the vacation entry
            new_vacation = Vacation(
                country_id=country_id,
                description=description,
                start_date=start_date,
                end_date=end_date,
                price=price,
                image_url=image_url
            )
            self.db.add(new_vacation)
            self.db.commit()
            self.db.refresh(new_vacation)
            return new_vacation

        # Catching specific exceptions and rolling back the transaction
        except ValueError as e:
            print(f"Error creating vacation: {e}")
            self.db.rollback()
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.db.rollback()
            return None

    # This method is used to update a specific existing vacation in the database.
    # keep tracking of the rules.
    def update_vacation(self, vacation_id: int, country_id: int, description: str, start_date, end_date,price: float, image_url: str):
        try:
            # Fetch the existing vacation
            vacation = self.db.query(Vacation).filter(Vacation.id == vacation_id).first()
            if not vacation:
                raise ValueError("Vacation not found.")
            # Convert string dates to datetime.date if needed
            if isinstance(start_date, str):
                start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            if isinstance(end_date, str):
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            # Rule 1: Price can't be above 10,000 or negative
            if price < 0 or price > 10000:
                raise ValueError("Price must be between 0 and 10,000.")
            # Rule 2: Start date can't be after end date
            if start_date >= end_date:
                raise ValueError("Start date must be before end date.")

            # Update the vacation fields
            vacation.country_id = country_id
            vacation.description = description
            vacation.start_date = start_date
            vacation.end_date = end_date
            vacation.price = price
            vacation.image_url = image_url
            # Commit the changes to the database
            self.db.commit()
            self.db.refresh(vacation)
            return vacation

        # Catching specific exceptions and rolling back the transaction
        except ValueError as e:
            print(f"Error updating vacation: {e}")
            self.db.rollback()
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.db.rollback()

            return None

    # This method is used to delete a vacation from the database.
    def delete_vacation(self, vacation_id: int):
        try:

            self.db.query(Like).filter(Like.vacation_id == vacation_id).delete()

            deleted_rows = self.db.query(Vacation).filter(Vacation.id == vacation_id).delete()
            self.db.commit()
            return deleted_rows > 0
        except Exception as e:
            print(f"Error deleting vacation: {e}")
            self.db.rollback()
            return False