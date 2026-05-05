import numpy as np

a1= np.arange(10)
a2= np.arange(12).reshape(3,4)
# a3= np.arange(8).reshape(2,2,2)


# INDEXING
# print(a1[-1])
# print(a1[5])

# print(a2[1,2])
# print(a3[0,0,0])

# print(a1[5:2:-1])
# print(a2[0,:])
# print(a2[::2,::3])
# print(a2[::2,1::2])
# print(a2[1,::3])
# print(a2[:2,1:])

a3 = np.arange(27).reshape(3,3,3)
# print(a3[1,:,1])
# print(a3[2,1:,1:])
# print(a3[::2,0,::2])

# ITERATING

# for i in a1:
#     print(i)

for x in np.nditer(a2, op_flags=['readwrite']):
    x[...]= x*2

print(a2)