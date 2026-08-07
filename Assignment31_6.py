"""WAP that schedules the following messages:
    Monday at 9:00 AM: Start your weekly goals
    Wednesday at 5:00 PM: Review your weekly progress
    Friday at 6:00 PM: Weekly work completed
    
Use:
schedule.every().moday.at()
schedule.every().wednesday.at()
schedule.every().friday.at()
"""

import schedule
import time


def Monday():
    print("Monday at 9:00 AM: Start your weekly goals")
    
def Wednesday():
    print("Wednesday at 5:00 PM: Review your weekly progress")

def Friday():
    print("Friday at 6:00 PM: Weekly work completed")


def main():

    # schedule.every(2).minutes.do(CreateLog)
    # schedule.every(2).seconds.do(CreateLog, DirectoryName)

    schedule.every().monday.at("09:00").do(Monday)
    schedule.every().wednesday.at("17:00").do(Wednesday)
    schedule.every().friday.at("18:00").do(Friday)


    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()




