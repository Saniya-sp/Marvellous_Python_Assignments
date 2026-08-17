"""Draw a boxplot for Attendencec. Identify if any outliers are present"""

import matplotlib.pyplot as plt
import pandas as pd

def main():
    file_name = 'student_performance_ml.csv'
    df = pd.read_csv(file_name)
    # Draw boxplot
    plt.boxplot(df["Attendance"],notch=False, vert=True, patch_artist=True)

    plt.ylabel("Attendance")
    plt.title("Boxplot of Attendance")

    plt.show()

    # To identify outliers
    # use the IQR (Interquartile Range) method

    Q1 = df["Attendance"].quantile(0.25)
    Q3 = df["Attendance"].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - (1.5 * IQR)
    upper_limit = Q3 + (1.5 * IQR)

    outliers = df[
        (df["Attendance"] < lower_limit) |
        (df["Attendance"] > upper_limit)
    ]

    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)

    print("\nLower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)

    print("\nOutliers:")
    print(outliers)


if __name__ == "__main__":
    main()


#-----------------------------------------------------------------------------------------------------------------------------

# Observation:
#     No outliers are present in the Attendance column because all attendance values lie within the lower and upper IQR limits.


