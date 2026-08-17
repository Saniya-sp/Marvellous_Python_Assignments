"""Create a plot showing relaton between AssignmentsCOmpleted and FinalResult.
Explain your observation"""


import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("student_performance_ml.csv")

    # Calculate average FinalResult for each number of assignments
    result = df.groupby("AssignmentsCompleted")["FinalResult"].mean()

    print(result)

    # Plot
    result.plot(kind="bar")

    plt.xlabel("Assignments Completed")
    plt.ylabel("Pass Rate")
    plt.title("Assignments Completed vs Final Result")
    plt.xticks(rotation=0)
    plt.show()

if __name__ == "__main__":
    main()


#-----------------------------------------------------------------------------------------------------------------------------

# Observation:
    # The plot shows a positive relationship between AssignmentsCompleted and FinalResult. 
    # Students who completed fewer than 6 assignments mostly failed, while students who completed 6 or more assignments passed in this dataset.
    # Therefore, completing more assignments appears to be associated with a higher chance of passing.