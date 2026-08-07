"""WAP that creates a new text file every minute.
The filena me should contain the current timestamp.
Example:
File_25_07_2026_16_30_00.txt
Write the following information into file:
    Filename
     Creation date
      Creation time
"""

import os
import time
import schedule
import datetime

def CreateFile():
    Border = "-" * 50

    timestamp = time.strftime("%d_%m_%Y_%H_%M_%S")
    LogFileName = os.path.join("File_%s.txt" %timestamp)
    
    fobj = open(LogFileName, "w")
    fobj.write("File name: %s" %LogFileName + "\n")
    fobj.write("Creation date: %s" %datetime.datetime.now().strftime('%d-%m-%Y') + "\n")
    fobj.write("Creation time: %s" %datetime.datetime.now().strftime('%I:%M:%S %p') +"\n")
    fobj.close()


def main():

    
    schedule.every(1).minutes.do(CreateFile)
    # schedule.every(5).seconds.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()



