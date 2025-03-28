import json
import re
import datetime
import numpy as np

# user = {"login": "login","password": "password", "info": "info"}
        
# file = open("Users.json", "+a")
# users = json.load(file)
# file.close()

# users["3"] = json.dumps(user)

# file = open("Users.json", "w")
# json.dump(user, file, indent=4)
# file.close()

# date_pattern = r"(0?[1-9]|[12]\d|3[01])/(0?\d|1[012])/([12]\d{3}) ([01]\d|2[1-3]):([0-5]\d)"
# date_pattern = "%d-%m-%Y %H:%M:%S"

# begin = datetime.datetime.strptime("03-05-2025 16:00:00", date_pattern)
# end = datetime.datetime.strptime("03-05-2025 20:00:00", date_pattern)
# date = datetime.datetime.strptime("03-05-2025 17:00:00", date_pattern)
# print(begin < date < end)


# file = open("Idx_Transaction.txt").read().split(" ")
# print(file)
# idx_trn = list(map(lambda data: int(data), open("Idx_Transaction.txt").read().split(' ')))
# print(idx_trn)

print(np.random.randint(0, 1024))