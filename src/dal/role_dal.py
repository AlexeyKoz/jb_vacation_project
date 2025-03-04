from sqlalchemy.orm import Session
from src.models.role import Role

class RoleDAL:
    def __init__(self, db: Session):
        self.db = db

    def get_all_roles(self):
        try:
            return self.db.query(Role).all()
        except Exception as e:
            print(f"Error getting roles: {e}")
            return []

    def get_role_by_id(self, role_id: int):
        try:
            return self.db.query(Role).filter(Role.id == role_id).first()
        except Exception as e:
            print(f"Error getting role: {e}")
            return None

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