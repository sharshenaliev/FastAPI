from fastapi import FastAPI
from sqladmin import Admin
from src.db import engine
from src.routers import router
from src.admin import UserAdmin, HouseAdmin

app = FastAPI()


app.include_router(router, prefix="/api/v1",)
admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(HouseAdmin)
