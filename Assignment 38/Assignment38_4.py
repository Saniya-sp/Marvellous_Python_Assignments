"""Use value_counts() to analyze the distribution of FinalResult
Calculate the percentage of Pass and Fail students
Is the dataset balanced? Justify your answer.
"""
import pandas as pd

file_name = 'student_performance_ml.csv'
df = pd.read_csv(file_name)

# Count Pass and Fail
result_counts = df["FinalResult"].value_counts()

print("FinalResult Distribution:")
print(result_counts)

# Calculate percentage
result_percentage = df["FinalResult"].value_counts(normalize=True) * 100

print("\nPercentage of Pass and Fail:")
print(result_percentage)

# Display separately
pass_percentage = (df["FinalResult"] == 1).mean() * 100
fail_percentage = (df["FinalResult"] == 0).mean() * 100

print("\nPass Percentage:", pass_percentage)
print("Fail Percentage:", fail_percentage)

#---------------------------------------------------------------------------------------------------------------------#

# Observation:

# Dataset is NOT balanced. A balanced dataset would have the classes approximately equally represented, such as:
# Pass : 50%
# Fail : 50%

# The dataset is not perfectly balanced because 60% of the students have FinalResult = 1 (Pass), while only 40% have 
# FinalResult = 0 (Fail). Therefore, the Pass class is more represented than the Fail class.