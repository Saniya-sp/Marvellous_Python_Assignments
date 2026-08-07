"""WAP that copies all .txt files from one directory to another every ten minutes
The program should handle:
    Accept source and destination directories
    Validate both directories
    Copy only .txt files
    Maintain a log of copied files
    Avoid terminating if one file cannot be copied

"""

import os
import time
import schedule
import datetime
import shutil

def CopyTextFiles(source, destination):
    
    # Validate directories
    if not os.path.isdir(source):
        print("Source directory is invalid.")
        return

    if not os.path.isdir(destination):
        print("Destination directory is invalid.")
        return

    for FolderName, SubFilder, FileName in os.walk(source):

        for file in FileName:

            source_path = os.path.join(source, file)
            destination_path = os.path.join(destination, file)

            # Copy only .txt files
            if os.path.isfile(source_path) and file.endswith(".txt"):

                try:
                    shutil.copy(source_path, destination_path)

                    print(f"{file} copied successfully.")

                except Exception as e:
                    # Continue copying remaining files
                    with open("CopyLog.txt", "a") as log:
                        log.write(
                            f"Failed to copy {file}. Reason: {e}\n"
                        )

                    print(f"Failed to copy {file}")
        

def main():

    schedule.every(10).minutes.do(CopyTextFiles, "Test", "Test1")
    # schedule.every(10).seconds.do(CopyTextFiles, "Test", "Test1")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()



