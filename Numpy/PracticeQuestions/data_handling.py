import numpy as np

dataset = np.array([[1, np.nan, 3],
                [4, np.nan, np.nan],
                [7, 8, 9]])
dataset[np.isnan(dataset)] = np.nanmean(dataset)
print(dataset)

print()
col_mean = np.nanmean(dataset, axis=0)

inds = np.where(np.isnan(dataset))
dataset[inds] = np.take(col_mean, inds[1])
print(dataset)