"""Write a program that accepts
    A message from the user
    A time interval in seconds

Schedule the program to display the message repeatedly after the specified interval
Example ip:
Enter message: Jay Ganesh
ENter interval in seconds: 5

Expected op:

Jay Ganesh
every five seconds

Validate that the interval is greater than zero
"""

import schedule
import time

    
def Display(message):
    print(message)

        
def main():

    message = input("Enter message: ")
    interval = int(input("Enter interval in seconds: "))
    # Validate interval
    if interval <= 0:
        print("Interval must be greater than zero.")
        return

    schedule.every(interval).seconds.do(Display, message)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()