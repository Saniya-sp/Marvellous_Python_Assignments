"""Based on the dataset values analyze whether
    Higher StudyHours increse the chance on passing
    High Attendence improves the final result
    Write your observation in 4-5 lines"""
##### value_counts = it gives the count of each value present in column


import pandas as pd

file_name = 'student_performance_ml.csv'
df = pd.read_csv(file_name)

study_hrs = df["StudyHours"].mean()
print(study_hrs)

high_study = df[df["StudyHours"] > 5]

study_passing_rate = high_study['FinalResult'].value_counts(normalize=True) * 100
print(study_passing_rate)

high_attendence = df[df["Attendance"] > 5]

attendence_passing_rate = high_attendence['FinalResult'].value_counts(normalize=True) * 100
print(attendence_passing_rate)

#--------------------------------------------------------------------------------------------------------------------------

# Observation:
#        From the data it seems like higher StudyHours don't make much difference in passing. 
#        But high attendence improves the final results.