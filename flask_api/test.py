import requests
import json

BASE = "http://127.0.0.1:5000"

data = [{"user_id": 101, "username":"John", "email":"john@gmail.com", "password":"hello123", "contact":"9864057241"},
        {"user_id": 102, "username":"Peter", "email":"peter@gmail.com", "password":"coolpeter22", "contact":"8761072543"},
        {"user_id": 103, "username":"Kamal", "email":"kamal@hotmail.com", "password":"kamlaml", "contact":"9965733241"}]

headers = {'Content-Type': 'application/json'}

response = requests.delete(BASE + "/user")
print(response.json())


'''
for i in range(len(data)):
    json_data = json.dumps(data[i])
    response = requests.post(BASE + "/user", data=json_data, headers=headers)
    print(response.json())

#DELETE ALL
#DELETE SINGLE
input()
response = requests.delete(BASE + "/user")
print(response.json())
'''