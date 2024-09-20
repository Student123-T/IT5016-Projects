"""
Author:Tanmmey Arora
"""
#LAB 1
def create_detailed_report(id_counter):
     user_name=input("Enter your user name:")
     user_age=input("Enter your age:")
     user_email=input("Enter your E-mail:")
     unique_id=id_counter+1
     updated_counter=unique_id
     print("Detailed Report:")
     print(f"Name:{user_name}\nAge:{user_age}\nE-mail:{user_email}\nID Counter:{updated_counter}")
     return updated_counter,unique_id
id_counter=5000
id_counter,unique_id=create_detailed_report(id_counter)
