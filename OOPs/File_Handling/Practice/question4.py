import csv

data= ["karan", "agra",23,"python"]
data2 = [["name", "age"], ["Karan", 22]]

with open("data.csv", "w", newline="") as f:
    writer= csv.writer(f)
    writer.writerow(data)

with open("data2.csv", "w", newline="") as f:
    writer= csv.writer(f)
    writer.writerows(data2)

with open("data2.csv", "r", newline="") as f:
    reader= csv.reader(f)
    for row in reader:
        print(row)