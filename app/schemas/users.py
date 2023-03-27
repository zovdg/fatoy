from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class ShowUser(BaseModel):
    # id: int
    username: str
    email: EmailStr
    is_active: bool
    # hashed_password: str
    # is_superuser: bool

    class Config:
        orm_mode = True
