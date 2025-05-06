from fastapi import Body, FastAPI, Response
import json
import numpy as np
from datetime import datetime, timezone

from Lab2.AuthService.GrpServices.RequestAboutNewUser.RequestAboutNewUser import RequestToAddNewUser
from Lab2.AuthService.jwt_auth import (check_access_token,
                                       check_refresh_token,
                                       create_token)

app = FastAPI()

BASE_URL = "/user"
path_to_users = "Lab2/AuthService/Users.json" 

Transaction_AddAuthUserService_Port = 50002
Report_AddAuthUserService_Port = 50001
Report_CreateNewUser_Port = 50003


@app.post(BASE_URL+'/refresh')
def refresh(id: int = Body(),
            access_token: str = Body(),
            refresh_token: str = Body()):
    
    file = open(path_to_users)
    users = json.load(file)
    file.close()

    # return Response(status_code=200)

    user_refresh_token = users[str(id)]["token"]

    if check_access_token(access_token) and check_refresh_token(user_refresh_token):
        access_token = create_token(payload={'id': id, "exp": datetime.now(tz=timezone.utc), "aud": "user"})
        refresh_token = create_token(payload={"id": id})

        file = open(path_to_users, "w")
        users[str(id)]['token'] = refresh_token
        json.dump(users, file, indent=4)
        file.close()

        return {"access_token": access_token, "refresh_token": refresh_token}
    else:
        return Response("Необходима повторная авторизация", status_code=401)

@app.post(BASE_URL+"/auth")
def authorization(login:str = Body(),
                    password:str = Body()):
    
    file = open(path_to_users)
    users = json.load(file)
    file.close()

    for id in users:
        user_login = users[id]["login"]
        user_password = users[id]["password"]

        """
            Если пользователь авторизован, то другие сервисы получают об этом информацию
            Теперь этот пользователь может обращаться в другие сервисы
            Цикл while - это упрощенный способ создать согласованность. 
            Пока от сервисов не будет получен ответ об успешной обработки, сообщение будет повторно отправляться
        """
        if user_login == login and user_password == password:
            
            access_token = create_token(payload={'id': id, "exp": datetime.now(tz=timezone.utc), "aud": "user"})
            refresh_token = create_token(payload={"id": id, "exp": datetime.now(tz=timezone.utc), "aud": "user"})

            file = open(path_to_users, "w")
            users[str(id)]['token'] = refresh_token
            json.dump(users, file, indent=4)
            file.close()

            return {"id": id, "access_token": access_token, "refresh_token": refresh_token}
        
    return {"Message": "Неверный логин или пароль"}


@app.post(BASE_URL+"/create")
def create_user(login:str = Body(),
                password:str = Body(),
                name_user:str = Body()):
    
    file = open(path_to_users, 'r')
    users = json.load(file)
    file.close()
    
    # массив всех id пользователей
    idx = []
    for id in users:
        if users[id]["login"] == login or users[id]["password"] == password:
            return {"Message": "Логин или пароль уже занят"}
        idx.append(int(id))

    # генерация нового id
    while True:
        id_user = np.random.randint(0, 1024)
        if id_user not in idx:
            break
    
    user = {"login": login,"password": password, "token": ''}
    
    users[id_user] = user
    file = open(path_to_users, "w")
    json.dump(users, file, indent=4)
    file.close()

    while True: 
        response = RequestToAddNewUser(id_user, name_user, Report_CreateNewUser_Port)
        if response.status:
            break

    return {"status": 200}
