"""
Author:Tanmmey Arora
"""
#Q1 [While Loop]
def password_system():
    correct_password="Tanmmey@56"
    attempts_variables=0
    max_attempts=3
    while attempts_variables < max_attempts:
        enter_password=str(input("Enter password:"))
        if enter_password==correct_password:
            print("Correct Password")
            break
        else:
            attempts_variables+=1
            print(f"Incorrect Password. You have {max_attempts-attempts_variables} attemps left")

        if(attempts_variables==max_attempts):
           print("access denied")
            
def main():
    password_system()
main()

#Q2 [For Loop]
def Multiplication_Tables():
    i=0
    for i in range (7,71,7):
        print(i)
def main():
    Multiplication_Tables()
main()
