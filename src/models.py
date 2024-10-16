from sqlmodel import Field, SQLModel, Relationship


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    phone_number: str | None = None
    profile_url: str
    houses: list["House"] | None = Relationship(back_populates="user")


class House(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    address: str
    price: int
    area: float | None = None
    series: float | None = None
    user_id: int | None = Field(default=None, foreign_key="user.id")
    user: User | None = Relationship(back_populates="houses")
