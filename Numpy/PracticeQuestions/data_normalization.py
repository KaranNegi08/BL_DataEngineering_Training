import numpy as np
import random

data = np.random.randint(10,60,10)
min_max= (data - np.min(data)) / (np.max(data) - np.min(data)) 
# print(data)
print(min_max)
