from src.services.vacation_service import VacationService
from src.services.country_service import CountryService

# 1) vacation creation positive test - expected to pass

def test_create_vacation_positive(db_session):
    vacation_service = VacationService(db_session)
    country_service = CountryService(db_session)
    country = country_service.create_country("Japan")
    country_id = country.id

    try:
        vacation = vacation_service.create_vacation(country_id, "Trip to Bali", "2025-06-01", "2025-06-10", 1500.00,"bali.jpg")
        assert vacation is not None
        assert vacation.description == "Trip to Bali"

    finally:
        db_session.delete(country)
        db_session.commit()

# 1) vacation creation negative test - expected to fail

def test_create_vacation_negative(db_session):
    vacation_service = VacationService(db_session)
    country_service = CountryService(db_session)
    country = country_service.create_country("Japan")
    country_id = country.id

    try:
        vacation = vacation_service.create_vacation(country_id, "Trip to Bali", "2025-06-01", "2025-05-10", 1500.00,"bali.jpg")
        assert vacation is not None
        assert vacation.description == "Trip to Bali"

    finally:
        db_session.delete(country)
        db_session.commit()

# 2) get all vacations positive test - expected to pass

def test_get_all_vacations_positive(db_session):
    vacation_service = VacationService(db_session)
    country_service = CountryService(db_session)
    country = country_service.create_country("Japan")
    country2 = country_service.create_country("Norway")
    country_id = country.id
    country_id2 = country2.id
    vacation_service.create_vacation(country_id, "Tokyo Trip", "2025-08-12", "2025-08-22", 4000.00, "Tokyo.jpg")
    vacation_service.create_vacation(country_id2, "Oslo Trip", "2025-08-01", "2025-08-15", 2000.00, "Oslo.jpg")
    vacations = vacation_service.get_all_vacations()

    try:
        assert len(vacations) == 2

    finally:
        db_session.delete(country)
        db_session.delete(country2)
        db_session.commit()

# 2) get all vacations negative test - expected to fail

def test_get_all_vacations_negative(db_session):
    vacation_service = VacationService(db_session)
    country_service = CountryService(db_session)
    country = country_service.create_country("Japan")
    country2 = country_service.create_country("Norway")
    country_id = country.id
    country_id2 = country2.id
    vacation_service.create_vacation(country_id, "Tokyo Trip", "2025-08-12", "2025-08-22", 4000.00, "Tokyo.jpg")
    vacation_service.create_vacation(country_id2, "Oslo Trip", "2025-08-01", "2025-08-15", 20000.00, "Oslo.jpg")
    vacations = vacation_service.get_all_vacations()

    try:
        assert len(vacations) == 2

    finally:
        db_session.delete(country)
        db_session.delete(country2)
        db_session.commit()

# 3) delete vacation positive test - expected to pass

def test_delete_vacation_positive(db_session):
    vacation_service = VacationService(db_session)
    country_service = CountryService(db_session)
    country = country_service.create_country("France")
    country_id = country.id

    try:
        vacation = vacation_service.create_vacation(country_id, "France Trip", "2025-09-01", "2025-09-10", 1800.00, "france.jpg")
        deleted = vacation_service.delete_vacation(vacation.id)
        assert deleted is True
        assert vacation_service.get_vacation_by_id(vacation.id) is None

    finally:
        db_session.delete(country)
        db_session.commit()

# 3) delete vacation negative test - expected to fail

def test_delete_vacation_negative(db_session):
    vacation_service = VacationService(db_session)
    country_service = CountryService(db_session)
    country = country_service.create_country("France")
    country_id = country.id

    try:
        vacation = vacation_service.create_vacation(country_id, "France Trip", "2025-09-01", "2025-09-10", 1800.00, "france.jpg")
        deleted = vacation_service.delete_vacation(999)
        assert deleted is True
        assert vacation_service.get_vacation_by_id(vacation.id) is None

    finally:
        db_session.delete(country)
        db_session.commit()

# 4) update vacation positive test - expected to pass

def test_update_vacation_positive(db_session):
    vacation_service = VacationService(db_session)
    country_service = CountryService(db_session)
    country = country_service.create_country("France")
    country_id = country.id
    vacation = vacation_service.create_vacation(country_id, "France Trip", "2025-09-01", "2025-09-10", 1800.00,"france.jpg")

    try:
        vacation = vacation_service.update_vacation(vacation.id, country_id, "France Trip", "2026-12-15", "2026-12-20", 9800.00,"france.jpg")
        assert vacation.price == 9800

    finally:
        db_session.delete(country)
        db_session.commit()

# 4) delete vacation negative test - expected to fail

def test_update_vacation_negative(db_session):
    vacation_service = VacationService(db_session)
    country_service = CountryService(db_session)
    country = country_service.create_country("France")
    country_id = country.id
    vacation = vacation_service.create_vacation(country_id, "France Trip", "2025-09-01", "2025-09-10", 1800.00,"france.jpg")

    try:
        vacation = vacation_service.update_vacation(vacation.id, country_id, "France Trip", "2026-12-15", "2026-12-20", -5000.00,"france.jpg")
        assert vacation is not None

    finally:
        db_session.delete(country)
        db_session.commit()