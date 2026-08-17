"""WAP to load the file student_performance_ml.csv using pandas.
Display:
    First 5 records
    last 5 records
    total no of rows and columns
    list of column names
    data type of each column"""

import pandas as pd

file_name = 'student_performance_ml.csv'
df = pd.read_csv(file_name)

print("First 5 records: ",df.head())
print("Last 5 records: ",df.tail())
print("total no of rows and columns: ",df.shape)
print("list of column names: \n",df.columns)
print("data type of each column: \n",df.dtypes)


