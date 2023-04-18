import os
import pickle

data_file_path = os.path.join(os.path.dirname(__file__), "dataCustomer.pkl" )##

class customer():
    def __init__(self,name,dob,address,contact):
        self.__name = name
        self.__dob = dob
        self.__address = address
        self.__contact = contact

    def return_customer_name(self):
        return self.__name
    def return_customer_dob(self):
        return self.__dob
    def return_customer_address(self):
        return self.__address
    def return_customer_contact(self):
        return self.__contact
    
    def __str__(self) -> str:
        return f'Name: {self.__name}, address: {self.__address}, contact: {self.__contact}.'

class customer_List():
    def __init__(self):
        self.Customer_list = []

    def __str__(self) -> str:
        return f'Customer List'

    def add_customer(self,customer):
        self.Customer_list.append(customer)

    def remove_customer(self,customer):
        if customer in self.Customer_list:
            self.Customer_list.remove(customer)
        else:
            pass

    def save_customer_data(self):
        with open(data_file_path, "wb") as file_out:
            pickle.dump(self.Customer_list,file_out)

    def input_customer_from_file(self):
        with open(data_file_path, "rb") as file_in:
            self.Customer_list = pickle.load(file_in)