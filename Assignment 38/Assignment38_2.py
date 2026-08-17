"""WAP to display
Display:
    Total number of students in the dataset
    Count of how many students passed (FinalResult = 1)
    Count of how many students failed (FinalResult = 0)
"""

import pandas as pd

file_name = 'student_performance_ml.csv'
df = pd.read_csv(file_name)

passed_students= df['FinalResult']
passed_count = 0
for std in passed_students:
    if std == 1:
        passed_count += 1

failed_students= df['FinalResult']
failed_count = 0
for std in failed_students:
    if std == 0:
        failed_count += 1

print("Total students: ", len(df))
print("Passed students: ", passed_count)
print("Failed students: ", failed_count)



