import os
import pickle

#import data.pkl

data_file_path = os.path.join(os.path.dirname(__file__), "dataCar.pkl" )##

class Car:
    def __init__(self, model, brand, year, price):
        self.__model = model
        self.__brand = brand
        self.__year = year
        self.__price = price

    def return_car_brand(self):
        return self.__brand
    def return_car_model(self):
        return self.__model
    def return_car_year(self):
        return self.__year
    def return_car_price(self):
        return self.__price
    
    def __str__(self):
        return (f'Model: {self.__model}, {self.__brand}, production year:{self.__year}, price:{self.__price}')

class CarStore_list:
    def __init__(self):
        self.List_Car = []

    def __str__(self) -> str:
        return f'List of available cars'

    def add_car(self,car):
        self.List_Car.append(car)

    def remove_car(self,car):
        if car in self.List_Car:
            self.List_Car.remove(car)
        else:
            pass

    def input_car_from_file(self):
        with open(data_file_path, "rb") as file_in: 
            self.List_Car = pickle.load(file_in)

    def save_car_data(self):
        with open(data_file_path, "wb") as file_out:
            pickle.dump(self.List_Car,file_out)

    def display_cars(self):
        if len(self.List_Car) == 0:
            return f'No car exist'
        else:
            for car in self.List_Car:
                print(f"{car.return_car_model()}, {car.return_car_brand()}")