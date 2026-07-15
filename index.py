from fastapi import FastAPI
from routes.index import user

app = FastAPI()

app.include_router(user)

# Below code comment using route from routes folder and above include
# @app.get("/")
# def read_something():
#     return {"msg":"Hello World"}
