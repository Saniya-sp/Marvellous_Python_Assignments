"""Voting ELigibility Checker
Devlop a Tkinter application that accepts a person's name and age.
Provide a Check Eligibility button to determmine whether the person is eligible to vote based on the minimum age of 18 years
""" 

import tkinter as tk

root = tk.Tk()  #window/gui starts

root.title("Voting ELigibility Checker")
root.geometry("400x300")    #width x height

tk.Label(root, text="Marvellous Infosystems",
         font=("Arial",18,"bold")).pack(pady=10)    #pady=padding in pixcels

tk.Label(root, text="Enter person's name").pack()    #pack acts as .add
entry1 = tk.Entry(root) #text field as input
entry1.pack()

tk.Label(root, text="Enter person's age").pack()    #pack acts as .add
entry2 = tk.Entry(root) #text field as input
entry2.pack()

def CheckEligibility():

    name = entry1.get().strip()
    age = entry2.get().strip()

    if int(age) > int(18):
        labelResult.config(text=f"{name} Is Eligible For Voting")
    else:
        labelResult.config(text=f"{name} Is Not Eligible For Voting")


tk.Button(root, text="Check Eligibility", command=CheckEligibility).pack(pady=15)  #calls Addition function

labelResult = tk.Label(root, text="", font=("Ariel", 14))
labelResult.pack()

root.mainloop()