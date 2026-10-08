"""Drop the 'ENglish' column from the original dataframe"""

import pandas as pd

data={
    "Name":['Alice', 'Sagar', 'Pooja'],
    "Math": [85,90,78],
    "Science": [92,88,80],
    "English": [75,85,82],
}

df = pd.DataFrame(data)
df_dropped = df.drop(columns=['English'])
print(df_dropped)

