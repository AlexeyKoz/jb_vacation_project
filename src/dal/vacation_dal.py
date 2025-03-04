from sqlalchemy.orm import Session
from src.models.vacation import Vacation

class VacationDAL:
    def __init__(self, db: Session):
        self.db = db

    def get_all_vacations(self):
        try:
            return self.db.query(Vacation).all()
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
        except Exception as e:
            print(f"Error creating vacation: {e}")
            self.db.rollback()
            return None