from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import traceback
from config.db import engine, meta
from routes.index import user_router

app = FastAPI()

meta.create_all(engine)


# 1. The Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # Print the full error traceback to your terminal console
    print("--- DETAILED ERROR TRACEBACK ---")
    traceback.print_exc()
    print("--------------------------------")

    # Return the exact error message back to the client/browser
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "details": str(exc),
            "type": type(exc).__name__,
        },
    )


# 2. Include your existing router
app.include_router(user_router)

# Below code comment using route from routes folder and above include
# @app.get("/")
# def read_something():
#     return {"msg":"Hello World"}
