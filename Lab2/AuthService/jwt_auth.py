import jwt
import json

key = "secret"
path_to_user = "Lab2/ReportService/UserInfo.json"

def create_token_for_auth_user(payload):
    token = jwt.encode(payload=payload, key=key, algorithm="HS256")
    return token

def check_valid_token(token, users: json):
    try:
        # Проверяем валидность токена
        payload = jwt.decode(jwt=token, key=key, algorithms='HS256')
    except jwt.InvalidTokenError:
        # В случае невалидности возвращаем ошибку
        return {"status": 403}

    try:
        user = users[payload["id"]]
    except:
        return {"status": 404}
    
    return {"status": 200}

# token = create_token_for_auth_user({"id": 1})
# users = {1: {"name": "kirill"}}
# message = check_valid_token(token, users)
# print(message)