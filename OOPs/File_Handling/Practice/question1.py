import json

data = '{"name": "Karan", "age": 22, "city": "Agra"}'

parsed = json.loads(data)  #string to dict
print(parsed["age"])