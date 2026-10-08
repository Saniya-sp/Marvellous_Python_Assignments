"""Replace 'Charlie' with the 'Chris' in 'Name' column """

import pandas as pd

data={
    "Name":['Charlie', 'Sagar', 'Pooja'],
    "Math": [85,90,78],
    "Science": [92,88,80],
    "English": [75,85,82],
}

df = pd.DataFrame(data)
df['Name'] = df['Name'].replace('Charlie', 'Chris')

print(df)