from src.services.user_service import UserService
from conftest import db_session
from sqlalchemy.orm import Session
from src.services.country_service import CountryService
from src.services.like_service import LikeService
from src.services.vacation_service import VacationService



def test_user_registration_success(db_session):
    user_service = UserService(db_session)
    user = user_service.create_user("ben", "gvir", "bengvir@gmail.com", "asds", 2)

    try:
        assert user is not None
        assert isinstance(user.email, str)
    finally:
        db_session.delete(user)
        db_session.commit()


def test_user_registration_failed(db_session):
    user_service = UserService(db_session)
    user = user_service.create_user("asd", "gvir", 123123 , "1234", 2)

    try:
        assert user.email is str
        assert user is not None

    finally:
        db_session.delete(user)
        db_session.commit()



def test_login_positive(db_session):
    user_service = UserService(db_session)
    user = user_service.create_user("Bibi", "Netanyahu", "bibiNetanyahu@gmail.com","1234",role_id=2)
    login = user_service.login("bibiNetanyahu@gmail.com", "1234")
    db_session.commit()

    try:
        assert login is not None
        assert login.email == "bibiNetanyahu@gmail.com"
        assert login.password == "1234"

    finally:
        db_session.delete(user)
        db_session.commit()

def test_login_negative(db_session):
    user_service = UserService(db_session)
    user = user_service.create_user("bibi", "Netanyahu", "bibiNetanyahu@gmail.com", "1234", role_id=2)

    try:
        login = user_service.login("", "1234")
        assert login.email is not None

    finally:
        db_session.delete(user)
        db_session.commit()



def test_like_vacation_positive(db_session):
    user_service = UserService(db_session)
    country_service = CountryService(db_session)
    vacation_service = VacationService(db_session)
    like_service = LikeService(db_session)

    user = user_service.create_user("Nasrin", "Kadri", "nasrinKadri@gmai.com", "1234", 2)
    country = country_service.create_country("Japan")
    country_id = country.id
    vacation = vacation_service.create_vacation(country_id, "Japan Trip", "2025-07-01", "2025-07-10", 1700.00, "japan.jpg")

    try:
        like = like_service.add_like(user.id, vacation.id)
        assert like is not None
        unlike = like_service.remove_like(user.id, vacation.id)
        assert unlike is True

    finally:
        db_session.delete(user)
        db_session.delete(country)
        db_session.delete(vacation)
        db_session.commit()

def test_like_vacation_negative(db_session):
    user_service = UserService(db_session)
    country_service = CountryService(db_session)
    vacation_service = VacationService(db_session)
    like_service = LikeService(db_session)

    user = user_service.create_user("Nasrin", "Kadri", "nasrinKadri@gmai.com", "1234", 2)
    country = country_service.create_country("Japan")
    country_id = country.id
    vacation = vacation_service.create_vacation(country_id, "Japan Trip", "2025-07-01", "2025-07-10", 1700.00, "japan.jpg")

    try:
        like = like_service.add_like("domines", vacation.id)
        assert like is not None
        unlike = like_service.remove_like(user.id, vacation.id)
        assert unlike is True

    finally:
        db_session.delete(user)
        db_session.delete(country)
        db_session.delete(vacation)
        db_session.commit()

