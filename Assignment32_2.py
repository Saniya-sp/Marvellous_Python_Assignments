"""WAP that monitors the size of a specififed file every 30 seconds

Write the following information into file:
    File path
    File size in bytes
    Date and time
"""

import os
import time
import schedule
import datetime

def ChkFile(filepath, LogFileName):
    Border = "-" * 50

    if not os.path.isfile(filepath):
        print("File not found.")
        return

    size = os.path.getsize(filepath)
    current_time = datetime.datetime.now()
    
    fobj = open(LogFileName, "w")
    fobj.write(f"File Path : {filepath}\n")
    fobj.write(f"File Size : {size} bytes\n")
    fobj.write(f"Date and Time : {current_time.strftime('%d-%m-%Y %I:%M:%S %p')}\n")
    fobj.write("-" * 40 + "\n")
    fobj.close()


def main():

    
    timestamp = time.strftime("%d_%m_%Y_%H_%M_%S")
    LogFileName = os.path.join("File_%s.txt" %timestamp)
        
    
    # schedule.every(2).minutes.do(CreateLog)
    schedule.every(30).seconds.do(ChkFile, 'assignment32_1.py', LogFileName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()



