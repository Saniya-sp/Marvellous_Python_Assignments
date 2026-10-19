"""Basic Login Form
Devlop a Tkinter application that accepts a username and password using Entry widgets.
Provide a Login button to validate the entered credentials against predefined values and display an appropriate success or failure message.
""" 

import tkinter as tk

root = tk.Tk()  #window/gui starts

root.title("Login Form")
root.geometry("400x300")    #width x height

tk.Label(root, text="Marvellous Infosystems",
         font=("Arial",18,"bold")).pack(pady=10)    #pady=padding in pixcels

tk.Label(root, text="Enter Username").pack()    #pack acts as .add
entry1 = tk.Entry(root) #text field as input
entry1.pack()

tk.Label(root, text="Enter Password").pack()    #pack acts as .add
entry2 = tk.Entry(root) #text field as input
entry2.pack()

user_name = 'SaniyaPathan'
Password = 'Abc12345'

def CheckLogin():

    username = entry1.get().strip()
    password = entry2.get().strip()

    if username != user_name:
        labelResult.config(text=f"Username is not matching with the predefined value")

    elif password != Password:
        labelResult.config(text=f"Password is not matching with the predefined value")
    else:
        labelResult.config(text=f"Logged in successfully!")


tk.Button(root, text="Login", command=CheckLogin).pack(pady=35)  #calls Addition function

labelResult = tk.Label(root, text="", font=("Ariel", 12))
labelResult.pack()

root.mainloop()