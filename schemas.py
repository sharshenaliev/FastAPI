import datetime
from typing import Optional
from pydantic import BaseModel
from fastapi_users import schemas


class UserRead(schemas.BaseUser):
    first_name: str
    last_name: str
    phone_number: int
    date_of_birth: datetime.date


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    phone_number: int
    date_of_birth: datetime.date


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str
    last_name: str
    phone_number: int
    date_of_birth: datetime.date
    profile_image: Optional[str]


class BankCardSchema(BaseModel):
    id: int
    card_number: int
    expiration_date: datetime.date
    cvv: int
    balance: int
    bank_card: int
