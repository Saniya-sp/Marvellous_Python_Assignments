"""Normalize the 'Math; scores using Min-Max scaling
"""
import pandas as pd

data={
    "Name":['Alice', 'Sagar', 'Pooja'],
    "Math": [85,90,78],
    "Science": [92,88,80],
    "English": [75,85,82],
}

df = pd.DataFrame(data)

df['Math_Norm'] = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())
print(df[['Name', 'Math', 'Math_Norm']])
