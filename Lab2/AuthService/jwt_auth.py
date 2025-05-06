import jwt
import json

key = open("Lab2/AuthService/secret.txt").read()
path_to_users = "Lab2/AuthService/Users.json"

def create_token(payload: dict) -> str:
    token = jwt.encode(payload=payload, 
                       key=key,
                       algorithm="HS256")
    return token


def check_access_token(token:str) -> bool:
    try:
        jwt.decode(jwt=token, key=key, leeway=900, audience='user', algorithms='HS256', verify=True)
        return True
    except jwt.InvalidTokenError:
        # В случае невалидности возвращаем сообщение
        return False


def check_refresh_token(token:str) -> bool:
    file = open(path_to_users)
    users = json.load(file)
    file.close()
    try:
        claims = jwt.decode(jwt=token, key=key, leeway=8000000, audience='user', algorithms='HS256', verify=True)
        if users[claims["id"]]["token"] == token:
            return True
        else:
            return False
    except jwt.InvalidTokenError:
        # В случае невалидности возвращаем сообщение
        return False
