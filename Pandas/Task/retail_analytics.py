import numpy as np
import pandas as pd

np.random.seed(1)

sales = np.random.randint(-30,500,(30,5))
# print(sales)

# Replace negative values with 0
sales[sales < 0] = 0
# print(sales)

# Compute the average weekly sales per product (assume 7 days = 1 week)

data = sales[:28]

weekly_sales = data.reshape(4,7,5)

weekly_total = weekly_sales.sum(axis=1)

avg_weekly_sales = weekly_total.mean(axis=0)
# print(avg_weekly_sales)

# Identify the product with the highest average weekly sales
highest_weekly_sale= max(avg_weekly_sales)
# print(highest_weekly_sale)



# Pandas (Intermediate)
#  You are given a DataFrame containing order_id, customer_id, order_date, and order_amount.

# Convert order_date to datetime
data = {
    "order_id": [101, 102, 103, 104, 105, 106],
    "customer_id": [1, 2, 1, 3, 2, 4],
    "order_date": [
        "2025-01-10",
        "2025-01-15",
        "2025-02-05",
        "2025-02-18",
        "2025-03-02",
        "2025-03-12"
    ],
    "order_amount": [500, 700, 400, 1000, 650, 900]
}

df = pd.DataFrame(data)

df["order_date"] = pd.to_datetime(df["order_date"])
# print(df["order_date"].dtypes)

monthly_revenue = df.groupby(
    df["order_date"].dt.to_period("M")
)["order_amount"].sum()
# print(monthly_revenue)

unique_customers= df.groupby(
    df["order_date"].dt.to_period("M")
)["customer_id"].nunique()              #nunique return count of unique elements
print(unique_customers.idxmax())
