#  print("hello")

# import pandas as pd
# print(pd.__version__)
# df=pd.read_csv('~/Documents/Python_files/test_file.csv')
# df=pd.read_csv('~/Documents/Python_files/test_file1.csv')
# print(df)

# x = 5
# y = "John"
# print(x)
# print(y)

import pandas as pd 
from pandas_profiling import ProfileReport
data=pd.read_csv('~/Documents/Jup_notebooks/Clean_Dataset.csv')
# print(data)
#print(data.head())
# data.info()
# data.describe()
# data.isnull()
profile=ProfileReport(data,title="Airline data")
profile.to_file("Airline analysis.html")
print("feeling excited - wow! I nailed it - super Kavisha")
