import numpy as np
import random

A= np.random.randint(1,10,(3,3))
B= np.random.randint(1,10,(3,3))

# print(A)
# print(B)
# print(A@B)
# print(A*B)

print(np.linalg.det(A))

