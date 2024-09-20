"""
Author:Tanmmey Arora
"""

def Student_Details():
    Std_ID=str(input("Enter your student id:"))
    First_Name=str(input("Enter your first name:"))
    Last_Name=str(input("Enter your last namr:"))
    University=str(input("Which University do you attend?:"))
    if (University in "Whitecliffe"or"College"):
        Username=(Std_ID[0:2])+(Last_Name[0:3])
        print("Welcome to Whitecliffe College!")
        print("Your user name is:",Username)
    else:
        print("Please have your university generate your username.")
def main():
    print(Student_Details())
main()
