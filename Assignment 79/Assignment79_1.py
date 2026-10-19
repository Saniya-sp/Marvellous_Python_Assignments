"""
Addition of Two Numbers
Devlop a Tkinter application that accepts two numbers using Entry widgets.
Provide an Add button to calculate and display the addition using a Label widget.
""" 

import tkinter as tk

root = tk.Tk()  #window/gui starts

root.title("Marvellous Addition Calculator")
root.geometry("400x300")    #width x height

tk.Label(root, text="Marvellous Infosystems",
         font=("Arial",18,"bold")).pack(pady=10)    #pady=padding in pixcels

tk.Label(root, text="Enter First Number").pack()    #pack acts as .add
entry1 = tk.Entry(root) #text field as input
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()    #pack acts as .add
entry2 = tk.Entry(root)
entry2.pack()

def Addition():
    no1 = int(entry1.get())
    no2 = int(entry2.get())

    result = no1 + no2

    labelResult.config(text="Addition is : "+ str(result))


tk.Button(root, text="Addition", command=Addition).pack(pady=15)  #calls Addition function

labelResult = tk.Label(root, text="", font=("Ariel", 14))
labelResult.pack()

root.mainloop()