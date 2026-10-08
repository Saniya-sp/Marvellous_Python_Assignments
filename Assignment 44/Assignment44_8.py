"""Plot a line chart of marks for 'Alice' across all subjects"""

import matplotlib.pyplot as plt
import pandas as pd

data={
    "Name":['Alice', 'Sagar', 'Pooja'],
    "Math": [85,90,78],
    "Science": [92,88,80],
    "English": [75,85,82],
}

df = pd.DataFrame(data)

# df['Total'] = df['Math'] + df['Science']+ df['English']

alice_marks = df[df["Name"] == 'Alice'][['Math', 'Science', 'English']].values.flatten()

subjects = ['Math', 'Science', 'English']

plt.plot(subjects, alice_marks, marker='o')
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.title("Alice Marks")
plt.show()



