"""Create a gender column and perform one-hot encoding."""


import pandas as pd

data={
    "Name":['Alice', 'Sagar', 'Pooja'],
    "Math": [85,90,78],
    "Science": [92,88,80],
    "English": [75,85,82],
}

df = pd.DataFrame(data)

df['Gender'] = ["F","M","M"]
df_encoded = pd.get_dummies(df, columns=['Gender'])
print(df_encoded)