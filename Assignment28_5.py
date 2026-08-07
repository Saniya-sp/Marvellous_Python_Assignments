"""Search a word in file
PB Statement: WAP which accepts a file name and a word from user and check whether
that word is present in file or not
    
ip: Demo.txt Marvellous
op: Display whether the word Marvellous is present in Demo.txt or not
"""

import sys

def main():

    try:
        filename = input("Enter file name: ")
        word = input("Enter word to search: ")

        fobj = open(filename, "r")

        found = False

        for line in fobj:
            words = line.split()
            if word in words:
                found = True
                break

        fobj.close()

        if found:
            print(f"{word} is present in {filename}")
        else:
            print(f"{word} is not present in {filename}")

        
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()