"""Frequency of string in file
PB Statement: WAP which accepts a file name and one string from user and returns
frequency (count of occurrences) of that string in the file
    
ip: Demo.txt Marvellous
op: COunt how many times "Marvellous" is appears in Demo.txt
"""

import sys

def main():

    try:
        filename = input("Enter file name: ")
        word = input("Enter word to search: ")

        fobj = open(filename, "r")

        count = 0
        for line in fobj:
            words = line.split()
            count += words.count(word)
            # if word in words: 
            #     count += 1

        fobj.close()

    
        print(f"Word: {word} is occurred {count} times.")
       
        
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()