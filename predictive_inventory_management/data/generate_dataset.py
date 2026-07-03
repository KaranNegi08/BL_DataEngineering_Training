from faker import Faker
import pandas as pd
import numpy as np
import random

fake = Faker()

np.random.seed(42)

warehouses = [
    'WH-A',
    'WH-B',
    'WH-C',
    'WH-D',
    'WH-E',
]

products = [
    "Laptop",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Printer",
    "Tablet",
    "Mobile",
    "CPU",
    "Camera",
    "Speaker"
]

suppliers = [
    "Supplier-X",
    "Supplier-Y",
    "Supplier-Z",
    "Supplier-A",
    "Supplier-B"
]

rows=[]

for _ in range(1000):
    warehouse = random.choice(warehouses)
    product = random.choice(products)
    supplier = random.choice(suppliers)
    stock = random.randint(0,500)
    reorder= random.randint(10,200)

    transport_cost =500

    warehouse_cost= {
        "WH-A": 100,
        "WH-B": 200,
        "WH-C": 150,
        "WH-D": 250,
        "WH-E": 175
    }

    product_cost = {
        "Laptop": 500,
        "Keyboard": 80,
        "Mouse": 60,
        "Monitor": 250,
        "Printer": 300,
        "Tablet": 350,
        "Mobile": 400,
        "CPU": 280,
        "Camera": 450,
        "Speaker": 120
    }

    supplier_cost = {
        "Supplier-X": 100,
        "Supplier-Y": 130,
        "Supplier-Z": 160,
        "Supplier-A": 90,
        "Supplier-B": 140
    }

    transport_cost += warehouse_cost[warehouse]
    transport_cost += product_cost[product]
    transport_cost += supplier_cost[supplier]

    transport_cost += stock * 1.8

    transport_cost += np.random.normal(0, 50)

    transport_cost = round(transport_cost, 2)

    last_updated = fake.date_between(
        start_date="-2y",
        end_date="today"
    )

    rows.append({

        "Warehouse": warehouse,

        "Product": product,

        "Supplier": supplier,

        "Stock_Level": stock,

        "Reorder_Level": reorder,

        "Transport_Cost": transport_cost,

        "Last_Updated": last_updated

    })

df = pd.DataFrame(rows)

#Introducing Missing values
missing_index = np.random.choice(df.index, size=200, replace=False)

df.loc[missing_index,"Stock_Level"] = np.nan


df.to_csv("./data/inventory_dataset.csv", index= False)

print("Dataset Shape", df.shape)
print("Dataset generated successfully...")