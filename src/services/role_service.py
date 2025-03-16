from sqlalchemy.orm import Session
from src.dal.role_dal import RoleDAL

# Create a service for the `roles` table
class RoleService:
    def __init__(self, db: Session):
        self.role_dal = RoleDAL(db)

    # Define the methods of the `RoleService` class
    def get_all_roles(self):
        return self.role_dal.get_all_roles()

    # Define the methods of the `RoleService` class
    def get_role_by_id(self, role_id: int):
        return self.role_dal.get_role_by_id(role_id)

    # Define the methods of the `RoleService` class
    def update_role(self, role_id: int, name: str):
        return self.role_dal.update_role(role_id, name)


    # Define the methods of the `RoleService` class
    def create_role(self, name: str):
        if name.lower() == "admin":
            existing_admin = self.role_dal.get_role_by_id(1)
            if existing_admin:
                raise ValueError("There can be only one administrator in the system")
        return self.role_dal.create_role(name)

    # Define the methods of the `RoleService` class
    def delete_role(self, role_id: int):
        if role_id == 1:
            raise ValueError("Administrator role cannot be deleted")
        return self.role_dal.delete_role(role_id)
