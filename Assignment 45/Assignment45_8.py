"""Plot a histogram of math marks"""

import pandas as pd
import matplotlib.pyplot as plt 

data={
    "Name":['Bob', 'Sagar', 'Pooja'],
    "Math": [85,90,78],
    "Science": [92,88,80],
    "English": [75,85,82],
}

df = pd.DataFrame(data)

plt.hist(df['Math'],bins=5, edgecolor='black')
plt.title("Distribution of Math Marks")
plt.xlabel("MArks")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

