"""Design a Python Appl that creates two thresds named Thread1 and Thread2.
Thread1 should display numbers from 1 to 50.
Thread2 should display numbers from 50 to 1 in reverse order.
Ensure that:
    Thread2 starts execution only after Thread1 has completed. 
Use appropriate thread synchronization.
"""

import time
import threading

def Thread1(str_ip):
    print("TID of Small thread is :",threading.get_ident())

    for n in range(50+1):
        print(n)
    

def Thread2(str_ip):
    print("TID of Capital thread is :",threading.get_ident())

    for n in range(50,0,-1):
        print(n)


def main():
    print("TID of Main thread is :",threading.get_ident())

    start_ime = time.perf_counter()
    
    tobj1 = threading.Thread(target=Thread1, args=(50,))
    tobj2 = threading.Thread(target=Thread2, args=(50,))
    
    tobj1.start()
    tobj1.join()

    tobj2.start()
    tobj2.join()
    

    print("Exit from main")
    end_ime = time.perf_counter()

    print(f"Total time: {end_ime-start_ime:.4f} seconds")
    
if __name__ == "__main__":
    main()