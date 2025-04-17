from fastapi import Body, FastAPI
import json
import datetime

from Lab2.ReportService.CheckUserToAuth import check_user

app = FastAPI()

BASE_URL = "/report"
path_tran = "Lab2/TransactionService/Transaction.json" # принимать данные в msg от trnservice
path_to_users = "Lab2/ReportService/UsersInfo.json"
re_date_pattern = r"(0?[1-9]|[12]\d|3[01])/(0?[1-9]|1[012])/([12]\d{3}) ([01]\d|2[1-3]):([0-5]\d):([0-5]\d)"
date_pattern = "%d/%m/%Y %H:%M:%S"


@app.get(BASE_URL+"{id}")
def get_user(id:str):
    file = open(path_to_users)
    users = json.load(file)
    file.close()
    return users[id]


@app.post(BASE_URL+"/history/{id}")
def get_history_for_user(id:int,
                        begin: str = Body(pattern=re_date_pattern), 
                        end: str = Body(pattern=re_date_pattern)):
    
    if not check_user(id):
        return {"Message": "Не авторизированный пользователь"}

    begin_date = datetime.datetime.strptime(begin, date_pattern)
    end_date = datetime.datetime.strptime(end, date_pattern)

    # принимать информацию о нужном пользователе
    file_with_trn = open(path_tran)
    transaction = json.load(file_with_trn)
    file_with_trn.close()

    user_report = {"add": 0, "buy": 0, "history": []}

    for id_trn in transaction:

        str_date = transaction[id_trn]["date"]
        date = datetime.datetime.strptime(str_date, date_pattern)
        balance = transaction[id_trn]["balance"]
        method = transaction[id_trn]["method"]
        user_id = transaction[id_trn]["user"]

        if begin_date < date < end_date and id == user_id:
            user_report[method] += balance
            user_report["history"].append({"date": str_date, "method": method, "balance": balance})
    
    file_user_report = open(f"Lab2/ReportService/Reports/UserReport_{id}.json", "w")
    json.dump(user_report, file_user_report, indent=4)
    file_user_report.close()

    return {"status": 200}
