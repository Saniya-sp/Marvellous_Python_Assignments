"""Plot a pie chart of subject marks for 'Bob' """

import pandas as pd
import matplotlib.pyplot as plt

data={
    "Name":['Bob', 'Sagar', 'Pooja'],
    "Math": [85,90,78],
    "Science": [92,88,80],
    "English": [75,85,82],
}

df = pd.DataFrame(data)

bob = df[df['Name'] == 'Bob'][['Math', 'Science', 'English']].values.flatten()
labels = ['Math', 'Science', 'English']

plt.pie(bob, labels=labels, autopct='%1.1f%%')
plt.title("Bob's Subject Wise Distribution")
plt.show()

