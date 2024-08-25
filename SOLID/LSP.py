class Vehicle:
    def start(self):
        raise NotImplementedError

class Car(Vehicle):
    def start(self):
        print("Starting the car engine...")

class Bicycle(Vehicle):
    def start(self):
        print("Pedaling the bicycle...")