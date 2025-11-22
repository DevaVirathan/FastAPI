from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserUpdate


class UserRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(User).all()


    @staticmethod
    def get_by_id(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def create(db: Session, data: UserCreate):
        new_user = User(**data.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def update(db: Session, user_id: int, data: UserUpdate):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return None

        update_data = data.dict(exclude_unset=True)  
        for key, value in update_data.items():
            setattr(user, key, value)

        try:
            db.commit()
            db.refresh(user)
        except Exception:
            db.rollback()
            raise

        return user

    @staticmethod
    def delete(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return user