import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# country = ['India','USA',"Nepal"]
# print(pd.Series(country))

# CUSTOM INDEX
marks=[92,94,98,98]
subjects = ['maths', 'english','hindi',"bio"]

marks_series = pd.Series(marks, index=subjects, name= "Virat Bhai")
# print(marks)


# SERIES ATTRIBUTES
# print(marks_series.size)
# print(marks_series.dtype) 
# print(marks_series.is_unique)

# print(marks_series.index)
# print(marks_series.values)


# SERIES USING CSV

subs=pd.read_csv("subs.csv").squeeze("columns")
# print(a)
# print(type(a))

kohli = pd.read_csv("kohli_ipl.csv", index_col="match_no").squeeze("columns")
# print(kohli)

movies = pd.read_csv("bollywood.csv", index_col="movie").squeeze("columns")
# print(movies)

# print(movies.head())
# print(kohli.head(3))

# print(movies.sample())

# FOR FREQUENCY COUNT
# print(movies.value_counts())
# print(kohli.sort_values())
# print(kohli)
# kohli.sort_values(inplace=True)
# print(kohli)

# print(movies.describe())

x= pd.Series([10,12,55,64,52,3,4,5122,4])
# print(x[2])
# print(kohli[1:10])
# kohli[1]=1000
# print(kohli)
kohli[2:4]=[100,100]
x[2:4]= [100,100]
# print(x)
# print(kohli)

# print(list(kohli))
# print(dict(kohli))

s = pd.Series([1, None, 3])

# print(s)

# plt.plot(subs)
# plt.show()




