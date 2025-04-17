from fastapi import Body, FastAPI
import json
import numpy as np

from Lab2.AuthService.GrpServices.AuthToAllService.RequestToAddAuthUserService import RequestToAuthUserInAnotherService
from Lab2.AuthService.GrpServices.RequestAboutNewUser.RequestAboutNewUser import RequestToAddNewUser

app = FastAPI()

BASE_URL = "/user"
path_to_users = "Lab2/AuthService/Users.json" 

Transaction_AddAuthUserService_Port = 50002
Report_AddAuthUserService_Port = 50001
Report_CreateNewUser_Port = 50003

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
            while True:
                response1 = RequestToAuthUserInAnotherService(int(id), Transaction_AddAuthUserService_Port)
                response2 = RequestToAuthUserInAnotherService(int(id), Report_AddAuthUserService_Port)
                if response1 and response2:
                    break
            return {"status": 200, "id": id}
        
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
    
    user = {"login": login,"password": password}
    
    users[id_user] = user
    file = open(path_to_users, "w")
    json.dump(users, file, indent=4)
    file.close()

    while True: 
        response = RequestToAddNewUser(id_user, name_user, Report_CreateNewUser_Port)
        if response.status:
            break

    return {"status": 200, "id": id_user}
