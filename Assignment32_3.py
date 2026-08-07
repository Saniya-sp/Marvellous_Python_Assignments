"""WAP that reads and displays the content of a specified text file 
every minute

Handle the following conditions:
FIle does not exist
File is empty
Permission is denied
File cannot be opened
"""

import os
import time
import schedule

def ChkFile(filename):
    try:
        
        if not os.path.isfile(filename):
            print("File not found.")
            return

        fobj = open(filename, "r")
        data = fobj.read()

        if len(data) == 0:
            print("File is empty.")
        else:
            print("File Contents:")
            print(data)

    except FileNotFoundError:
        print("File does not exist.")

    except PermissionError:
        print("Permission denied.")

    except OSError:
        print("File cannot be opened.")


def main():

    # schedule.every(2).minutes.do(CreateLog)
    schedule.every(5).seconds.do(ChkFile, 'backup_log.txt')

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()



