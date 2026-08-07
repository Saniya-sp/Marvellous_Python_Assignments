"""Display file content
PB Statement: WAP which accepts a file name from user opens that file, and displays the
entire content on the console

ip: Demo.txt
op: Display contents of Demo.txt on console
"""

import sys

def main():

    try:
       
        fileName = input("Enter file name: ")

        fobj = open(fileName,"r")
        
        data = fobj.read()
        print(data)
        fobj.close()

        
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()