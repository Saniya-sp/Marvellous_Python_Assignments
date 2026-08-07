##########################################################
#
#   Importing required libraries
#
##########################################################
import sys
import os
import hashlib
import datetime

##########################################################
#
#   Function name :     CalculateChecksum
#   Input :             Name of file
#   Description :       Calculates checksum of file
#   Date :              03/08/2026  
#   Author :            Saniya Siraj Pathan
#
##########################################################

def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)    #Standard size to read chunks. On hard disk:(1024kb) block is measuring unit, on RAM: (1024kb)Page is measuring unit

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

##########################################################
#
#   Function name :     FindDuplicate
#   Input :             Name of Directory
#   Description :       Finds all duplicate files periodically
#   Date :              03/08/2026  
#   Author :            Saniya Siraj Pathan
#
##########################################################

def FindDuplicate(DirectoryName, fobj):

    Ret = False

    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("Path is invalid.")
        return

    Ret = os.path.isdir(DirectoryName)
    if Ret == False:
        print("It is not a Directory.")
        return

    fobj.write("Starting time of directory scanning: %s" %datetime.datetime.now())
    fobj.write("Directory name is: %s" %DirectoryName)

    Duplicate = {}
    TotalFiles = 0

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for fname in FileName:
            TotalFiles += 1
            fname = os.path.join(FolderName, fname)
            
            Checksum = CalculateChecksum(fname)
            # print(f"{fname}: {Checksum}")

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
                fobj.write("Checksum of duplicate files")
            else:
                Duplicate[Checksum] = [fname]

    fobj.write("Total files in directory are: %d" %TotalFiles)

    return Duplicate

##########################################################
#
#   Function name :     DeleteDuplicate
#   Input :             Name of Directory
#   Description :       Deletes all duplicate files periodically
#   Date :              03/08/2026  
#   Author :            Saniya Siraj Pathan
#
##########################################################

def DeleteDuplicate(MyDict, fobj):
    try:
        Border = "-"*30

        # MyDict = FindDuplicate(DirectoryName, fobj)
        
        Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

        fobj.write("Total duplicate files found: %d" %len(Result))

        count = 0
        totalDeleted = 0

        fobj.write("Paths of deleted duplicate files")

        for value in Result:

            for subvalue in value:
        
                count = count + 1

                if count > 1:
                    totalDeleted = totalDeleted + 1
                    fobj.write(subvalue)
                    os.remove(subvalue)

                    for key, values in MyDict.items():
                        # print("Check = ",key, values)
                        for val in values:
                            if val == subvalue:
                                checksum = key
                                print("checksum of file:", subvalue, checksum)
                    
            count = 0

        fobj.write("Total number of deleted files is: %d" %totalDeleted)
        # print("totalDeleted: ",totalDeleted)   

    except Exception as e:
        fobj.write("Exception occured during execution: %d" %str(e))