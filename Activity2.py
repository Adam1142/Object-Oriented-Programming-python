#Write a program to create a class vehicle and perform the following task 1. create an __init__ method with arguments and parameter- max_speed, mileage 2. create an object of class vehicle and pass the maximum speed and mileage of the car 3. print the value of max_speed and mileage by using the object
class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX = vehicle(240,80)
print("Model Max Speed", modelX.max_speed)
print("Mpdel Mileage", modelX.mileage)