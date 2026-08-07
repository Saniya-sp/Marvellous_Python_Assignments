"""WAP that accepts a directory name from the user and counts the number of files
inside it every five minutes.
Write the result into:
DirectoryCountLog.txt
Each entry should containg:
    Directory path
    Number of files
    Date and time
"""

import os
import time
import schedule
import datetime

def CreateLog(DirectoryName):
    Border = "-" * 50

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    LogFileName = os.path.join("DirectoryCountLog.txt")

    Ret = os.path.exists(DirectoryName)

    if Ret == True:
        # print("")
        Ret = os.path.isdir(DirectoryName)
        if Ret == False:
            print("Unable to proceed as directory name is existing but its not a directory")
            return
    else:
        os.mkdir(DirectoryName)
        print("Directory for the log file gets created successfully")


    DirectoryPath = os.path.join(DirectoryName)
    files = 0
    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        if FileName:
            files += 1
        # subDirectories = len(SubFolder)

    # totalFiles = len(files)      
    fobj = open(LogFileName, "a")
    fobj.write("Directory path: %s \n" %DirectoryPath)
    fobj.write("Number of files : %s \n" %files)
    fobj.write(datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")+"\n")
    fobj.write(Border +"\n")

def main():

    DirectoryName = input("Enter directory name: ")
    
    # if not os.path.isdir(DirectoryName):
    #     print("Invalid directory path.")
    #     return
    
    # schedule.every(2).minutes.do(CreateLog)
    schedule.every(2).seconds.do(CreateLog, DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()



