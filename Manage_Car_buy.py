from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from Class_CarStr import *
from Class_Customer import *
from Class_Receipt import *
import os
import pickle

def Receipt_manage():

    current_dir = os.path.dirname(os.path.abspath(__file__))
    store = CarStore_list()
    customerS = customer_List()
    RE_List = Receipt_list()

    def OpenCarfile():
        data_file_path = filedialog.askopenfilename(initialdir=current_dir)
        with open(data_file_path, "rb") as file_in: ###
            store.List_Car = pickle.load(file_in)
            # print(store.List_Car[0])
        options = []
        for i in store.List_Car:
            options.append(i.return_car_brand())
        cboChooseCar.config(values=options)

    def OpenCustomerFile():
        data_file_path = filedialog.askopenfilename(initialdir=current_dir)
        with open(data_file_path, "rb") as file_in1: ###
            customerS.Customer_list = pickle.load(file_in1)
        options = []
        for i in customerS.Customer_list:
            options.append(i.return_customer_name())
        txtnameCus.config(values=options)
    
    def clickcustomer(event):
        index = txtnameCus.current()
        # print(index)
        global customer_choose
        customer_choose = customerS.Customer_list[index]
        a = str(customerS.Customer_list[index].return_customer_address())
        b = str(customerS.Customer_list[index].return_customer_dob())
        c = str(customerS.Customer_list[index].return_customer_contact())

        txtCusAdress.config(state=NORMAL)
        txtCusAdress.delete(0,END)
        txtCusAdress.insert(0,a)
        txtCusAdress.config(state="readonly")

        txtCusDob.config(state=NORMAL)
        txtCusDob.delete(0,END)
        txtCusDob.insert(0,b)
        txtCusDob.config(state="readonly")

        txtCusContact.config(state=NORMAL)
        txtCusContact.delete(0,END)
        txtCusContact.insert(0,c)
        txtCusContact.config(state="readonly")

    def clickChooseCar(event):
        index = cboChooseCar.current()
        # print(cboChooseCar.current())
        
        global carChoose
        carChoose = store.List_Car[index]
        a = str(store.List_Car[index].return_car_model())
        b = str(store.List_Car[index].return_car_year())
        c = str(store.List_Car[index].return_car_price())

        cboCarBrand.config(state=NORMAL)
        cboCarBrand.delete(0,END)
        cboCarBrand.insert(0,a)
        cboCarBrand.config(state="readonly")

        CarP_Year.config(state=NORMAL)
        CarP_Year.delete(0,END)
        CarP_Year.insert(0,b)
        CarP_Year.config(state="readonly")

        txtcarPrice.config(state=NORMAL)
        txtcarPrice.delete(0,END)
        txtcarPrice.insert(0,c)
        txtcarPrice.config(state="readonly")

# Home window
    root = Tk()
    root.geometry("1352x650+0+0")
    root.title("Car Store Information Management System")
    root.configure(background="black")
    root.resizable(width=False, height=False)

    menubar = Menu(root)
    root.config(menu=menubar)

    File_Menu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Data import",menu=File_Menu)
    File_Menu.add_command(label="Car data",command=OpenCarfile)
    File_Menu.add_command(label="Customer data",command=OpenCustomerFile)

    Tops = Frame(root, width=1350, height=100, bd=4)
    Tops.pack(side=TOP) 

    lblInfo = Label(Tops, font=('arial', 35, 'bold'), text = "Car buying interface", bd=5, anchor='w')
    lblInfo.grid(row=0, column=0)
    #Label
    bottom = Frame(root, width=1350, height=600, bd=4)
    bottom.pack(side=TOP)   

    bottomLeft = Frame(bottom, width=1000, height=500, bd=4, relief="raise")
    bottomLeft .pack(side=LEFT) 

    #Bottom Left
    #
    bottomLeftTop = Frame(bottomLeft, width=1000, height=300, bd=2, relief="raise")
    bottomLeftTop .pack(side=TOP)

    bottomLeftTopL = Frame(bottomLeftTop, width=500, height=300, bd=2, relief="raise")
    bottomLeftTopL .pack(side=LEFT)  

    #
    bottomLeftBottom = Frame(bottomLeft, width=1000, height=300, bd=2, relief="raise")
    bottomLeftBottom .pack(side=BOTTOM) 

    bottomLeftBottomL = Frame(bottomLeftBottom, width=500, height=500, bd=2, relief="raise")
    bottomLeftBottomL .pack(side=LEFT) 

    #Bottom right
    bottomRight = Frame(bottom, width=650, height=600, bd=4, relief="raise")
    bottomRight .pack(side=RIGHT)

    bottomRightTop = Frame(bottomRight, width=650, height=475, bd=2, relief="raise")
    bottomRightTop .pack(side=TOP)

    bottomRightbottom = Frame(bottomRight, width=650, height=400, bd=2, relief="raise")
    bottomRightbottom .pack(side=BOTTOM)

