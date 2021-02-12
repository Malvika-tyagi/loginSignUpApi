from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from encoding_hashed_password import *

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
    # Check if user already exists or not
    password_validation = validate(item.password)
    if password_validation is False:
        return "Password is Not Validated. It Should include a special character, number and legth should be 8 " \
               "characters"
    password_encryption = encrypt_message(item.password)
    return_data = user_exists(collection, item.username)
    if return_data:
        return "User Already Exists. Kindly check your EmailId Again."
    sign_up_user = {"user_name": item.username.lower(), "Email": item.email.lower(), "Password": password_encryption}
    collection.insert_one(sign_up_user)
    return "Sign Up Successfully"


@app.post("/items/login/")
async def login(login: Login):
    client = MongoClient('localhost', 27017)
    db = client.login_db
    username_get = login.username
    password_get = login.password
    data = db.login_signup.find()
    for i in data:
        decrypted = decrypt_pass(i["Password"])
        if i["user_name"] == username_get and decrypted == password_get:
            return "logged in Successfully"
    return "Kindly Sign Up. User Not Exists"


def user_exists(collection, username):
    data = collection.find()
    for i in data:
        if i["user_name"] == username.lower():
            return True
    return False

