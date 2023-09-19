from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, ForeignKey, Column, Integer, String, Date, NUMERIC, LargeBinary
from sqlalchemy.orm import relationship, mapped_column
from fastapi_users.db import SQLAlchemyBaseUserTable


metadata = MetaData()

Base = declarative_base(metadata=metadata)


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False)
    date_of_birth = Column(Date)
    profile_image = Column(LargeBinary)
    bank_card = relationship("BankCard", back_populates="user")


class BankCard(Base):
    __tablename__ = "bankcard"

    id = Column(Integer, primary_key=True, autoincrement=True)
    card_number = Column(Integer, nullable=False)
    expiration_date = Column(Date)
    cvv = Column(NUMERIC(3))
    balance = Column(Integer)
    user_id = mapped_column(ForeignKey("user.id"))
    user = relationship("User", back_populates="bank_card")
