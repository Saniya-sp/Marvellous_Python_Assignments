"""Count lines in a file
PB Statement: WAP which accepts a file name from user and counts how many lines are present
in the file.
ip: Demo.txt
op: Total number of lines in Demo.txt 
"""

import sys

def main():

    try:
        fileName = sys.argv[1]
        fobj = open(fileName,"r")
        count = 0
        for line in fobj:
            count += 1

        fobj.close()

        print(f"Total number of lines in {fileName}: {count}")


    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()