form fastapi import APIRouter
from config.db import conn
from models.index import users

user = APIRouter()

@user.get('/')
    async def read_data():
        return conn.execute(users.select()).fetchall()