1. Project Title
    Duplicate File Removal Automation

2. Project Description
    This script will periodically scans a given directory. Then checksum of each file in the directory will be calculated and compared to check if the files have same chunks which means files are duplicates. If such files found, delete those files from directory. A logfile will always capture all the activities performed. And after completion of every periodic execution an email with logfile will be sent to the provided email address.

3. Features:
    -Recursive directory scanning
    -Checksum-based duplicate detection
    -Automatic duplicate file deletion
    -Timestamp based log generation
    -Periodic execution
    -Email notification
    -Log-file attachment
    Input validation
    -Exception handling
    -Modular programming

4. Requirements
    -Supported python version: 3.0+
    -Required python libraries: 
        sys
        os
        time
        schedule
        datetime
        hashlib
    -Internet connection for sending email
    -Email application password or SMTP credentials

5. Project Sturcture:

    -Assignment33.py file
        This file is starter of appliacation and contains main function. Inside main funtion scheduler is configured to run application periodically.

    -DeleteDuplicateFilesModule.py:
        This module contains function such as CalculateChecksum, FindDuplicate, DeleteDuplicate.

6. Command Line options:
    Command: python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>
    DirectoryPath: Provide aboslute path of directory in double quotes
    IntervalInMinutes: Time in minutes to pass to scheduler.
    ReceiverEmail: Email id of receiver on which statistics of execution will be sent.

7. Execution command:
    -python DuplicateFileRemoval.py E:/Data/Demo 50 pathansaniya00@gmail.com

8. Help command:
    -python DuplicateFileRemoval.py --h

9. Usage command:
    -python DuplicateFileRemoval.py --u

10. Log-file information:
    -Log files will be stored in Marvellous directory. File name will be "DuplicateRemovalLog_%s.log"%(timestamp) 

11. Email configuration:
    ## Explain how sender email credentials should be configured securely

12. Important notes:

    -Deleted files may not be recoverable.
    -Testing should first be performed on a sample directory.
    -Email passwords should not be hard-coded.
    -The first file from each duplicate group should be preserved.
    -Files should be considered duplicates only when their checksums are identical.


