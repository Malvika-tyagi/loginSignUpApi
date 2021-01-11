# loginSignUpApi
There are Two Post Method APi for the login and SIgn Up. 
# Sign Up API
To Run the Sign Up Api you have to Write ```uvicorn file_name:app --reload```
Open Postman and pase this URL for the Post Method ```http://127.0.0.1:8000/items/```
Api will Accept the Json in the format ``` {
    "username": "Foo",
    "email": "An optional description",
    "password": "password"
}```
# Login APi
To Run the Sign Up Api you have to Write ```uvicorn file_name:app --reload```
Open Postman and pase this URL for the Post Method ```http://127.0.0.1:8000/items/login/```
Api Will Accept the Json Input in this format ```{"username": "Foo",
    "password": "password"}```
