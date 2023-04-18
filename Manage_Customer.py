from Class_Customer import *
from tkinter import *
from tkinter import filedialog
import os

def customer_manager():
    customerS = customer_List()
    # print(customerS.Customer_list[0])
    current_dir = os.path.dirname(os.path.abspath(__file__))

    def summit():
        selected = Listbox_Customers.curselection()
        print(selected)
        for index in selected:
            select = customerS.Customer_list[index]
            a = f"{select.return_customer_name()}"
            b = f'{select.return_customer_dob()}'
            c = f"{select.return_customer_address()}"
            d = f"{select.return_customer_contact()}"
            label2_frame2.delete(0,END)
            label2_frame2.insert(END, f"Name: {a}, Dob: {b}, address: {c}, contact: {d}")

    def delete():
        selected = Listbox_Customers.curselection()
        print(selected)
        for index in selected:
            customerS.remove_customer(customerS.Customer_list[index])
        Listbox_Customers.delete(0,END)
        for index1, custMR in enumerate(customerS.Customer_list):
            info = f'{custMR.return_customer_name()}, {custMR.return_customer_address()}'
            Listbox_Customers.insert(index1, info)

    def add():
        add_custm_window = Toplevel()
        add_custm_window.title("Add customer")

        add_name = Label(add_custm_window,text="Name:",font=("Arial",15)).grid(row=0,column=0)
        add_Dob = Label(add_custm_window,text="Dob:",font=("Arial",15)).grid(row=1,column=0)
        add_address = Label(add_custm_window,text="Address:",font=("Arial",15)).grid(row=2,column=0)
        add_contact = Label(add_custm_window,text="Contact:",font=("Arial",15)).grid(row=3,column=0)

        entry_name = Entry(add_custm_window,bd=2,font=("Arial",13))
        entry_name.grid(row=0,column=1)
        entry_dob = Entry(add_custm_window,bd=2,font=("Arial",13))
        entry_dob.grid(row=1,column=1)
        entry_address = Entry(add_custm_window,bd=2,font=("Arial",13))
        entry_address.grid(row=2,column=1)
        entry_contact = Entry(add_custm_window,bd=2,font=("Arial",13))
        entry_contact.grid(row=3,column=1)

        def apply():
            a = entry_name.get()
            b = entry_dob.get()
            c = entry_address.get()
            d = entry_contact.get()
            new_customer = customer(a,b,c,d)
            customerS.add_customer(new_customer)
            Listbox_Customers.delete(0,END)
            for index, custMR in enumerate(customerS.Customer_list):
                info = f'{custMR.return_customer_name()}, {custMR.return_customer_address()}'
                Listbox_Customers.insert(index, info)
            add_custm_window.destroy()

        button_add = Button(add_custm_window,text="apply",command=apply).grid(row=4)

    def Openfile():
        data_file_path = filedialog.askopenfilename(initialdir=current_dir)
        with open(data_file_path, "rb") as file_in: 
            customerS.Customer_list = pickle.load(file_in)
        Listbox_Customers.delete(0,END)
        for index, custMR in enumerate(customerS.Customer_list):
            info = f'{custMR.return_customer_name()}, {custMR.return_customer_address()}'
            Listbox_Customers.insert(index, info)

    def SaveFile():
        customerS.save_customer_data()
        notice = Toplevel()
        a = Label(notice,text='Done save file').pack()

    window = Tk()
    window.title("Customers management.")
    menubar = Menu(window)
    window.config(background = "light yellow",menu=menubar)

    File_Menu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=File_Menu)
    File_Menu.add_command(label="Open",command=Openfile)
    File_Menu.add_command(label="Save",command=SaveFile)

    # frame 1
    frame1 = Frame(window, borderwidth=5,relief=SUNKEN)
    frame1.grid(row=0,column=0,padx=10, pady=10)

    Listbox_Cust=Label(frame1,text='List of all customers').grid(row=0,column=0)

    Listbox_Customers = Listbox(frame1,bg="light pink",fg="black",font=("Arial",15),width=30,height=15)
    Listbox_Customers.grid(row=1, column=0, sticky="nsew")

    for index, custMR in enumerate(customerS.Customer_list):
        info = f'{custMR.return_customer_name()}, {custMR.return_customer_address()}'
        Listbox_Customers.insert(index, info)

    scrollbar = Scrollbar(frame1)
    scrollbar.grid(row=1, column=1, sticky="ns")
    Listbox_Customers.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=Listbox_Customers.yview)


    button_frame = Frame(frame1)
    button_frame.grid(row=2,column=0)

    Summit_button = Button(button_frame,text="Detail",padx=2,command=summit)
    Summit_button.grid(row=0,column=0)

    delete_button = Button(button_frame,text='Delete',padx=2,command=delete)
    delete_button.grid(row=0,column=1)

    add_button = Button(button_frame,text='Add',padx=2,command=add)
    add_button.grid(row=0,column=2)

    frame2 =Frame(window,borderwidth=5,relief=SUNKEN)

    frame2.grid(row=1,column=0,padx=10, pady=10)
    label1_frame2 = Label(frame2, text="Details:")
    label1_frame2.grid(row=0, column=0)

    label2_frame2 = Entry(frame2,width=70)
    label2_frame2.grid(row=1, column=0)

    window.mainloop()