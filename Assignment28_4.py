"""COpy file content into another file
PB Statement: WAP which accepts a two file names from user
    first file is an existing file
    second file is a new file
copy all content from the first file into the second file

ip: ABC.txt Demo.txt
op: COntent of ABC.txt copied into Demo.txt
"""

import sys

def main():

    try:
        # fileName = sys.argv[1]
        source = input("Enter source file name: ")
        destination = input("Enter destination file name: ")

        file1 = open(source, "r")
        file2 = open(destination, "w")

        for line in file1:
            file2.write(line)

        file1.close()
        file2.close()
        
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()