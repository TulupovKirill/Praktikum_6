import requests
import re

response = requests.post("http://localhost:8080/user/auth", json={"login": "dasha", "password": "cool_password"})
id_user, token = int(response.json()["id"]), response.json()["token"]
response.close()

print(f"token: {token}")
print(f"id: {id_user}")

begin, end = "20/02/2025 00:00:00", "20/04/2025 00:00:00"
response = requests.post(f"http://localhost:8081/report/history{id_user}", 
                         json={"begin": begin,
                               "end": end,
                               "token": token})

print(f"status: {response.json()["status"]}")
response.close()
