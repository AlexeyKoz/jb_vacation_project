from sqlalchemy.orm import Session
from src.dal.vacation_dal import VacationDAL

class VacationService:
    def __init__(self, db: Session):
        self.vacation_dal = VacationDAL(db)

    def get_all_vacations(self):
        return self.vacation_dal.get_all_vacations()

    def get_vacation_by_id(self, vacation_id: int):
        return self.vacation_dal.get_vacation_by_id(vacation_id)

    def create_vacation(self, country_id: int, description: str, start_date, end_date, price: float, image_url: str):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if start_date >= end_date:
            raise ValueError("Start date must be before end date")
        return self.vacation_dal.create_vacation(country_id, description, start_date, end_date, price, image_url)
