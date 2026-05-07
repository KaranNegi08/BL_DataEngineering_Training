import numpy as np

arr= np.arange(11)

even_numbers = arr[arr%2 == 0]
# print(even_numbers)


replace_odd_number= np.where(arr%2 != 0, -1, arr)
print(replace_odd_number)

# print(len(even_numbers))