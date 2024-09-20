"""
Author:Tanmmey Arora
"""

def Magnitude_Descriptor():
    Magnitude=float(input("Plaesa enter magnitude of the earthquak:"))
    if(Magnitude<2.0):
       print("The earthquake is Micro.")
    elif(2.0>Magnitude<3.0):
       print("The earthquake is Very Minor.")
    elif(3.0>Magnitude<4.0):
       print("The earthquake is Minor.")
    elif(4.0>Magnitude<5.0):
       print("The earthquake is Light.")
    elif(5.0>Magnitude<6.0):
       print("The earthquake is Moderate.")
    elif(6.0>Magnitude<7.0):
       print("The earthquake is Strong.")
    elif(7.0>Magnitude<8.0):
       print("The earthquake is Major.")
    elif(8.0>Magnitude<10.0):
       print("The earthquake is Great.")
    else:
       print("The earthquake is Meteoric")
def main():
   print(Magnitude_Descriptor())
main()