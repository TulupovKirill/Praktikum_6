import jwt

key = open("Lab2/AuthService/secret.txt").read()

def check_valid_token(token):
    try:
        # Проверяем валидность токена
        jwt.decode(jwt=token, key=key, leeway=900, audience='user', algorithms='HS256')
    except jwt.InvalidTokenError:
        # В случае невалидности возвращаем сообщение
        return False
    
    return True
