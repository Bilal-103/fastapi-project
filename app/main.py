from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Bilal"}, {"id": 2, "name": "Ali"}]
