from fastapi import APIRouter
from app.core.database import Base, engine


router = APIRouter(prefix="/migrate", tags=["Migrations"])


@router.post("/")
def run_migrations():
    Base.metadata.create_all(bind=engine)
    return {"status": "migrations applied"}