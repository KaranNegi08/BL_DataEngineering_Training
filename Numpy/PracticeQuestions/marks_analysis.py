import numpy as np
import random

arr = np.random.randint(20,100,50)

# print(np.median(arr))
# print(np.max(arr))
# print(np.min(arr))

result= arr[arr > 75]
print(result)


arr = np.where(arr<40,40,arr)
print(arr)
print(np.min(arr))