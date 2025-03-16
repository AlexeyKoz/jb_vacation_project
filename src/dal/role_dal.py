from sqlalchemy.orm import Session
from src.models.role import Role


# This class is used to interact with "Role" table in database
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

    # This method is used to get a role by user id from database.
    def get_role_by_id(self, role_id: int):
        try:
            return self.db.query(Role).filter(Role.id == role_id).first()
        except Exception as e:
            print(f"Error getting role: {e}")
            return None

    # This method is used to create a new role exept admin role(like VIP user, etc...).
    # Admin role is created only once in the database manually(project requirement).
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
    # Admin role cannot be deleted(project requirement).
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

    # This method is used to change a role in the database.
    # Admin role cannot be changed(project requirement).
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