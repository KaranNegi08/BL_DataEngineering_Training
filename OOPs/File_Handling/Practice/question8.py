import csv

data = [
    {"name": "Karan", "age": 22},
    {"name": "Aman", "age": 23}
]

with open("data5.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)