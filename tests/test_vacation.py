# from src.services.vacation_service import VacationService
#
# def test_create_vacation(db_session):
#     vacation_service = VacationService(db_session)
#     vacation = vacation_service.create_vacation(1, "Trip to Bali", "2025-06-01", "2025-06-10", 1500.00, "bali.jpg")
#
#     assert vacation is not None
#     assert vacation.description == "Trip to Bali"
#
# def test_get_all_vacations(db_session):
#     vacation_service = VacationService(db_session)
#     vacation_service.create_vacation(1, "Hawaii Trip", "2025-08-01", "2025-08-15", 2000.00, "hawaii.jpg")
#     vacations = vacation_service.get_all_vacations()
#
#     assert len(vacations) == 1
#     assert vacations[0].description == "Hawaii Trip"
#
# def test_delete_vacation(db_session):
#     vacation_service = VacationService(db_session)
#     vacation = vacation_service.create_vacation(1, "France Trip", "2025-09-01", "2025-09-10", 1800.00, "france.jpg")
#     deleted = vacation_service.delete_vacation(vacation.id)
#
#     assert deleted is True
#     assert vacation_service.get_vacation_by_id(vacation.id) is None
