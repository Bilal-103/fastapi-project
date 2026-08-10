from fastapi import FastAPI
from app.schemas.user import UserCreate

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Bilal"}, {"id": 2, "name": "Ali"}]


@app.post("/users")
def create_user(user: UserCreate):
    return user
