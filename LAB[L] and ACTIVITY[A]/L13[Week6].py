"""
Author:Tanmmey Arora
"""
#Q1 
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
        print(f"Car info:{self.year}, {self.color}, {self.model}.")

class Electric_car(car):
    def __init__(self,color,model,year,battery_capacity):
        super().__init__(color,model,year)
        self.battery_capacity=battery_capacity

    def car_info(self):
        super().car_info()
        print(f"Battery Capapcity: {self.battery_capacity}Kmp")

my_Electric_Car= Electric_car("Black","Konisec",2023,200)
my_Electric_Car.drive()
my_Electric_Car.stop()
my_Electric_Car.car_info()

#Q2
class Account():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.__balance= balance

    def deposite(self,amount):
        if amount>0:
            self.__balance += amount
            print(f"${amount} deposited.")
        else:
            print("Deposite amount must be positive.")
        
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn.")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance
    
acc= Account("James", 100)
print(acc.owner)

acc.deposite(50)
print(acc.get_balance())

acc.withdraw(75)
print(acc.get_balance())
