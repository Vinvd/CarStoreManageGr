from Class_CarStr import *
from Class_Customer import *
import os
import pickle

data_file_path = os.path.join(os.path.dirname(__file__), "data_Receipt.pkl" )

class Receipt:
    def __init__(self, customer, car):
        self.__customer = customer
        self.__car = car

    def __str__(self) -> str:
        name = self.__customer._customer__name
        car = f'{self.__car._Car__brand}, {self.__car._Car__model}'
        return f'Customer: {name}, car purchased: {car}'
    
    def customer_name(self):
        return self.__customer.return_customer_name()
    def customer_dob(self):
        return self.__customer._customer__dob
    def customer_address(self):
        return self.__customer.return_customer_address()
    def customer_contact(self):
        return self.__customer._customer__contact
    def car_brand(self):
        return self.__car.return_car_brand()
    def car_model(self):
        return self.__car.return_car_model()
    def car_year(self):
        return self.__car._Car__year
    def car_price(self):
        return self.__car._Car__price

class Receipt_list():
    def __init__(self):
        self.aList = []

    def remove_receipt(self,a):
        if a in self.aList:
            self.aList.remove(a)
        else:
            pass


    def save_RE_list(self):
        with open(data_file_path, "wb") as file_out:
            pickle.dump(self.aList,file_out)
        
    def input_re_list(self):
        with open(data_file_path, "rb") as file_in:
            self.aList = pickle.load(file_in)
        # print(self.aList[0])

    def __str__(self) -> str:
        return f'This is a list of receipts'

# car1 = Car("Civic", "Honda", 2021, 20000)
# cust1 = customer("John", "01/01/2000", "123 Main St", "555-555-5555")
# receipt1 = Receipt(cust1, car1)
# print(receipt1.customer_name())
# print(receipt1)