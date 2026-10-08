"""Create a DataFrame with missing values and fill them with column mean"""

import pandas as pd
import numpy as np

data2 = {
    "Name":['Dan', 'Eve', 'Frank'],
    "Math": [np.nan, 76,88],
    "Science": [92,np.nan,85]
}

df2 = pd.DataFrame(data2)
df2.fillna(df2.mean(numeric_only=True), inplace=True)
print(df2)

