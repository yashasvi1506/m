import pandas as pd
data = pd.read_csv('Automobile_data.csv')
df = pd.DataFrame(data)
# print(df)
#1
print("Number of rows",len(df))
print("Number of columns",len(df.columns))
print("Datatypes :")
print(df.dtypes)
print(df.describe())
#2
print(df.info())
#3
df.rename(columns = {"index":"idx"},inplace = True)
print(df)
#4
For x in df.columns:
Df[x].fillna(value=df[x].mean(),inplace=True)
Print(df)
#5
Df1=df.loc(:,[‘index’,’breed’,’weight_low_lbs’, ’weight_high_lbs’, ’height_low_lbs’, ’height_high_lbs’,])
Print(df1)
