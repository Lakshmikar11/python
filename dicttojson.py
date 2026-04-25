import json

user = {"name": "Lakshmikar reddy", "age": 25}
json_data = json.dumps(user)
print(json_data)

data = json.loads(json_data)
print(data["name"])