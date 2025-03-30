from fastapi import Body, FastAPI
import json
import numpy as np
import datetime

from Lab2.TransactionService.CheckUserToAuth import check_user
from Lab2.TransactionService.GrpServices.CreateTransaction.RequestCreateTransaction import RequestCreateTransaction

app = FastAPI()

BASE_URL = "/trn"
path_tran = "TransactionService/Transaction.json"
path_idx_trn = "TransactionService/Idx_Transaction.txt"
re_date_pattern = r"(0?[1-9]|[12]\d|3[01])/(0?[1-9]|1[012])/([12]\d{3}) ([01]\d|2[1-3]):([0-5]\d):([0-5]\d)"
date_pattern = "%d/%m/%Y %H:%M:%S"

Report_CreateTrancation_Port = 50004


@app.post(BASE_URL+"/history")
def get_history_for_user(
                        begin: str = Body(pattern=re_date_pattern), 
                        end: str = Body(pattern=re_date_pattern)):
    
    if not check_user(id):
        return {"Message": "Не авторизированный пользователь"}
    
    result = []

    begin_date = datetime.datetime.strptime(begin, date_pattern)
    end_date = datetime.datetime.strptime(end, date_pattern)

    file_with_trn = open(path_tran)
    transaction = json.load(file_with_trn)
    file_with_trn.close()

    for id_trn in transaction:

        str_date = transaction[id_trn]["date"]
        date = datetime.datetime.strptime(str_date, date_pattern)

        if begin_date < date < end_date:
            result.append({id_trn:transaction[id_trn]})
    
    return result


@app.post(BASE_URL+"/{method}")
def add(id_user:int, method:str, balance:int = Body()):

    assert method in ["add", "buy"], {"Message": "Метод не поддерживается"}

    check_user(id_user)

    if not check_user:
        return {"Message": "Пользователь не найден"}
    
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
