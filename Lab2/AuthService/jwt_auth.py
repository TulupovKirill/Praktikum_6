import jwt

key = open("Lab2/AuthService/secret.txt").read()
path_to_user = "Lab2/ReportService/UserInfo.json"

def create_token_for_auth_user(payload):
    token = jwt.encode(payload=payload, 
                       key=key,
                       algorithm="HS256")
    return token
