from fastapi import Body, FastAPI
import json
import numpy as np
import datetime

from Lab2.TransactionService.CheckUserToAuth import check_valid_token
from Lab2.TransactionService.GrpServices.CreateTransaction.RequestCreateTransaction import RequestCreateTransaction

app = FastAPI()

BASE_URL = "/trn"
path_tran = "Lab2/TransactionService/Transaction.json"
re_date_pattern = r"(0?[1-9]|[12]\d|3[01])/(0?[1-9]|1[012])/([12]\d{3}) ([01]\d|2[1-3]):([0-5]\d):([0-5]\d)"
date_pattern = "%d/%m/%Y %H:%M:%S"

Report_CreateTrancation_Port = 50004

@app.post(BASE_URL+"/{method}")
def add(id_user:int, method:str, balance:int, token: str = Body()):

    assert method in ["add", "buy"], {"Message": "Метод не поддерживается"}

    if not check_valid_token(token):
        return {"Message": "Пользователь не авторизован"}
    
    file_with_trn = open(path_tran)
    transactions = json.load(file_with_trn)
    file_with_trn.close()
    
    while True:
        id_trn = np.random.randint(0, 1024)
        if id_trn not in transactions:
            break
    
    date = datetime.datetime.now().strftime(date_pattern)
    transaction = {"date": date, "user": id_user, "method": method, "balance": balance}

    response = RequestCreateTransaction(method=method,
                                        id_user=id_user,
                                        balance=balance,
                                        port=Report_CreateTrancation_Port)
    if response.status:
        status = 200
        transactions[id_trn] = transaction
    else:
        status = 404

    file_with_trn = open(path_tran, "w")
    json.dump(transactions, file_with_trn, indent=4)
    file_with_trn.close()

    return {"status": status, "message": response.report}
