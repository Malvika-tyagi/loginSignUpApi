from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

class Item(BaseModel):
    username: str
    email: str
    password: str


class Login(BaseModel):
    username: str
    password: str

app = FastAPI(debug=True)

@app.post("/items/")
async def sign_up(item: Item):
    client = MongoClient('localhost', 27017)
    db = client.login_db
    collection = db.login_signup
    sign_up_user = {"user_name": item.username.lower(), "Email": item.email.lower(), "Password": item.password.lower()}
    result = collection.insert_one(sign_up_user)
    return result.inserted_id


@app.post("/items/login/")
async def login(login: Login):
    client = MongoClient('localhost', 27017)
    db = client.login_db
    username_get = login.username
    password_get = login.password
    data = db.login_signup.find()
    for i in data:
        if i["user_name"] == username_get and i["Password"] == password_get:
            return "logged in Successfully"
    return "Kindly Sign Up. User Not Exits"