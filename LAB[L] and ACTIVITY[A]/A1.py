"""
Author: Tanmmey arora
"""
Amt=int(input("Enter the amount: "));
x=str(input("Enter the dollar type:"));
if(x=="nz"):
   Nz=Amt*0.95
   print("New Zealland dollars are:",Nz)
else:
   Aus=Amt/0.95
   print("Australian dollar are:", Aus)