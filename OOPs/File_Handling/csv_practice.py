import csv
import json
# data = {
#     "user": {
#         "name": "Karan",
#         "age": 22,
#         "address": {
#             "city": "Agra",
#             "pincode": 282001
#         }
#     },
#     "location":{
#         "city": "Pune",
#         "pincode": 411001
#     }
# }

data = [
    {"name": "Karan", "address": json.dumps({"city": "Agra"})}
]


with open("data3.csv", "w", newline="") as f:
    fieldnames = ["name", "address"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(data)

with open("data3.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["address"])
        print(type(json.loads(row["address"])))


# with open("data3.csv", "w", newline="") as f:
#     writer=csv.writer(f)
#     writer.writerows(data)

# def write_csv(file_name, data):
#     with open(file_name, "w", newline="") as file:
#         writer = csv.DictWriter(file, fieldnames=data[0].keys())
#         writer.writeheader()
#         writer.writerows(data)

# write_csv("data.csv",data)
# def read_csv():
#     with open("data.csv") as f:
#         return list(csv.reader(f))

# print(read_csv())


# with open("data.csv", "w", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["user","location"])
#     writer.writeheader()
#     writer.writerow(data)


# with open("data.csv", "r", newline="") as f:
#     reader= csv.DictReader(f)
#     for row in reader:
#         print(row["location"])


