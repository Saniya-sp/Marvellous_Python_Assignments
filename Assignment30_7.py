"""Write a Python program that performs a file backup every hour.
The program should:
    1.Accept the source file path
    2.Accept the destination directory path
    3.COpy the source file to the destination directory
    4.Add the current date and time to the backup filename
    5. write the backup operation details into
        backup_log.txt
Example backup filename:
    Data_25_07_2026_16_30_00.txt
Example log entry:
    Backup completed successfully at 25-07-2026 04:30:00 PM

Use the shutil module for file copying
"""

import schedule
import time
import datetime
import shutil
import os

    
def Backup(source, destination):
    try:
        # Get current date and time
        current_time = datetime.datetime.now()

        # # Extract source file details
        # filename = os.path.basename(source)
        # name, ext = os.path.splitext(filename)

        # Create backup filename
        backup_filename = (
            "Data" + "_" +
            current_time.strftime("%d_%m_%Y_%H_%M_%S") +
            ".txt"
        )

        # Create complete destination path
        backup_path = os.path.join(destination, backup_filename)

        # Copy file
        shutil.copy(source, backup_path)

        fobj = open("backup_log.txt", "a")
        # Write log\
        fobj.write(
            "Backup completed successfully at " +
            current_time.strftime("%d-%m-%Y %I:%M:%S %p") +
            "\n"
        )

        fobj.close()
        print("Backup completed successfully")

    except Exception as e:
        with open("backup_log.txt", "a") as log:
            log.write(
                "Backup failed at " +
                datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") +
                " Reason: " + str(e) +
                "\n"
            )

        print("Backup failed")

    
def main():

    source = input("Enter source file path: ")
    destination = input("Enter destination directory path: ")

    # Schedule backup every hour
    schedule.every(1).hours.do(Backup, source, destination)
    # schedule.every(1).minutes.do(Backup, source, destination)

    print("Backup scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()