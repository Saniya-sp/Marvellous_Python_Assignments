"""Find the Largest Number
Devlop a Tkinter application that accepts three numbers from the user.
Provide a Finf Maximum button to determine and display the largest number.
"""
 
import tkinter as tk

root = tk.Tk()  #window/gui starts

root.title("Find the Largest Number")
root.geometry("400x300")    #width x height

tk.Label(root, text="Marvellous Infosystems",
         font=("Arial",18,"bold")).pack(pady=10)    #pady=padding in pixcels

tk.Label(root, text="Enter First Number").pack()    #pack acts as .add
entry1 = tk.Entry(root) #text field as input
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()    #pack acts as .add
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Enter Third Number").pack()    #pack acts as .add
entry3 = tk.Entry(root)
entry3.pack()

def LargestNo():
    no1 = int(entry1.get())
    no2 = int(entry2.get())
    no3 = int(entry3.get())

    if no1 > no2:
        if no1 > no3:
            largest = no1
        else:
            largest = no3
    else:
        largest = no2

    labelResult.config(text="Largest Number Is : "+ str(largest))

tk.Button(root, text="Largest Number Is", command=LargestNo).pack(pady=15)  #calls Addition function

labelResult = tk.Label(root, text="", font=("Ariel", 14))
labelResult.pack()

root.mainloop()