from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User, UserUpdate

user_router = APIRouter()

@user_router.get("/")
def read_data():  # Removed 'async'
    result = conn.execute(users.select()).fetchall()
    return [row._mapping for row in result]


@user_router.get("/{id}")
def read_data_by_id(
    id: int,
):  # Renamed function slightly so it doesn't duplicate the name above
    result = conn.execute(users.select().where(users.c.id == id)).fetchall()
    return [row._mapping for row in result]


@user_router.post("/")
def write_data(user: User):  # Removed 'async'
    conn.execute(
        users.insert().values(name=user.name, email=user.email, password=user.password)
    )
    conn.commit()
    result = conn.execute(users.select()).fetchall()
    return [row._mapping for row in result]


@user_router.put("/{id}")
def update_data(id: int, user: UserUpdate):  # Removed 'async'
    update_values = user.model_dump(exclude_unset=True)
    if update_values:
        conn.execute(users.update().values(**update_values).where(users.c.id == id))
        conn.commit()
    result = conn.execute(users.select()).fetchall()
    return [row._mapping for row in result]


@user_router.delete("/{id}")
def delete_data(id: int):  # Removed 'async'
    conn.execute(users.delete().where(users.c.id == id))
    conn.commit()
    result = conn.execute(users.select()).fetchall()
    return [row._mapping for row in result]


#  Old Code not working

# @user.get("/")
# async def read_data():
#     return conn.execute(users.select()).fetchall()


# @user.get("/{id}")
# async def read_data(id: int):
#     return conn.execute(users.select().where(users.c.id == id)).fetchall()


# @user.post("/")
# async def write_data(user: User):
#     conn.execute(
#         users.insert().values(name=user.name, email=user.email, password=user.password)
#     )
#     return conn.execute(users.select()).fetchall()


# @user.put("/{id}")
# async def update_data(id: int, user: User):
#     conn.execute(
#         users.update(name=user.name, email=user.email, password=user.password).where(
#             users.c.id == id
#         )
#     )
#     return conn.execute(users.select()).fetchall()


# @user.delete("/{id}")
# async def delete_data(id: int):
#     conn.execute(users.delete().where(users.c.id == id))
#     return conn.execute(users.select()).fetchall()
