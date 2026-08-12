from fastapi import FastAPI
from app.database.database import Base, engine
from app.models.user import User
from app.schemas.user import UserCreate
from app.routers.users import router as users_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users_router)


@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


@app.post("/users")
def create_user(user: UserCreate):
    return user
