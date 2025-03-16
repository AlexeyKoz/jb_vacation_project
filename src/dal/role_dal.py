from sqlalchemy.orm import Session
from src.models.role import Role


# This class is used to interact with the database
class RoleDAL:
    def __init__(self, db: Session):
        self.db = db

    # This method is used to get all roles from the database.
    def get_all_roles(self):
        try:
            return self.db.query(Role).all()
        except Exception as e:
            print(f"Error getting roles: {e}")
            return []



    # This method is used to get a role by its ID.
    def get_role_by_id(self, role_id: int):
        try:
            return self.db.query(Role).filter(Role.id == role_id).first()
        except Exception as e:
            print(f"Error getting role: {e}")
            return None


    # This method is used to create a new role in the database.
    def create_role(self, name: str):
        try:
            new_role = Role(name=name)
            self.db.add(new_role)
            self.db.commit()
            self.db.refresh(new_role)
            return new_role
        except Exception as e:
            print(f"Error creating role: {e}")
            self.db.rollback()
            return None



    # This method is used to delete a role from the database.
    def delete_role(self, role_id: int):
        try:
            role = self.get_role_by_id(role_id)
            if role:
                self.db.delete(role)
                self.db.commit()
                return True
            return False
        except Exception as e:
            print(f"Error deleting role: {e}")
            self.db.rollback()
            return False



    # This method is used to update a role (exept admin role)
    # in case we will create more roles in the future.
    def update_role(self, role_id: int, name: str):
        try:
            role = self.get_role_by_id(role_id)
            if role:
                role.name = name
                self.db.commit()
                return role
            return None
        except Exception as e:
            print(f"Error updating role: {e}")
            self.db.rollback()
            return None