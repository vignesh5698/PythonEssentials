import pandas as pd
df1 = pd.read_csv("details.csv")
print(df1)
print(df1.describe())
print(df1['Salary']>50000)
filter=df1['Salary']>50000
print(df1[filter])
print(df1[df1['Age']>5])