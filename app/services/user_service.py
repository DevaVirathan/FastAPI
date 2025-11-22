from sqlalchemy.orm import Session
from app.repository.user_repo import UserRepository
from app.schemas.user_schema import UserCreate, UserUpdate


class UserService:
    @staticmethod
    def list_users(db: Session):
        return UserRepository.get_all(db)
    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        return UserRepository.get_by_id(db, user_id)

    @staticmethod
    def create_user(db: Session, data: UserCreate):
        return UserRepository.update(db, data)
    
    @staticmethod
    def update_user(db: Session, user_id: int, data: UserUpdate):
        return UserRepository.update(db, user_id, data)


    @staticmethod
    def delete_user(db: Session, user_id: int):
        return UserRepository.delete(db, user_id)