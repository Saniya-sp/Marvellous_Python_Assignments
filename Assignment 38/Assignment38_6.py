"""Plot a histogram of study hours. Explain what the distribution tells you."""

import matplotlib.pyplot as plt
import pandas as pd

def main():
    
    file_name = 'student_performance_ml.csv'
    df = pd.read_csv(file_name)
    study_hours = df['StudyHours']
    plt.hist(
        study_hours,                  #Continuous Data
        bins=5,                 #no. of groups
        edgecolor="black",        #border colour
        alpha=0.8,              #transperancy
        rwidth=0.9            #relative width of bars

    )
 
    
    plt.title("Marvellous Histogram")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    main()

#----------------------------------------------

# Observation:
    # 7 students study 8 hrs, 
    # 6 students study 1.2 to 2.2 hrs, 
    # 5 students study 2.3 to 3.9 hrs, 
    # 6 students study 3.9 to 4.5 hrs, 
    # 6 students study 4.5 to 6.9 hrs.

