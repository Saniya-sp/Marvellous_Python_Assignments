"""Write a script that schedules following tasks
    Print Lunch Time! every day at 1:00 PM
    Print Wrap Up work every day at 6:00 PM.

both tasks should be handled by diffrent functions.
"""

import schedule
import time
import datetime

def Lunch():
    print("Lunch Time !")
    
def WrapUp():
    print("Wrap up work")
    
def main():

    schedule.every().day.at("16:10").do(Lunch)
    schedule.every().day.at("16:11").do(WrapUp)

    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()