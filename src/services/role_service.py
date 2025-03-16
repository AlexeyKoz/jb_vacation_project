from sqlalchemy.orm import Session
from src.dal.role_dal import RoleDAL


# Create a service for handle "Role" logic validation
class RoleService:
    def __init__(self, db: Session):
        self.role_dal = RoleDAL(db)

    # Methods for getting all roles
    def get_all_roles(self):
        return self.role_dal.get_all_roles()

    # Methods for getting specific role by id
    def get_role_by_id(self, role_id: int):
        return self.role_dal.get_role_by_id(role_id)

    # Methods for update specific role
    def update_role(self, role_id: int, name: str):
        return self.role_dal.update_role(role_id, name)

    # Method to create a new role
    def create_role(self, name: str):
        if name.lower() == "admin":
            existing_admin = self.role_dal.get_role_by_id(1)
            if existing_admin:
                raise ValueError("There can be only one administrator in the system")
        return self.role_dal.create_role(name)

    # Method to delete a role
    def delete_role(self, role_id: int):
        if role_id == 1:
            raise ValueError("Administrator role cannot be deleted")
        return self.role_dal.delete_role(role_id)
