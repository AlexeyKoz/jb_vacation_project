from src.services.user_service import UserService

def test_create_user(db_session):
    user_service = UserService(db_session)
    user = user_service.create_user("John", "Doe", "john@example.com", "1234", 2)

    assert user is not None
    assert user.email == "john@example.com"

def test_get_all_users(db_session):
    user_service = UserService(db_session)
    user_service.create_user("Alice", "Smith", "alice@example.com", "1234", 2)
    users = user_service.get_all_users()

    assert len(users) == 1
    assert users[0].email == "alice@example.com"

def test_get_user_by_email_and_password(db_session):
    user_service = UserService(db_session)
    user_service.create_user("Bob", "Brown", "bob@example.com", "1234", 2)
    user = user_service.get_user_by_email_and_password("bob@example.com", "1234")

    assert user is not None
    assert user.first_name == "Bob"

def test_check_email_exists(db_session):
    user_service = UserService(db_session)
    user_service.create_user("Eve", "Adams", "eve@example.com", "1234", 2)

    assert user_service.check_email_exists("eve@example.com") is True
    assert user_service.check_email_exists("unknown@example.com") is False

def test_delete_user(db_session):
    user_service = UserService(db_session)
    user = user_service.create_user("Mike", "Tyson", "mike@example.com", "1234", 2)
    deleted = user_service.delete_user(user.id)

    assert deleted is True
    assert user_service.get_user_by_id(user.id) is None
