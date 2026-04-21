data = [
    {"name": "A", "age": 20},
    {"name": "B", "age": 25},
    {"name": "C", "age": 29}

]

user= [user for user in data if user["age"] > 22]
print(user)