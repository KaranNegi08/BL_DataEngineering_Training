import numpy as np

data = np.array([30, 32, -999, 35, 1000, 33], dtype='float')

data[(data == -999) | (data == 1000)] = np.nan

# print(np.nanmean(data))

# print(data[~np.isnan(data)])

valid_indices= np.where(~np.isnan(data))
print(valid_indices)
