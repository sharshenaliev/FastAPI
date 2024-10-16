from sqladmin import ModelView
from src.models import User, House


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name]
    column_searchable_list = [User.name]


class HouseAdmin(ModelView, model=House):
    column_list = [House.id, House.price]
