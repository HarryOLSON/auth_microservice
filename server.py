from utils import create_token, decode_password, encode_password, validate_token
from db.auth_manager import DBManager
from fastapi import FastAPI, Request
from settings import DBCreds


server = FastAPI()
db_manager = DBManager(DBCreds)


@server.get("/")
async def root():
    return {"message": "Hello World"}


@server.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@server.post('/log-in/')
def log_in(request: Request):
    auth_header = request.authorization
    if not request.authorization:
        return 'No user data is provided', 401
    username = request.authorization.username
    user_check = db_manager.check_user_exist(username)
    if user_check:
        user = user_check.fetchone()
        email = user[0]
        password = user[1]
        password = decode_password(password)
        if auth_header.user == email and auth_header.password == password:
            return {
                'token': create_token(auth_header.username, False)
            }
    return 'invalid user data is provided', 401


@server.post('/validate/')
def validate(request: Request):
    encoded_jwt = request.headers["Authorization"]

    if not encoded_jwt:
        return "missing credentials", 401

    decoded = validate_token(encoded_jwt)
    if not decoded:
        return 'error while validating', 401
    return decoded, 200


@server.post('/sign-up/')
def sign_up(request: Request):
    if not request.authorization:
        return 'No user data is provided', 401

    username = request.authorization.username
    email = request.authorization.email
    first_name = request.authorization.first_name
    last_name = request.authorization.last_name
    password = request.authorization.password
    password = encode_password(password)

    user_check = db_manager.check_user_exist(username)
    if not user_check:
        user_creation = db_manager.create_user({
            'user_name': username,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'password': password
        })
        if user_creation:
            return {
                'token': create_token(username, False)
            }
        return 'Error creating user', 404
    return "User with these credentials already exists"


