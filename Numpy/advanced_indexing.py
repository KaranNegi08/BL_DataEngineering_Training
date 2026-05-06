import numpy as np
import random

# FANCING INDEXING (pick element in any order)
a= np.arange(24).reshape(6,4)
# print(a[[0,2,3,5]])
# print(a[:,[0,3]])

# BOOLEAN INDEXING
a= np.random.randint(1,100,24).reshape(6,4)
filtered = a[a>50]
# print(filtered)
filtered2 = a[ (a>50) & (a%2 == 0)]
# print(filtered2)
