"""
Author: Tanmmey arora
"""
def Addition():
  Num1=int(input("Enter The Number1:"))
  Num2=int(input("Enter The Number2:"))
  Add=Num1+Num2
  print("Addition is",Add)

def Subtraction():
  Num1=int(input("Enter The Number1:"))
  Num2=int(input("Enter The Number2:"))
  Sub=Num1-Num2
  print("Subtraction is",Sub)

def Multiplication():
  Num1=int(input("Enter The Number1:"))
  Num2=int(input("Enter The Number2:"))
  Mul=Num1*Num2
  print("Multiplication is",Mul)

def Division():
  Num1=int(input("Enter The Number1:"))
  Num2=int(input("Enter The Number2:"))
  Div=Num1/Num2
  print("Division is",Div)

def Calculator():
  choice=int(input("Enter the choice:"));
  choice==0;

  if(choice ==1):
    print(Addition())
  elif(choice ==2):
    print(Subtraction())
  elif(choice ==3):
    print(Multiplication())
  elif(choice ==4):
    print(Division())
  else:
    print("Try Again")

def main():
   print(Calculator())
main()