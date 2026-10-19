"""Area of Circle
Devlop a Tkinter application that accepts radius of a circle.
Provide a Calculate Area button to calculate and display the area of circle.
""" 

import tkinter as tk

root = tk.Tk()  #window/gui starts

root.title("Area of Circle")
root.geometry("400x300")    #width x height

tk.Label(root, text="Marvellous Infosystems",
         font=("Arial",18,"bold")).pack(pady=10)    #pady=padding in pixcels

tk.Label(root, text="Enter Radius of Circle").pack()    #pack acts as .add
entry = tk.Entry(root) #text field as input
entry.pack()

def AreaOfCircle():
    radius = entry.get()
    area =3.14 * int(radius)**2

    labelResult.config(text="Area of Circle Is : "+ str(area))

tk.Button(root, text="Area of Circle Is", command=AreaOfCircle).pack(pady=15)  #calls Addition function

labelResult = tk.Label(root, text="", font=("Ariel", 14))
labelResult.pack()

root.mainloop()
