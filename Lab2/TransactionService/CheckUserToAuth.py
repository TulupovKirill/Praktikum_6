path_to_auth_user = "TransactionService/auth_user.txt"

def check_user(id):
    auth_users = list(map(lambda data: int(data), open(path_to_auth_user).read().split(' ')[:-1]))
    return id in auth_users
