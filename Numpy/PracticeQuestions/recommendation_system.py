import numpy as np

ratings = np.array([
    [5, 4, np.nan],
    [3, np.nan, 4],
    [4, 5, 5]
])

avg_rating= np.nanmean(ratings, axis=1)
print(avg_rating)
print("Max rating item at index : " , np.argmax(avg_rating))
