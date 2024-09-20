"""
Author:Tanmmey Arora
"""
class UnstructedCode:
    def xyzz(self,a,b):
        result=a+b
        print(f"Result:{result}")
class Calculator:
    def add(self,a,b):
        result=a+b
        print(f"Addition Result:{result}")
    def mul(self,a,b):
        result=a*b
        print(f"Multiplication Result:{result}")
def legacy_function(x,y):
    r=x+y
    print(f"Result:{r}")
class InflexibleShape:
    def calculate_area(self):
        pass
class Circle(InflexibleShape):
    def calculate_area(self):
        pass
class Square(InflexibleShape):
    def calculate_area(self):
        pass

if __name__=="__main__":
    obj=UnstructedCode()
    obj.xyzz(5,10)
    calc=Calculator()
    calc.add(5,10)
    calc.mul(10,6)
    legacy_function(4,8)
    circle=Circle()
    square=Square()
