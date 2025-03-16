from src.services.user_service import UserService
from conftest import db_session
from sqlalchemy.orm import Session
from src.services.country_service import CountryService


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



def test_login_positive(db_session):
    user_service = UserService(db_session)
    user = user_service.create_user("Bibi", "Netanyahu", "bibiNetanyahu@gmail.com","1234",role_id=2)
    login = user_service.login("bibiNetanyahu@gmail.com", "1234")
    db_session.commit()

    assert login is not None
    assert login.email == "bibiNetanyahu@gmail.com"
    assert login.password == "1234"

    db_session.delete(user)
    db_session.commit()

def test_login_negative(db_session):
    user_service = UserService(db_session)
    user = user_service.create_user("Bibi", "Netanyahu", "bibiNetanyahu@gmail.com", "1234", role_id=2)
    login = user_service.login("bibiNetanyahu@gmail.com", "12")
    db_session.commit()

    assert login is not None
    assert login.email == "bibiNetanyahu@gmail.com"
    assert login.password == "1234"

    db_session.delete(user)
    db_session.commit()


from src.services.like_service import LikeService
from src.services.vacation_service import VacationService
from src.services.user_service import UserService


def test_like_and_unlike_vacation(db_session):
    user_service = UserService(db_session)
    vacation_service = VacationService(db_session)
    like_service = LikeService(db_session)

    user = user_service.create_user("Nasrin", "Kadri", "nasrinKadri@gmai.com", "1234", 2)
    country = vacation_service.create_country("Japan")
    vacation = vacation_service.create_vacation(1, "Japan Trip", "2025-07-01", "2025-07-10", 1700.00, "japan.jpg")

    commit = db_session.commit()

    # like = like_service.add_like(user.id, vacation.id)
    # assert like is not None
    #
    # commit = db_session.commit()
    #
    # removed = like_service.remove_like(user.id, vacation.id)
    # assert removed is True
    #
    # commit  = db_session.commit()