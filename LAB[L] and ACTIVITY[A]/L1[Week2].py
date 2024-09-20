"""
Author:Tanmmey Arora
"""
# Q1
Name=str(input("Enter your Name: "));
Birth_Year=int(input("Enter your Birth Year: "));
Current_Year=int(input("Enter Current Year: "));
Age=(Current_Year - Birth_Year)
print("Name is: ",Name)
print("Birth Year is: ",Birth_Year)
print("Age is: ",Age)

#Q2
a=42
b=3.14
c="Hello World!"
d=[1,2,3]
e=(1,2,3)
f={"name":"John","Age":30}

# part a)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))


# part c)
import math
b_exp= math.exp(b)
print(b_exp)

# part d)
print(a%b) # Remainder

# part e)
Add=a+5
print("Addition is",Add)
Sub=a-10
print("Subtraction is:",Sub)
Mul=a*2
print("Multiplication is",Mul)
Div=a/7
print("Division is:",Div)

# part f)
print(c.upper())

# part b)
b="3.14"
print(type(b))

# part g)
a="42"
b="3.14"
print(a,type(a))
print(b,type(b))
print(a+b)

# part h)
print(c[::-1])