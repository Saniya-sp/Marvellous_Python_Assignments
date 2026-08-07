"""WA python program that schedule a function to print:
Coding Kar..!
every 30 minutes

"""

import schedule
import time
import datetime

def Display():
    print("COding Kar..!")

def main():
    schedule.every(30).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)
    

if __name__ == "__main__":
    main()