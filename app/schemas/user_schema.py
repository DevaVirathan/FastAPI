from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str


class UserResponse(UserCreate):
    id: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

class Config:
    orm_mode = True