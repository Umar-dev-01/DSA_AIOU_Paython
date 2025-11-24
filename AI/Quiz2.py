import pandas as pd

data1 = {
'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
'B': [1, 2, 3, 4, 5, 6],
'C': [10, 20, 30, 40, 50, 60]
}

df1 = pd.DataFrame(data1)

Group by 'A' → mean of B and sum of C

result1 = df1.groupby('A').agg({'B': 'mean', 'C': 'sum'})
print("Question 1 Result:\n", result1, "\n")





data2 = {
'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom'],
'Age': [25, 32, 41, 28, 35],
'Salary': [40000, 55000, 65000, 45000, 70000]
}

df2 = pd.DataFrame(data2)

result2 = df2[(df2['Age'] > 30) & (df2['Salary'] > 50000)].sort_values(by='Salary', ascending=False)
print("Question 2 Result:\n", result2)