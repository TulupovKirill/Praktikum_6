from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import jwt

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        token = (await request.json())['token']
        if self.check_valid_token(token):
            return await call_next(request)
        else:
            return Response(status_code=403)
    
    def check_valid_token(self, token):
        key=open("Lab2/AuthService/secret.txt").read()
        try:
            # Проверяем валидность токена
            jwt.decode(jwt=token, key=key, leeway=900, audience='user', algorithms='HS256')
        except jwt.InvalidTokenError:
            # В случае невалидности возвращаем сообщение
            return False
        
        return True