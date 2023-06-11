from settings import JWT_SECRET
import jwt
import datetime
import base64


# logging

def create_token(username, auth):
    return jwt.encode(
        {
            'username': username,
            'exp': datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'admin': auth
        },
        JWT_SECRET,
        algorithm='HS256'
    )


def encode_password(password):
    password = base64.b64decode(password.encode()).decode()
    return password


def decode_password(password):
    password = base64.b64encode(password.encode()).decode()
    return password


def validate_token(token):
    encoded_jwt = token.split(" ")[1]
    try:
        decoded = jwt.decode(
            encoded_jwt, JWT_SECRET, algorithms=["HS256"]
        )
    except Exception as ex:
        return False, ex
    return True, decoded
