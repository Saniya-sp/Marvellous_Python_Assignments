"""WAP that scans a specified directory every minute.
The task should display:
    Directory name
    Number of files
    Number of subdirectories
    Date and time of scanning
    
Use the os module
Example op:
DIrectory Scanned: E:/Data
Total Files: 15
Total Subdirectories: 4
Scan Time: 25-07-2026 04:30:00 PM
"""

import sys
import os
import time
import schedule
import datetime


def ScanDirectory(DirectoryName):
    files = 0
    directories = 0
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("Path is invalid.")
        return

    Ret = os.path.isdir(DirectoryName)
    if Ret == False:
        print("It is not a Directory.")
        return

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        files = len(FileName)
        subDirectories = len(SubFolder)
         
    print("Directory Scanned:", DirectoryName)
    print("Total Files:", files)
    print("Total Subdirectories:", subDirectories)
    print("Scan Time:", datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    print("-" * 40)

def main():
    
    path = input("Enter directory path: ")

    if not os.path.isdir(path):
        print("Invalid directory path.")
        return

    # Schedule scanning every minute
    schedule.every(1).minutes.do(ScanDirectory, path)

    print("Directory monitoring started...")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()



