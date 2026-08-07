"""Schedule a task that executes every 5 minutes:
The task should write the current date and time into a file named:
Marvellous.txt
New entries should be appended without removing previous entries
Excample:
Task executed at : 28-07-2026 14:45:00 PM
Task executed at : 28-07-2026 14:50:00 PM
Task executed at : 28-07-2026 14:55:00 PM

"""

import schedule
import time
import datetime

def Display(filename):
    fobj = open(filename, "a")

    fobj.write("Task executed at :" + datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")+ "\n")

    fobj.close()

def main():

    schedule.every(5).minutes.do(Display, "Marvellous.txt")

    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()