#Customers Information

    lblname = Label(bottomLeftTopL, font=('arial', 17, 'bold'), text="Customer's Information", fg="black", width= 20,borderwidth=15, anchor='w')
    lblname.grid(row=0, column=1)

    lblname = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Name", fg="black", width= 15,borderwidth=10, anchor='w')
    lblname.grid(row=1, column=0)
    txtnameCus = ttk.Combobox(bottomLeftTopL,state='readonly', font=('arial', 16, 'bold'), width=23,justify='left')
    txtnameCus.bind("<<ComboboxSelected>>",clickcustomer)
    txtnameCus.grid(row=1, column=1)

    lblname = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Address", fg="black", width= 15,borderwidth=10, anchor='w')
    lblname.grid(row=2, column=0)
    txtCusAdress = Entry(bottomLeftTopL,state='readonly', font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left')
    txtCusAdress.grid(row=2, column=1)

    lblname = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Date of birth", fg="black", width= 15,borderwidth=10, anchor='w')
    lblname.grid(row=3, column=0)
    txtCusDob = Entry(bottomLeftTopL,state='readonly', font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left')
    txtCusDob.grid(row=3, column=1)

    lblname = Label(bottomLeftTopL, font=('arial', 16, 'bold'), text="Contact", fg="black", width= 15,borderwidth=10, anchor='w')
    lblname.grid(row=4, column=0)
    txtCusContact = Entry(bottomLeftTopL,state='readonly', font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left')
    txtCusContact.grid(row=4, column=1)

    lblname = Label(bottomLeftTopL, font=('arial', 2, 'bold'), text="", fg="black", width= 15,height=3, anchor='w')
    lblname.grid(row=5, column=0)

#Cars Information

    lblcarPrice = Label(bottomLeftBottomL, font=('arial', 2, 'bold'), text="", fg="black", width= 15,height=0, anchor='w')
    lblcarPrice.grid(row=0, column=0)

    lblcar = Label(bottomLeftBottomL, font=('arial', 18, 'bold'), text=" Car's Information", fg="black", width= 15,bd=11, anchor='w')
    lblcar.grid(row=1, column=1)

    lblChooseCar = Label(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Name", fg="black", width= 15,bd=15, anchor='w')
    lblChooseCar.grid(row=2, column=0)
    cboChooseCar = ttk.Combobox(bottomLeftBottomL,state='readonly', font=('arial', 13, 'bold'), width=30)
    cboChooseCar.bind("<<ComboboxSelected>>",clickChooseCar)
    cboChooseCar.grid(row=2, column=1)

    lblcarBrand = Label(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Brand", fg="black", width= 15,bd=9, anchor='w')
    lblcarBrand.grid(row=3, column=0)
    cboCarBrand = Entry(bottomLeftBottomL,state='readonly', font=('arial', 16, 'bold'),bd=2,bg="white", width=24,justify='left')
    cboCarBrand.grid(row=3, column=1)

    lblcar = Label(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Produce Year", fg="black", width= 15,bd=10, anchor='w')
    lblcar.grid(row=4, column=0)
    CarP_Year = Entry(bottomLeftBottomL,state='readonly', font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left')
    CarP_Year.grid(row=4, column=1)

    lblcarPrice = Label(bottomLeftBottomL, font=('arial', 16, 'bold'), text="Car Price ($)", fg="black", width= 15,bd=10, anchor='w')
    lblcarPrice.grid(row=5, column=0)
    txtcarPrice = Entry(bottomLeftBottomL,state='readonly', font=('arial', 16, 'bold'), bd=2, width=24, bg="white", justify='left')
    txtcarPrice.grid(row=5, column=1)

    lblcarPrice = Label(bottomLeftBottomL, font=('arial', 16, 'bold'), text="", fg="black", width= 15,height=22 ,bd=19, anchor='w')
    lblcarPrice.grid(row=6, column=0)
    
    #Reset function
    def Reset():
        txtReceipt.config(state=NORMAL)
        txtReceipt.delete("1.0",END)
        txtReceipt.config(state=DISABLED)

    #print receipt function
    def ReceiptPrint():
        txtReceipt.config(state=NORMAL)
        txtReceipt.delete("1.0",END)
        txtReceipt.insert(END,"\n")
        txtReceipt.insert(END,"Items\t\t\t\t\t"+"Cost of Items\n\n")
        txtReceipt.insert(END,"____________________________________________________" "\n")
        txtReceipt.insert(END,"\n")
        txtReceipt.insert(END,"Customer Name: \t\t\t\t\t"+ txtnameCus.get()+ "\n")
        txtReceipt.insert(END,"Customer Address: \t\t\t\t\t"+ txtCusAdress.get()+ "\n")
        txtReceipt.insert(END,"Customer Date of Birth: \t\t\t\t\t"+ txtCusDob.get()+ "\n")
        txtReceipt.insert(END,"Customer Contact: \t\t\t\t\t"+ txtCusContact.get()+ "\n")
        txtReceipt.insert(END,"\n")
        txtReceipt.insert(END,"____________________________________________________" "\n")
        txtReceipt.insert(END,"\n")
        txtReceipt.insert(END,"Car Name: \t\t\t\t\t"+  cboChooseCar.get()+ "\n")
        txtReceipt.insert(END,"Car Brand: \t\t\t\t\t"+  cboCarBrand.get()+ "\n")
        txtReceipt.insert(END,"Car Price: \t\t\t\t\t"+ "$"+txtcarPrice.get()+ "\n")
        txtReceipt.insert(END,"Production year: \t\t\t\t\t"+  CarP_Year.get()+ "\n")
        txtReceipt.insert(END,"\n")
        txtReceipt.insert(END,"____________________________________________________" "\n")
        txtReceipt.config(state=DISABLED)

        try:
            data_file_path = os.path.join(os.path.dirname(__file__), "data_Receipt.pkl" )
            with open(data_file_path,"rb") as file__in:
                RE_List.aList = pickle.load(file__in)
            re1 = Receipt(customer_choose,carChoose)
            RE_List.aList.append(re1)
            RE_List.save_RE_list()

        except FileNotFoundError:
            print('Receipt file data not exist')
            re1 = Receipt(customer_choose,carChoose)
            RE_List.aList = []
            RE_List.aList.append(re1)
            RE_List.save_RE_list()

#Buttons
    Button1=Button(root,width=6, text="Reset" , font=('arial', 15, 'bold'),fg="black", bd= 2, command=Reset)
    Button1.place(x = 705, y =590)

    Button2=Button(root,width=6, text="Receipt" , font=('arial', 15, 'bold'),fg="black", bd= 2, command=ReceiptPrint)
    Button2.place(x = 827, y =590)

#Receipt board
    lblReceipt = Label(bottomRightTop, font=('arial', 16, 'bold'), text='Receipt', bd=2, anchor='w')
    lblReceipt.grid(row=0, column=0, sticky=W)
    txtReceipt = Text(bottomRightTop,state=DISABLED, font=('arial', 11, 'bold'), bd=8, width=60,height=25, bg='white')
    txtReceipt.grid(row=1, column=0)

    root.mainloop()