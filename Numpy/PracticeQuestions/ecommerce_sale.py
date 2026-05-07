import numpy as np
import random

sales = np.random.randint(20,100,30)

# top_five = np.sort(sales)[::-1]
# print(sorted[:5])
top_five = np.sort(sales)[-5:]
# print(top_five)

above_average = sales[sales > np.mean(sales)]
print(above_average)



