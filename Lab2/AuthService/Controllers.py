from fastapi import Body, FastAPI
import json
import numpy as np

from Lab2.AuthService.GrpServices.AuthToAllService.RequestToAddAuthUserService import RequestToAuthUserInAnotherService

app = FastAPI()

BASE_URL = "/user"
path_to_users = "AuthService/Users.json" 

Transaction_AddAuthUserService_Port = 50002
Report_AddAuthUserService_Port = 50001


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
    
    file = open(path_to_users)
    users = json.load(file)
    file.close()
    
    idx = []
    for id in users:
        idx.append(id)

    while True:
        id = np.random.randint(0, 1024)
        if id not in idx:
            break
    
    user = {"login": login,"password": password}
    
    users[id] = user
    file = open(path_to_users, "w")
    json.dump(users, file, indent=4)
    file.close()

    # отправить сообщение в reportservice с новым пользователем
    balance = 0

    data = {
        "name": name_user,
        "balance": balance
    }



    return {"status": 200, "id": id}
