import numpy as np

a= np.arange(10)
# print(np.sum(a))

# print(np.sin(a))

# SIGMOID
def sigmoid(array):
    return 1/(1 + np.exp(-(array)))

b = sigmoid(a)
# print(b) 

import random

actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)

def mse(actual, predicted):
    return np.mean((actual - predicted)**2)

# print(mse(actual,predicted))

# WORKING WITH MISSING VALUES
a= np.array([1,2,3,np.nan,6])
b=a[~np.isnan(a)]
# print(b)

# PLOTTING GRAPHS
import matplotlib.pyplot as plt
x= np.linspace(-10,10,100)
# y=x
# y=x**2
y=np.sin(x)
plt.plot(x,y)

plt.show()




