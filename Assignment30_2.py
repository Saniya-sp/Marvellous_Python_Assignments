"""WA python program that displays the current date and time after every one minute:
Use the datetime module.
Expected op:
Current Date and Time: 28-7-2026 04:30:00 PM
"""

import schedule
import time
import datetime

def Display():
    print("Current Date and Time: ",datetime.datetime.now())

def main():
    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()