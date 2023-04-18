from Class_Receipt import *
from tkinter import *
from tkinter import filedialog
import os 

current_dir = os.path.dirname(os.path.abspath(__file__))

def Receipt_management():        
    RE_list = Receipt_list()
    # RE_list.input_re_list()

    def detail():
        selected = list_listBox.curselection()
        for index in selected:
            print(index)
            select =  RE_list.aList[index]
        new_window = Tk()
        new_window.title('Detailed informations')

        txtReceipt = Text(new_window,bd=8, width=35,height=20, bg='white',font=("Times New Roman",15))
        txtReceipt.grid(row=0,column=0)

        txtReceipt.delete('1.0',END)
        txtReceipt.insert(END,f'\n\n\n')
        txtReceipt.insert(END,f'    Customer detail:\n')
        txtReceipt.insert(END,f'        Name: {select.customer_name()}\n')
        txtReceipt.insert(END,f'        Dob: {select.customer_dob()}\n')
        txtReceipt.insert(END,f'        Address: {select.customer_address()}\n')
        txtReceipt.insert(END,f'        Contact: {select.customer_contact()}\n')
        txtReceipt.insert(END,f'\n')
        txtReceipt.insert(END,f'    Car purchased detail:\n')
        txtReceipt.insert(END,f'        Brand: {select.car_brand()}\n')
        txtReceipt.insert(END,f'        Model: {select.car_model()}\n')
        txtReceipt.insert(END,f'        Production year: {select.car_year()}\n')
        txtReceipt.insert(END,f'        Price: {select.car_price()}\n')

        new_window.mainloop()

    def delete():
        selected = list_listBox.curselection()
        for index in selected:
            RE_list.remove_receipt(RE_list.aList[index])
        list_listBox.delete(0,END)
        for i, iReceipt in enumerate(RE_list.aList):
            info = f'Customer: {iReceipt.customer_name()}, #Bought: {iReceipt.car_brand()}, {iReceipt.car_model()}'
            list_listBox.insert(i,info)

    def openfile():
        data_file_path = filedialog.askopenfilename(initialdir=current_dir)
        with open(data_file_path, "rb") as file_in:
            RE_list.aList = pickle.load(file_in)
        list_listBox.delete(0,END)
        for i, iReceipt in enumerate(RE_list.aList):
            info = f'Customer: {iReceipt.customer_name()}, #Bought: {iReceipt.car_brand()}, {iReceipt.car_model()}'
            list_listBox.insert(i,info)

    def savefile():
        RE_list.save_RE_list()
        notice = Toplevel()
        a = Label(notice,text='Done save file').pack()

    window = Tk()
    window.title('Receipts management')

    menubar = Menu(window)
    window.config(menu=menubar)

    File_Menu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=File_Menu)

    File_Menu.add_command(label="Open",command=openfile)
    File_Menu.add_command(label="Save",command=savefile)

    Frame1 = Frame(window)
    Frame1.grid(row=0, column=0)  # make Frame1 span across two columns

    Listbox_label = Label(Frame1,text='Receipt List',font=("Arial",15))
    Listbox_label.grid(row=0,column=0)

    list_listBox = Listbox(Frame1,bg="white",font=("Arial",15),width=38,height=15)
    list_listBox.grid(row=1,column=0,sticky="nsew")

    for i, iReceipt in enumerate(RE_list.aList):
        info = f'Customer: {iReceipt.customer_name()}, #Bought: {iReceipt.car_brand()}, {iReceipt.car_model()}'
        list_listBox.insert(i,info)

    scrollbar = Scrollbar(Frame1)
    scrollbar.grid(row=1, column=1, sticky="ns")
    list_listBox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=list_listBox.yview)

    buttonFrame = Frame(Frame1)
    buttonFrame.grid(row=2,column=0)

    Detail_button = Button(buttonFrame,text="Detail",padx=2,command=detail)
    Detail_button.grid(row=0,column=0)

    delete_button = Button(buttonFrame,text='Delete',padx=2,command=delete)
    delete_button.grid(row=0,column=1)

    window.mainloop()