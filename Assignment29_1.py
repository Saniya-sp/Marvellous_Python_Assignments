"""Check file exists in current directory
PB Statement: WAP which accepts a file name from user and check whether
that file exists in the current directory or not
    
ip: Demo.txt Marvellous
op: Display whether Demo.txt exist or not
"""

import os

def main():

    try:
        filename = input("Enter file name: ")

        if(os.path.exists(filename)):
            print("File is present in current directory")
        else:
            print("There is no such file")
        
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()