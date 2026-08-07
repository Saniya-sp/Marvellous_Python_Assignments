"""Count words in a file
PB Statement: WAP which accepts a file name from user and counts the total number of
words in that file

ip: Demo.txt
op: Total number of words in Demo.txt 
"""

import sys

def main():

    try:
        fileName = sys.argv[1]
        fobj = open(fileName,"r")
        count = 0
        
        for line in fobj:
            words = line.split()
            count += len(words)

        fobj.close()

        print(f"Total number of words in {fileName}: {count}")


    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()