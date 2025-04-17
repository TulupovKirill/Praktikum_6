

path_to_users = "AuthService/Users.json" 

file = open(path_to_users, 'r')
users = json.load(file)
file.close()