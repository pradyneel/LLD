from abc import ABC, abstractmethod

# An abstract product (the interface)
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

# Concreate Products (Implements the interface)
class Sedan(Car):
    def drive(self):
        return "Driving a Sedan"

class SUV(Car):
    def drive(self):
        return "Driving an SUV"

# Factory
class CarFactory:
    @staticmethod
    def create_car(car_type: str) -> Car:
        if car_type == 'Sedan':
            return Sedan()
        elif car_type == 'SUV':
            return SUV()
        else:
            raise ValueError(f'Unknown car type: {car_type}')

# Client code
if __name__ == '__main__':
    car_type = input('Enter the type of car you want to create (Sedan/SUV)')
    try:
        car = CarFactory.create_car(car_type)
    except ValueError as e:
        print(e)