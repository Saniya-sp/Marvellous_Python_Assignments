"""Group students by gender and calculate average marks."""

import pandas as pd

data={
    "Name":['Alice', 'Sagar', 'Pooja'],
    "Math": [85,90,78],
    "Science": [92,88,80],
    "English": [75,85,82],
}

df = pd.DataFrame(data)

df['Gender'] = ["F","M","M"]

print(df.groupby('Gender')[['Math','Science','English']].mean())

