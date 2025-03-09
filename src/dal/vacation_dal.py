from sqlalchemy.orm import Session
from src.models.vacation import Vacation
from datetime import datetime

class VacationDAL:
    def __init__(self, db: Session):
        self.db = db

    def get_all_vacations(self):
        try:
            return self.db.query(Vacation).order_by(Vacation.start_date).all()  # Ordering by start_date
        except Exception as e:
            print(f"Error getting vacations: {e}")
            return []

    def get_vacation_by_id(self, vacation_id: int):
        try:
            return self.db.query(Vacation).filter(Vacation.id == vacation_id).first()
        except Exception as e:
            print(f"Error getting vacation: {e}")
            return None

    def create_vacation(self, country_id: int, description: str, start_date, end_date, price: float, image_url: str):
        try:
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

        except ValueError as e:
            print(f"Error creating vacation: {e}")
            self.db.rollback()
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.db.rollback()
            return None