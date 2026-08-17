"""Using Pandas function calsulate and display
    Average studey hours
    Average attendance
    Maximum PreviousScore
    Minimun SleepHours
"""

import pandas as pd

file_name = 'student_performance_ml.csv'
df = pd.read_csv(file_name)

print("Average Study Hours:", df["StudyHours"].mean())

print("Average Attendance:", df["Attendance"].mean())

print("Maximum Previous Score:", df["PreviousScore"].max())

print("Minimum Sleep Hours:", df["SleepHours"].min())



