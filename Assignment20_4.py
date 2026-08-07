"""Design a Python Appl that creates three thresds named Small, Capital and Digits.
All threads should accept string as a input.
The Small thread should count and display the number of lowercase characters
The Capital thread should count and display the number of uppercase characters
The Digits thread should count and display the number of numeric digits
Each thread must also display:
    Thread ID
    Thread Name
"""

import time
import threading

def Small(str_ip):
    print("TID of Small thread is :",threading.get_ident())

    count = 0
    for n in str_ip:
        # print('n small ', n, n.islower())
        if n.islower():
            count+=1
    
    print('Small count = ',count)
    

def Capital(str_ip):
    print("TID of Capital thread is :",threading.get_ident())

    count = 0
    for n in str_ip:
        # print('n cap ', n, n.isupper())

        if n.isupper():
            count+=1
    
    print('Capital count = ',count)
    

def Digit(str_ip):
    print("TID of Digit thread is :",threading.get_ident())
    count = 0
    for n in str_ip:
        # print('n dig ', n, n.isdigit())
        if n.isdigit():
            count+=1
    
    print('Digit count = ',count)
    

def main():
    print("TID of Main thread is :",threading.get_ident())

    str_ip = str(input("Enter string: "))
    
    start_ime = time.perf_counter()
    
    tobj1 = threading.Thread(target=Small, args=(str_ip,))
    tobj2 = threading.Thread(target=Capital, args=(str_ip,))
    tobj3 = threading.Thread(target=Digit, args=(str_ip,))
    
    tobj1.start()
    tobj1.join()

    tobj2.start()
    tobj2.join()
    
    tobj3.start()
    tobj3.join()

    print("Exit from main")
    end_ime = time.perf_counter()

    print(f"Total time: {end_ime-start_ime:.4f} seconds")
    
if __name__ == "__main__":
    main()