# Define a parent class called "Vehicle"
class Vehicle:
    def __init__(self, color):
        self.color = color
    
    def honk(self):
        print("Honk honk!")

# Define a child class called "Car" that interacts from Vechile
class Car(Vehicle):
    def __init__(self, color, speed):
        super().__init__(color)
        self.speed = speed
    
    def accelerate(self):
        self.speed += 10

# Create an object (instance) of the Car class
my_car = Car("red", 60)
my_car.honk() # Output: Honk honk!