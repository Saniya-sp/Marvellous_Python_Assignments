"""Design automation script which accept process name and display system information of that process if it is running

Command: python Assignment34_2.py Folder_name Process_name

"""


#scheduler added
import psutil
import sys
import os
import time
import schedule

def Find_Process(FolderName, process_name):
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

    fobj.write(Border+"\n")
    fobj.write("____Marvellous Platform Survillence System____")
    fobj.write("Logfile gets created at : "+timestamp+"\n")

    fobj.write(Border+"\n")
    fobj.write("---------------System Report---------------")

    fobj.write("\n\n\n\n")   

    found = False

    for process in psutil.process_iter(
        ['name', 'pid', 'username', 'status', 'cpu_percent', 'memory_percent']
    ):
        try:
            name = process.info['name']

            if name and name.lower() == process_name.lower():

                found = True

                fobj.write("\nProcess is running!\n")
                fobj.write("-" * 40+ "\n")
                fobj.write("Process Name :"+ name+ "\n")
                fobj.write("PID          :" + str(process.info['pid'])+ "\n")
                fobj.write("Username     :" + process.info['username']+ "\n")
                fobj.write("Status       :" + process.info['status']+ "\n")
                fobj.write("CPU Usage    :" + str(process.info['cpu_percent']) + "%"+ "\n")
                fobj.write("Memory Usage :" + str(process.info['memory_percent']) + "%"+ "\n")
                fobj.write("-" * 40)
               
        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass

        except TypeError as e:
            # print("Exception: ",str(e))
            fobj.write("Exception: " + str(e))

    if not found:
        print(f"\nProcess '{process_name}' is not running.")
        fobj.write("\nProcess " + process_name + " is not running.")

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
    if (len(sys.argv)==2):

        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This automation script is used to perform")
            print("1 : It fethc the information of running processes")
            print("2 : It maintains all records into log file")
            print("3 : It sends the logfile through mail periodically.")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as :")
            print(f"python {sys.argv[0]} Folder_Name Process_Name")
            # print("Time_Interval: Time in minutes for periodic execution")
            print("Folder_Name: Name of folder for periodic execution")
            print("Process_Name: Name of process to check")
            
        else:
            print("Unable to proceed as there is no matching argument")
            print("Please use --h or --u flag for more details")

    #Actual project code
    elif (len(sys.argv)==3):
        
        Find_Process(sys.argv[1], sys.argv[2])

    else:
        print("Invalid number of arguments.")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for more details")

    print(Border)
    print("____Thank You For Using Our Automation System____")
    print(Border)
    
if __name__ == "__main__":
    main()

