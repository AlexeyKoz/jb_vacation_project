from sqlalchemy.orm import Session
from src.dal.vacation_dal import VacationDAL

# Create a service for handle "Vacation" logic validation
class VacationService:
    def __init__(self, db: Session):
        self.vacation_dal = VacationDAL(db)

    # Methods for getting all vacations
    def get_all_vacations(self):
        return self.vacation_dal.get_all_vacations()

    # Methods for getting  specific vacation by id
    def get_vacation_by_id(self, vacation_id: int):
        return self.vacation_dal.get_vacation_by_id(vacation_id)

    # Methods for create a new vacation
    def create_vacation(self, country_id: int, description: str, start_date, end_date, price: float,image_url: str):
        return self.vacation_dal.create_vacation(country_id, description, start_date, end_date, price, image_url)

    # Methods for update a vacation
    def update_vacation(self, vacation_id: int, country_id: int, description: str, start_date, end_date, price: float, image_url: str):
        return self.vacation_dal.update_vacation(vacation_id, country_id, description, start_date, end_date, price, image_url)

    # Methods for delete a vacation
    def delete_vacation(self, vacation_id: int):
        return self.vacation_dal.delete_vacation(vacation_id)