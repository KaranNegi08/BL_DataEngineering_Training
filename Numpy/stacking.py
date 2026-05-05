import numpy as np

a1= np.arange(12).reshape(3,4)
a2= np.arange(12,24).reshape(3,4)

# print(np.hstack((a1,a2)))
# print(np.vstack((a1,a2)))

result=np.stack((a1,a2))
# print(result)
# print(np.concatenate((a1,a2), axis=1))

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

# print(np.vstack((A, B)))
# print(np.hstack((A, B)))

features1 = np.array([[1],[2],[3]])
features2 = np.array([[4],[5],[6]])

combined = np.hstack((features1, features2))
print(combined)