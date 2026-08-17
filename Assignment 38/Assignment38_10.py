"""plot SleepHours against FinalResult.
Does sleeping more gurantee success ? Explain"""


import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("student_performance_ml.csv")

    plt.scatter(df["SleepHours"], df["FinalResult"])

    plt.xlabel("Sleep Hours")
    plt.ylabel("Final Result")
    plt.title("Sleep Hours vs Final Result")

    plt.yticks([0, 1], ["Fail", "Pass"])

    plt.show()

if __name__ == "__main__":
    main()


#-----------------------------------------------------------------------------------------------------------------------------

# Observation:
    # Yes, sleeping more does guarantee success. Also the dataset shows that students sleeping 6 hours can have either a Pass or Fail result. 
    # Although higher sleep hours appear to be associated with better results in this dataset.