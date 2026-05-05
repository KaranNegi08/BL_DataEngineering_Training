import numpy as np

a1= np.arange(12).reshape(3,4)
a2= np.arange(12,24).reshape(3,4)
ans = np.hsplit(a2,4)

# print(ans)

data = np.arange(10)

train, test = np.split(data, [7])
print(train, test)
