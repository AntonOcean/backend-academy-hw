from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Item(BaseModel):
    message: str


app = FastAPI()

origins = [
    "http://localhost:63343",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["my-api-group"])
async def main():
    return Item(message=11)


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}