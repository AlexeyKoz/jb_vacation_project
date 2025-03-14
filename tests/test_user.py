from src.services.user_service import UserService
from conftest import db_session
from sqlalchemy.orm import Session


def test_user_registration_success(db_session):
    user_service = UserService(db_session)
    user = user_service.create_user("ben", "gvir", "bengvir@gmail.com", "asds", 2)

    assert user is not None
    assert user.email == "bengvir@gmail.com"

    db_session.delete(user)
    db_session.commit()


def test_user_registration_failed(db_session):
    user_service = UserService(db_session)
    user = user_service.create_user("asd", "gvir", "bengvir@gmail.com", "1234", 2)

    assert user is not None
    assert user.email == "bengvir@gmail.com"

    db_session.delete(user)
    db_session.commit()



def test_get_all_users(db_session):
    user_service = UserService(db_session)
    user = user_service.create_user("moshe", "rabenu", "mosherabenu@gmail.com", "1234", 2)
    users = user_service.get_all_users()

    assert len(users) == 1
    assert users[0].email == "mosherabenu@gmail.com"

    db_session.delete(user)
    db_session.commit()

def test_get_user_by_email_and_password(db_session):
    user_service = UserService(db_session)
    user_service.create_user("itzhak", "cohen", "itzhakcohen@gmail.com", "1234", 2)
    user = user_service.get_user_by_email_and_password("itzhakcohen@gmail.com", "1234")

    assert user is not None
    assert user.first_name == "itzhak"

    db_session.delete(user)
    db_session.commit()

def test_check_email_exists(db_session):
    user_service = UserService(db_session)
    user = user_service.create_user("elon", "musk", "elonmusk@gmail.com", "1234", 2)

    assert user_service.check_email_exists("elonmusk@gmail.com") is True

    db_session.delete(user)
    db_session.commit()


def test_delete_user(db_session):
    user_service = UserService(db_session)
    user = user_service.create_user("Mike", "Tyson", "miketyson@gmail.com", "asd", 2)
    deleted = user_service.delete_user(user.id)

    assert deleted is True
    assert user_service.get_user_by_id(user.id) is None

    db_session.commit()
