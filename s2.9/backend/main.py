import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Hello World {os.getenv('MY_BACKEND_NAME')}"}