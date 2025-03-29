from fastapi import Body, FastAPI
import json
import numpy as np
from Lab2.AuthService.GrpServices.RequestToAddAuthUserService import RequestToAuthUserInAnotherService

app = FastAPI()

BASE_URL = "/user"
path_to_users = "Users.json"

Transaction_AddAuthUserService_Port = 50002
Report_AddAuthUserService_Port = 50001

@app.get(BASE_URL+"{id}")
def get_user(id:str):
    file = open(path_to_users)
    users = json.load(file)
    file.close()
    return users[id]["info"]


@app.post(BASE_URL+"/auth")
def authorization(login:str = Body(),
                    password:str = Body()):
    
    file = open(path_to_users)
    users = json.load(file)
    file.close()

    for id in users:
        user_login = users[id]["login"]
        user_password = users[id]["password"]

        if user_login == login and user_password == password:
            RequestToAuthUserInAnotherService(int(id), Transaction_AddAuthUserService_Port)
            RequestToAuthUserInAnotherService(int(id), Report_AddAuthUserService_Port)
            return {"status": 200, "id": id}
        
    return {"Message": "Неверный логин или пароль"}


@app.post(BASE_URL+"/create")
def create_user(login:str = Body(),
                    password:str = Body(), info:dict = Body()):
    
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
    
    info["balance"] = 0
    user = {"login": login,"password": password, "info": info}
    
    users[id] = user
    file = open(path_to_users, "w")
    json.dump(users, file)
    file.close()

    return {"status": 200, "id": id}
