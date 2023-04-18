from Manage_Carstore import *
from Manage_Car_buy import *
from Manage_Customer import*
from Manage_Receipt import *

from tkinter import *
import os

icon_file_path = os.path.join(os.path.dirname(__file__), "car.png"  )

window = Tk()
window.geometry("700x600")
window.title("Car store management.")

icon = PhotoImage(file = icon_file_path)
window.iconphoto(True,icon)

title_label = Label(window,text='CAR STORE MANAGEMENT PROGRAM', bd=44,font=("Times New Roman",25,'bold'))
title_label.pack(side=TOP)

button_frame = Frame(window)
button_frame.pack()

# BUTTONS

button = Button(button_frame, text="Car storage list",font=("Arial",18),relief=RAISED,bd=5, 
                width=20, height=3,fg="white",bg="#1A237E",command=carstore_edit)
button.grid(row=0, column=0)

button2 = Button(button_frame, text="Customer list",font=("Arial",18),relief=RAISED,bd=5, 
                width=20, height=3,fg="white",bg="#1A237E", command=customer_manager)
button2.grid(row=1, column=0)

button1 = Button(button_frame, text="Buy a car ",font=("Arial",18),relief=RAISED,bd=5, 
                width=20, height=3,fg="white",bg="#1A237E",command=Receipt_manage)
button1.grid(row=2, column=0)

button3 = Button(button_frame, text="Receipt list ",font=("Arial",18),relief=RAISED,bd=5, 
                width=20, height=3,fg="white",bg="#1A237E",command=Receipt_management)
button3.grid(row=3, column=0)

window.mainloop()