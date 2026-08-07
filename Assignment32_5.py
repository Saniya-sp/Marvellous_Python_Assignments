"""WAP that deletes all empty files from a specified directory every hour

The program should handle:
    Scan the directory recursively
    Detect files whose size is zero bytes
    Delete the empty files
    Store deleted file paths in a log file
    Handle permission errors
Test the program only on a sample directory.

"""

import os
import time
import schedule
import datetime
import shutil

def DeleteFiles(source):

    timestamp = datetime.datetime.now()
    timestamp = time.strftime("%d_%m_%Y_%H_%M_%S")
    LogFileName = os.path.join("File_%s.txt" %timestamp)

    fobj = open(LogFileName, "w")

    # Validate directories
    if not os.path.isdir(source):
        print("Source directory is invalid.")
        return

    for FolderName, SubFilder, FileName in os.walk(source):

        for file in FileName:

            source_path = os.path.join(FolderName, file)
            print("source_path:",source_path)
            print("File: ",file)
            # Copy only .txt files
            if os.path.isfile(source_path):

                try:
                    delete_fobj = open(source_path, "r")
                    data = delete_fobj.read()
            
                    if len(data) == 0:
                        
                        print("File is empty.")
                        delete_fobj.close()
                        os.remove(source_path)
                        fobj.write("File deleted successfullt: %s" %source_path)
                        print(f"{source_path} : File is deleted.")

                    else:
                        delete_fobj.close()

                        print("File is not empty")
                        
                except Exception as e:
                    # Continue copying remaining files
                    with open("CopyLog.txt", "a") as log:
                        log.write(
                            f"Failed to delete {file}. Reason: {e}\n"
                        )

                    print(f"Failed to delete {file}: {e}")
        

def main():

    # schedule.every(10).minutes.do(DeleteFiles, "Test1")
    schedule.every(5).seconds.do(DeleteFiles,"Test1")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()



