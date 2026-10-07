"""Design automation script which accept directory name from user and create logfile in that directory which contains 
information of running process as its name, PID, username 

Command: python Assignment34_3.py Marvellous_Logs

"""

#scheduler added
import psutil
import sys
import os
import time
import schedule

def display_processes(FolderName):
    Border = "-" * 50
    Ret = False
    Ret = os.path.exists(FolderName)

    if Ret == True:
        # print("")
        Ret = os.path.isdir(FolderName)
        if Ret == False:
            print("Unable to proceed as directory name is existing but its not a directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for the log file gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, "Marvellous_%s.log" %timestamp)

    fobj = open(FileName, "w")

    print(f"Log file gets successully created with name : {FileName}")

    print(f"Log file gets successully created with name : {FileName}")
    fobj.write(Border+"\n")
    fobj.write("____Marvellous Platform Survillence System____")
    fobj.write("Logfile gets created at : "+timestamp+"\n")

    fobj.write(Border+"\n")
    fobj.write("---------------System Report---------------")

    fobj.write("\n\n\n\n")
   

    for process in psutil.process_iter(['name', 'pid', 'username']):
        try:
            name = process.info['name']
            pid = process.info['pid']
            username = process.info['username']

            log_message = (
                f"Process Name: {name}, "
                f"PID: {pid}, "
                f"Username: {username}"
            )

            print(log_message)
            fobj.write(log_message+"\n")

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

        except TypeError as e:
            print("Exception: ",str(e))
            fobj.write("Exception: " + str(e))

    fobj.write(Border+"\n")
    fobj.write("--------------End of log file---------------")
    fobj.write(Border+"\n")
    
    fobj.close()


def main():
    Border = "-" * 50
    print(Border)
    print("____Marvellous Platform Survillence System____")
    print(Border)

    # --h & --u handling
    if (len(sys.argv)<2):

        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):

            print("This automation script is used to perform")
            print("1 : It fetch the information of running processes")
            print("2 : It maintains all records into log file")
            print("3 : It sends the logfile through mail periodically.")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):

            print("Use the automation script as :")
            print(f"python {sys.argv[0]} Folder_Name")
            # print("Time_Interval: Time in minutes for periodic execution")
            print("Folder_Name: Name of folder for periodic execution")
            
        else:

            print("Unable to proceed as there is no matching argument")
            print("Please use --h or --u flag for more details")

    #Actual project code
    elif (len(sys.argv)==2):
        
        display_processes(sys.argv[1])

    else:
        print("Invalid number of arguments.")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for more details")

    print(Border)
    print("____Thank You For Using Our Automation System____")
    print(Border)
    
if __name__ == "__main__":
    main()

