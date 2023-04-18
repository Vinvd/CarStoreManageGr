from tkinter import *
from tkinter import filedialog
from Class_CarStr import *
import pickle
import os

# store = CarStore()
# store.output_car_data()
# store.add_car_from_file()

# print(store.List_Car[0])
# store.output_car_data()

def carstore_edit():
    store = CarStore_list()
    current_dir = os.path.dirname(os.path.abspath(__file__))

    def summit():
        selected = Listbox_car.curselection()
        print(selected)
        for index in selected:
            car = store.List_Car[index]
            out = f'Model: {car.return_car_model()}'
            out2 = f'Brand: {car.return_car_brand()}'
            out3 = f'Production year: {car.return_car_year()}'
            out4 = f'Price: {car.return_car_price()}'
            label2_frame2.delete(0, END)  # clear any previous text
            label2_frame2.insert(END, f"{out}, {out2}, {out3}, {out4}")

    def delete():
        selected = Listbox_car.curselection()
        print(selected)
        for index in selected:
            store.remove_car(store.List_Car[index])
            Listbox_car.delete(0,END)
            for index1, car in enumerate(store.List_Car):
                info = f'{car.return_car_model()}, {car.return_car_brand()}'
                Listbox_car.insert(index1, info)

    def add():
        add_car_window  = Toplevel()
        add_car_window.title("Add car")
        add_car_model = Label(add_car_window,text="car module:",font=("Arial",15)).grid(row=0,column=0)
        add_car_brand = Label(add_car_window,text="car brand:",font=("Arial",15)).grid(row=1,column=0)
        add_car_year = Label(add_car_window,text="car year:",font=("Arial",15)).grid(row=2,column=0)
        add_car_price = Label(add_car_window,text="car price:",font=("Arial",15)).grid(row=3,column=0)

        entry_model = Entry(add_car_window,bd=2,font=("Arial",13))
        entry_model.grid(row=0,column=1)
        entry_brand = Entry(add_car_window,bd=2,font=("Arial",13))
        entry_brand.grid(row=1,column=1)
        entry_year = Entry(add_car_window,bd=2,font=("Arial",13))
        entry_year.grid(row=2,column=1)
        entry_price = Entry(add_car_window,bd=2,font=("Arial",13))
        entry_price.grid(row=3,column=1)

        def apply():
            model = entry_model.get()
            brand = entry_brand.get()
            year =  entry_year.get()
            price = entry_price.get()
            car_new =Car(model,brand,year,price)
            store.add_car(car_new)
            Listbox_car.delete(0,END)
            for index1, car in enumerate(store.List_Car):
                info = f'{car.return_car_model()}, {car.return_car_brand()}'
                Listbox_car.insert(index1, info)
            add_car_window.destroy()
    
        button_add = Button(add_car_window,text="apply",command=apply).grid(row=4)

    def Openfile():
        data_file_path = filedialog.askopenfilename(initialdir=current_dir)
        with open(data_file_path, "rb") as file_in: 
            store.List_Car = pickle.load(file_in)
            Listbox_car.delete(0,END)
            for index, car in enumerate(store.List_Car):
                info = f'{car.return_car_model()}, {car.return_car_brand()}'
                Listbox_car.insert(index, info)

    def SaveFile():
        store.save_car_data()
        notice = Toplevel()
        a = Label(notice,text='Done save file').pack()


    window = Tk()
    # window.geometry('1500x750')
    window.title("Car store management.")

    menubar = Menu(window)
    window.config(background = "light yellow",menu=menubar)

    File_Menu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=File_Menu)
    File_Menu.add_command(label="Open",command=Openfile)
    File_Menu.add_command(label="Save",command=SaveFile)
   

    # frame 1
    frame1 = Frame(window, borderwidth=5,relief=SUNKEN)
    frame1.grid(row=0,column=0,padx=10, pady=10)

    Listbox_car_label=Label(frame1,text='Current inventory:').grid(row=0,column=0)


    Listbox_car = Listbox(frame1,bg="#ECEFF1",fg="#424242",font=("Arial",15),width=30,height=15)
    Listbox_car.grid(row=1, column=0, sticky="nsew")

    for index, car in enumerate(store.List_Car):
        info = f'{car.return_car_model()}, {car.return_car_brand()}'
        Listbox_car.insert(index, info)

    scrollbar = Scrollbar(frame1)
    scrollbar.grid(row=1, column=1, sticky="ns")
    Listbox_car.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=Listbox_car.yview)

    button_frame = Frame(frame1)
    button_frame.grid(row=2,column=0)

    Summit_button = Button(button_frame,text="Detail",padx=2,command=summit)
    Summit_button.grid(row=0,column=0)

    delete_button = Button(button_frame,text='Delete',padx=2,command=delete)
    delete_button.grid(row=0,column=1)

    add_button = Button(button_frame,text='Add',padx=2, command=add)
    add_button.grid(row=0,column=2)

    # frame 2
    frame2 =Frame(window,borderwidth=5,relief=SUNKEN)
    frame2.grid(row=1,column=0,padx=10, pady=10)


    label1_frame2 = Label(frame2, text="Car you selected:")
    label1_frame2.grid(row=0, column=0)

    label2_frame2 = Entry(frame2,width=70)
    label2_frame2.grid(row=1, column=0)

    window.mainloop()
