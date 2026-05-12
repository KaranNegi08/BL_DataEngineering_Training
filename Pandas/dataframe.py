import numpy as np
import pandas as pd


# USING LIST
student_data = [
    [100, 80,10],
    [92, 70,20],
    [97, 90,5],
    [99, 100,24]
]

data = pd.DataFrame(student_data, columns=['iq','marks','package in lakhs'])
# print(data)

#USING DICT
student_dict= {
    'iq':[10,90,120,88],
    'marks':[99, 100,24,98],
    'package':[100, 80,10,78]
}

data= pd.DataFrame(student_dict)
# print(data)

movies= pd.read_csv("movies.csv")
# print(movies)

ipl= pd.read_csv("ipl-matches.csv")
# print(ipl)

# print(ipl.shape)
# print(ipl.dtypes)
# print(ipl.index)
# print(movies.columns)
# print(type(ipl.values))
# print(ipl.info) #Return  whole data
# print(ipl.info()) 
# print(ipl.describe())
# print(movies.describe())
# print(movies.isnull().sum())
# print(movies.duplicated().sum())
 
# print(movies.iloc[0:5])


#FILTERING DATAFRAME

# new_df = ipl[ipl['MatchNumber'] == 'Final']
# winning_team = new_df[['Season','WinningTeam']]
# print(winning_team)


# super_over = ipl[ipl['SuperOver'] == 'Y']
# teams= super_over[['Team1','Team2']]
# print(teams)
# print(teams.shape[0])


# wins = ipl[(ipl['City'] == 'Kolkata') & (ipl['WinningTeam'] == 'Chennai Super Kings')]
# print(wins)



# winner = ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]/ipl.shape[0]*100
# print(winner)


data={
    'Name':["John","Anna","Peter"],
    'Age':[28,56,52],
    'City':['Agra','Noida','Jaipur'],
    'Salary':[52000,45000,80000]
}
df = pd.DataFrame(data)
# print(df)
# print(df[['Age','Name']])
# df['Designation']=['Doctor','Pilot','Engineer']
# df.drop('Designation',axis =1, inplace=True)
# print(df.loc[[0,2]])

# df.iloc[0:2,2:]
# df.loc[[0,1]][['City','Salary']]
# df.iloc[1:,:2]


# CONDITIONAL SELECTION
# people age greater than 30
# print(df[(df['Age'] > 30) & (df['City'] =='Jaipur')])


# data={
#     'A':[1,2,np.nan,4,5],
#     'B':[np.nan,2,3,4,5],
#     'C':[1,2,3,np.nan,np.nan],
# }
# df =pd.DataFrame(data)

# df.isna()
# df.isna().sum()
# df.isna().any()


# df.dropna()
# df.dropna(thresh=3)
# df.dropna(how='all')
# df.dropna(subset=['A'])


# df.fillna(0)
# values={'A':0,'B':100,'C':300}
# df.fillna(value=values)
# df.fillna(df.mean())
# df.fillna(method='ffill')
# df.fillna(method='bfill')



# emplopyees= pd.DataFrame({
#     'emp_id':[1,2,3,4],
#     'name':['suresh','vijay','kunal','dishant'],
#     'department':['HR','IT','SDE','HR']
# })

# salaries = pd.DataFrame({
#     'emp_id':[1,2,3,6],
#     'salary':[30000,40000,50000,80000],
#     'bonus':[5000,7000,9000,10000]
# })


# pd.merge(emplopyees,salaries, on='emp_id',how='inner')
# pd.merge(emplopyees,salaries, on='emp_id',how='outer')
# pd.merge(emplopyees,salaries, on='emp_id',how='left')
# pd.merge(emplopyees,salaries, on='emp_id',how='right')


# df1= pd.DataFrame({
#     'A':['A0','A1','A2'],
#     'B':['B0','B1','B2'],
#     'C':['C0','C1','C2']
# })

# df2= pd.DataFrame({
#     'A':['A3','A4','A5'],
#     'B':['B3','B4','B5'],
#     'C':['C3','C4','C5']
# })


# pd.concat([df1,df2])
# pd.concat([df1,df2], axis=1)
# pd.concat([df1,df2], ignore_index= True)


# df1 = pd.DataFrame({
#     "Name": ["Karan", "Aman", "Dishant"]
# }, index=[1,2,3])

# df2 = pd.DataFrame({
#     "Marks": [90, 85]
# }, index=[1,2])

# df1.join(df2)
# df1.join(df2, how='outer')


# data = {
#     "Department": ["IT", "HR", "IT", "HR", "Sales"],
#     "Employee": ["Karan", "Aman", "Rohit", "Neha", "Simran"],
#     "Salary": [50000, 40000, 60000, 45000, 55000]
# }
# df = pd.DataFrame(data)

# cat = df.groupby('Department')['Salary'].sum()
# for i,v in cat:
#   print(i)
#   print(v)

# print(cat)

# Group by multiple columns
# df.groupby(['Department','Salary'])['Salary'].sum()
# df.groupby('Department')['Employee'].count()

# multiple aggregation
df.groupby('Department')['Salary'].agg(['mean','max','min'])