"""Add a new column 'Status' where students with total>=250 are 'Pass', else 'Fail'."""

import pandas as pd
import matplotlib.pyplot as plt

data={
    "Name":['Bob', 'Sagar', 'Pooja'],
    "Math": [85,90,78],
    "Science": [92,88,80],
    "English": [75,85,82],
}

df = pd.DataFrame(data)

df['Total'] = df['Math'] + df['Science']+ df['English']

df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')

print(df[['Name', 'Total', 'Status']])