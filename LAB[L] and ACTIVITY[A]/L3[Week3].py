"""
Author:Tanmmey Arora
"""

def Wavelength_To_Colour():
    print("Welcome to wavelength to colour converter")
    Wavelength=int(input("Please Enter an integer wavelength between 380 and 750:"))
    if(620 <= Wavelength <= 750):
       print("The Colour Of This Wavelength is...Red")
    elif(590 <= Wavelength <= 620):
       print("The Colour Of This Wavelength is...Orange")
    elif(570 <= Wavelength <= 590):
       print("The Colour Of This Wavelength is...Yellow")
    elif(495 <= Wavelength <= 570):
       print("The Colour Of This Wavelength is...Green")
    elif(450 <= Wavelength <= 495):
       print("The Colour Of This Wavelength is...Blue")
    elif(380 <= Wavelength <= 450):
       print("The Colour Of This Wavelength is...Violet")
    else:
       print("Try Again")
def main():
   print(Wavelength_To_Colour())
main()
