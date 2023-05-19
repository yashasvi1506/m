#week_5
# from google.colab import files
# data = files.upload()
import pandas as pd
import scipy.stats as stats
from sklearn.impute import SimpleImputer
import numpy as np

#1st q
data = pd.read_excel('employees.xls')
# print(data)
imp = SimpleImputer(strategy = 'mean',missing_values=np.nan)
imp = imp.fit(data[['SALARY']])
data['SALARY'] = imp.transform(data[['SALARY']])
# print(data)
#2nd q
one_hot_encoded_data = pd.get_dummies(data, columns = ['JOB_ID'])
print(one_hot_encoded_data)
# print(data)

#3q
#L1 Norm

maximum=df["Weight"].max()
df["L1_Norm_Weight"]=df["Weight"]/maximum
#L2 Norm

summation=df["Weight"].sum()
df["L2_Norm_Weight"]=df["Weight"]/summation
#Max

squareSum=(df["Weight"]**2).sum()
df["Max_Norm_Weight"]=df["Weight"]/(np.sqrt(squareSum))
df.head()

