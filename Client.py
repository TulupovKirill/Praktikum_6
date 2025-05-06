import requests

response = requests.post("http://localhost:8080/user/auth", json={"login": "dasha", "password": "cool_password"})

data = response.json()

print(data)

id_user = int(data["id"])
access_token = data["access_token"]
refresh_token = data["refresh_token"]
response.close()

print(f"access_token: {access_token}, type: {type(access_token)}")
print(f"refresh_token: {refresh_token}, type: {type(refresh_token)}")
print(f"id: {id_user}")

response = requests.post("http://localhost:8080/user/refresh", json={"id" : id_user, 
                                                                     "access_token" : access_token, 
                                                                     "refresh_token" : refresh_token})

print(response)

# new_access_token = response.json()["access_token"]
# new_refresh_token = response.json()["refresh_token"]

# print(f"new_access_token: {new_access_token}")
# print(f"new_refresh_token: {new_refresh_token}")


# begin, end = "20/02/2025 00:00:00", "20/04/2025 00:00:00"
# response = requests.post(f"http://localhost:8081/report/history{id_user}", 
#                          json={"begin": begin,
#                                "end": end,
#                                "token": token})

# print(f"status: {response.json()["status"]}")
response.close()
