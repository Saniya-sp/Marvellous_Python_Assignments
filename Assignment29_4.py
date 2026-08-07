"""Compare two files(COmmand line)
PB Statement: WAP which accepts two file names through command line arguments,
compares the content of both files 
If both files contain the same content, display Success.
Otherwise display Failure

ip (Command line): Demo.txt Hello.txt
op: Success or Failure
"""

import sys

def main():

    try:

        file1 = sys.argv[1]
        file2 = sys.argv[2]

        f1 = open(file1, "r")
        f2 = open(file2, "r")

        data1 = f1.read()
        data2 = f2.read()

        f1.close()
        f2.close()

        if data1 == data2:
            print("Success")
        else:
            print("Failure")

        
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()