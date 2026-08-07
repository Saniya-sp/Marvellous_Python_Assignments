##########################################################
#
#   Importing required libraries
#
##########################################################
# python assignment33.py "C:\Users\saniya pathan\Desktop\Marvellous_Assignments\Test1" 2 ReceiverEmail = command line i/p


import sys
import os
import time
import schedule
import datetime
from DeleteDuplicateFilesModule import DeleteDuplicate, FindDuplicate
from EmailSendingActivity import send_mail

##########################################################
#
#   Function name :     DeleteFilesProcess
#   Input :             Command line arguments
#   Description :       It performs complete deleteion operation
#   Date :              03/08/2026   
#   Author :            Saniya Siraj Pathan
#
##########################################################

def DeleteFilesProcess(DirectoryName):

    Border = "-"*30
    timestamp = time.ctime()
    LogDirectory = "Marvellous"
        
    Ret = os.path.exists(LogDirectory)

    if(Ret == False):
        print("Marvellous Automation Error : There is no such directory with name ",LogDirectory)
        os.mkdir(LogDirectory)
        print("Log directory: Marellous created successfully")
    
    LogFileName = "DuplicateRemovalLog_%s.log"%(timestamp)        
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")
    LogFilePath = os.path.join(LogDirectory,LogFileName )

    fobj = open(LogFilePath,"w")
    
    fobj.write(Border+"\n")
    fobj.write(" Duplicate File Removal Script \n")
    fobj.write(Border+"\n\n")

    sender = 'pathansaniyaxxxx@gmail.com'   
    app_password = "ztwuxxxxxxxxxxxxxx"
    #Your second email for testing
    receiver = "saniyapathanxxxxxxx@gmail.com"
    subject = 'Logs of deleted duplicate files.'
    body = """Hi, \n
        Please find attached log file of you directory. Details of deleted duplicate files are stored in the log file"""

        
    MyDict = FindDuplicate(DirectoryName, fobj)
    DeleteDuplicate(MyDict, fobj)
    send_mail(sender, app_password, receiver, subject, body,LogFilePath)
    
##########################################################
#
#   Function name :     main
#   Input :             Command line arguments
#   Description :       It controls the script
#   Date :              03/08/2026   
#   Author :            Saniya Siraj Pathan
#
##########################################################

def main():
    # Data = DeleteDuplicate("Test")
    # # print("Dictonary is :", Data)

    Border = "-"*40
    
    print(Border)
    print(" Duplicate File Removal Automation ")
    print(Border)
    
    if(len(sys.argv) == 4):
        
        if(sys.argv[1] == "--h" or sys.argv[1] == "--help"):
            print("This script scans a directory, identifies duplicate files using checksum, deletes duplicate file,\n"
            "and sends a logfile through email.")
            print("Usage:")
            print("python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>")
            print("Example:")
            print("python DuplicateFileRemoval.py E:/Data/Demo 50 pathansaniya00@gmail.com")
            print("For better usage please check --u flag")
        
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--usage"):
            print("Please execute the script as ")
            print("python FileName.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>")
            print("DirectoryPath should be absolute path")
        
        else:

            # schedule.every(1).minute.do(DeleteDuplicate,sys.argv[1])
            schedule.every(30).seconds.do(DeleteFilesProcess,sys.argv[1])
            # fobj.close()

            while True:
                schedule.run_pending()
                time.sleep(1)
                
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print(" Thank you for using Marvellous Automation Script ")
    print(Border)
    
    
    

##########################################################
#
#   Starter of the automation script
#
##########################################################


if __name__ == "__main__":
    main()

    # logfile- file counts of diff type, comnd line ip- dir name & time, periodic schedule