from src.services.like_service import LikeService
from src.services.vacation_service import VacationService
from src.services.user_service import UserService

def test_like_and_unlike_vacation(db_session):
    user_service = UserService(db_session)
    vacation_service = VacationService(db_session)
    like_service = LikeService(db_session)

    user = user_service.create_user("Nasrin", "Kadri", "nasrinKadri@gmai.com", "1234", 2)
    vacation = vacation_service.create_vacation(1, "Japan Trip", "2025-07-01", "2025-07-10", 1700.00, "japan.jpg")
     
    commit = db_session.commit() 
    
    like = like_service.add_like(user.id, vacation.id)
    assert like is not None

    removed = like_service.remove_like(user.id, vacation.id)
    assert removed is True
