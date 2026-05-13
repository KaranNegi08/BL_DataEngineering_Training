import numpy as np
import pandas as pd

np.random.seed(1)

temperature_readings= np.random.randint(-4,45,size=(7,24))
# print(temperature_readings)
days=[
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thrusday",
    "Friday",
    "Saturday",
    "Sunday"
]

# Find the daily maximum and minimum temperature
max_temp = temperature_readings.max(axis=1)
# print(f"Daily max temperature of this week: {max_temp}")

min_temp = temperature_readings.min(axis=1)
# print(f"Daily min temperature of this week: {min_temp}")

# Identify the day with the largest temperature variation
max_variation= max_temp-min_temp
max_variation_index= np.argmax(max_variation)
max_variation_day= days[max_variation_index]
# print(max_variation)
print(f"The day with the largest temperature variation is: {max_variation_day}")

mean_temp = temperature_readings.mean()
std_deviation = temperature_readings.std()

lower_limit = mean_temp -2 * std_deviation
upper_limit = mean_temp +2 * std_deviation
print(f"Mean temperature: {mean_temp}")
# print(f"Standard deviation: {std_deviation}")

outliers = (temperature_readings < lower_limit )| (temperature_readings > upper_limit)
temperature_readings[outliers] = mean_temp
print(f"Outliers replaced with Standard Deviation. \n {temperature_readings}")