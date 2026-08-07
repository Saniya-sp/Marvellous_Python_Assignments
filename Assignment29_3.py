"""Copy file content into a new file(COmmand line)
PB Statement: WAP which accepts an existing file name through command line arguments,
create a new file named Demo.txt and copies all content from the given file into Demo.txt

ip (Command line): ABC.txt
op: Created Demo.txt and copy contents of ABC.txt into Demo.txt
"""

import sys

def main():

    try:

        source = sys.argv[1]
        destination = sys.argv[2]

        file1 = open(source,"r")
        file2 = open(destination,"w")
        
        for line in file1:
            file2.write(line)

        file1.close()
        file2.close()

        
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()