#week_3
# from google.colab import files
# data = files.upload()
import pandas as pd
data = pd.read_csv('employees.csv')
df = pd.DataFrame(data)
# print(df)
#1. Extract rows with missing values for a specific column, use isnull() for that column.
print(df['DEPARTMENT_ID'].isnull())
#2. Extract columns that contain at least one missing value.
print(df.isnull().any())
#3.Extract rows that contain at least one missing value, use any() method.
print(df.isnull().any(axis=1))
#4. Find a list of columns with missing data
x = list(df.isnull().any())
y=list(df.columns)
ans=[]
for i in range(len(y)):
  if x[i]:
    ans.append(y[i])
print(*ans)
#5. Find the number of missing values/data per column
print(df.isna().sum())
#6. Find the column with the maximum number of missing data
x = list(df.isna().sum())
y = list(df.columns)
a=[]
for i in range(len(x)):
  a.append([x[i],y[i]])
a.sort(reverse = True)
print("Column with maximum number of missing data :",a[0][1])
#7. Find the number total of missing values in the DataFrame
print(df.isna().sum().sum())
#8. Find rows with missing data
print(df.isnull().any(axis=1))
#9. Print a list of rows with missing data
x = list(df.isna().any(axis=1))
ans=[]
for i in range(len(x)):
  if x[i]:
    ans.append(i)
print("Rows with missing data :",)
print(*ans)
#10. Print the number of missing data per row
print(df.isna().sum(axis=1))
#11. Find the row with the largest number of missing data.
x = list(df.isna().sum(axis=1))
a=[]
for i in range(len(x)):
  a.append([x[i],i])
a.sort(reverse = True)
print("Row with maximum number of missing data :",a[0][1])

#12Q. Remove rows with missing data
x=df.dropna(axis=0, how='any')
print(x)
