import numpy as np
import pandas as pd

np.random.seed(1)

time_track = np.random.randint(10,200, size=(14,6))

# print(time_track)
#  total time spent per course
total_time_spent = time_track.sum(axis=0)
# print(f"Total time spent per course: {total_time_spent}")

# Identify courses where average daily engagement exceeds a threshold
avg_engagement = time_track.mean(axis=0)
threshold=100

# high_engagement_course = np.where(avg_engagement > threshold)[0]
high_engagement_course= avg_engagement[avg_engagement > threshold]
# print(f"courses where average daily engagement exceeds a threshold: {high_engagement_course}")


# Rank courses based on engagement
ranking = high_engagement_course[np.argsort(high_engagement_course)[::-1]   ] #decreasing order
print(f"Course ranking based on engagement: {ranking}")
