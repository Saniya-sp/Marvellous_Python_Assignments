"""WAP that creates a new log file every ten minutes
The filename should contain the current date and time
Example:
MarvellousLog_25_07_2026_16_30_00.txt
The file should contain:

Log file created successfully
Creation Time: 25-07-2026 04:30:00 PM
"""

import os
import time
import schedule
import datetime

def CreateLog():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join("MarvellousLog_%s.txt" %timestamp)

    fobj = open(FileName, "w")
    fobj.write("Log file created successfully \n")
    fobj.write("Creation Time: %s" %datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))


def main():
    
    # Schedule scanning every minute
    schedule.every(10).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()



