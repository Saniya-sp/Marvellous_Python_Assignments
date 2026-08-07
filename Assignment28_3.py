"""Display file line by line
PB Statement: WAP which accepts a file name from user and displays the content
of the file line by line on the screen

ip: Demo.txt
op: Display each line of Demo.txt one by one.
"""

import sys

def main():

    try:
        fileName = sys.argv[1]
        fobj = open(fileName,"r")
        count = 0
        
        for line in fobj:
            print(line, end="")
            
        fobj.close()

        
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()