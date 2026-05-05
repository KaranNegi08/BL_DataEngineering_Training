import numpy as np

a1 = np.arange(12).reshape(3,4)
a2= np.arange(12,24).reshape(3,4)


# SCALAR OPERATION
# a3=a1**2



# print(a1>5)
# print(a1+a2)
# print(a3)

# AGGREGATION OPERATIONS
# print(np.sum(a1))
# print(np.max(a1))
# print(np.min(a1))
# print(np.mean(a1))

# print(np.sum(a2, axis=0))


A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(A @ B)