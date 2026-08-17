"""Create scatter plot of StudyHours vs PreviousScore
Use different colours for pass and fail students"""

import matplotlib.pyplot as plt
import pandas as pd

def main():
    file_name = 'student_performance_ml.csv'
    df = pd.read_csv(file_name)
    study_hours = df['StudyHours']
    previous_score = df['PreviousScore']

    # Separate Pass and Fail students
    pass_students = df[df["FinalResult"] == 1]
    fail_students = df[df["FinalResult"] == 0]

    # Scatter plot
    plt.scatter(
        pass_students["StudyHours"],
        pass_students["PreviousScore"],
        label="Pass"
    )

    plt.scatter(
        fail_students["StudyHours"],
        fail_students["PreviousScore"],
        label="Fail"
    )

    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.title("Study Hours vs Previous Score")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()


