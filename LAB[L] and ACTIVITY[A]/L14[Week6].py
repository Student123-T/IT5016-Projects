"""
Author:Tanmmey Arora
"""
class Person():
    def __init__(self,name,age):
        self.name= name
        self.age= age

    def great(self):
        print(f"Hello, my name is {self.name} and i am {self.age} year old.")


person1= Person ("James", 18)
person1.great()

class rectangle():
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width *self.height
    
    def perimeter(self):
        return 2*(self.width+self.height)

rec= rectangle(5,4)
print(f"Area:{rec.area()}")
print(f"Perimeter:{rec.perimeter()}")

class car():
    def __init__(self,color,model,year):
        self.color=color
        self.model=model
        self.year=year
Car1= car("Black","Tesla Model 5",1971)
print(f"Color:{Car1.color}")
print(f"Model:{Car1.model}")
print(f"Year:{Car1.year}")

class car():
    def __init__(self,color,model,year):
        self.color=color
        self.model=model
        self.year=year

    def drive(self):
        print(f"The {self.color} {self.model} is driving.")

    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")

    def car_info(self):
        print(f"Car info:{self.year} White BMW.")

Car1= car("RED","Supra",2003)
Car2= car("WHITE","BMW",1985)

Car1.drive()
Car2.stop()
Car2.car_info()
