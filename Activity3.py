#Write a program to create a class parrot and preform the following task 1. create a class variable speices 2. create an __init__ method that has instance variables -name and age 3. create instances of class parrot, passing arguments as well 4.print class variable by accecing it 5. print instance variable as well
class parrot:
    speices = "Bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
# instantiate the parrot class 
blu = parrot("Blu", 10)
woo = parrot("Woo", 15)
#Access the class atributes 
print("Blu is a {}".format(blu.speices))
print("Woo is a {}".format(woo.speices))
#Access the instance attribute
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))