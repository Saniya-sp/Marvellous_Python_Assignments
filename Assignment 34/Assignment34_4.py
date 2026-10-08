"""Design automation script which accept directory name and email id from user and create log file in that directory which contains
information of running processes a sits name, PID, Username. After creating log file send that log file to the specified mail.

Usage: filename.py folder_name email_id

"""

#scheduler added
import psutil
import sys
import os
import time
# import schedule
import smtplib
from email.message import EmailMessage


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
    fobj.write(" ____Running Process Details Logging____"+"\n")
    fobj.write(Border+"\n")
    
    fobj.write("Logfile gets created at : "+timestamp+"\n")

    fobj.write(Border+"\n")
    fobj.write("---------------System Report---------------")

    fobj.write("\n\n\n")

  

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

    return FileName


def send_mail(sender, app_password, receiver, subject, body, file_name):
    
    #Step 1: Create Email object
    msg = EmailMessage()
    #Step 2: Set mail headers
    msg["From"]=sender
    msg["To"] = receiver
    msg["Subject"] = subject
    #Step 3: Add mail body 
    msg.set_content(body)
    #Step 4: Create SMTP SSL connection manually 
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
    #Step 5: Login using Gmail + App password 
    smtp.login(sender, app_password)

    if file_name:
        # Attach file
        filename = file_name
        # filepath = r"D:\Reports\Report.pdf"
        with open(filename, "rb") as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="octet-stream",
            filename=file_name
        )

    #Step 6: Send the email 
    smtp.send_message(msg)
    #Step 7: Close connection manually
    smtp.quit()

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
        #Always use separate temporary/testing account
        sender_email = "pathansaniya00@gmail.com"
        #App password generated from Google account
        app_password = "ztwu boeu **** ****"
        #Your second email for testing
        receiver_email = "saniyapathan3618@gmail.com"
        subject = 'Test mail'
        body = 'Hi, this is you from your another mail id.'
        file_name = None

        file_name= display_processes(sys.argv[1])


        send_mail(sender_email, app_password, receiver_email, subject, body, file_name)
        
        print("Mail sent successfully.")

    else:
        print("Invalid number of arguments.")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for more details")

    print(Border)
    print("____Thank You For Using Our Automation System____")
    print(Border)
    
if __name__ == "__main__":
    main()

