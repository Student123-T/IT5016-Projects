"""
Aythor:Tanmmey Arora
"""

def Grade_Calculator():
    Assesment_Grade=float(input("Enter your assesment grade:"))
    Exam_Grade=float(input("Enter your exam grade:"))
    Avg=(Assesment_Grade+Exam_Grade)/2
    print("Your average grade is:",Avg)
    if(Avg>=90):
        print("Your final grade is A")
    elif(Avg>=80):
        print("Your final grade is B")
    elif(Avg>=70):
        print("Your final grade is C")
    elif(Avg>=60):
        print("Your final grade is D")
    else:
        print("FAIL")
def main():
    print(Grade_Calculator())
main()