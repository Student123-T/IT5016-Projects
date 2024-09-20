"""
Author:Tanmmey Arora
"""
#LAB 4
def create_detailed_report(id_counter):
     user_name=input("Enter your user name:")
     user_age=input("Enter your age:")
     user_email=input("Enter your E-mail:")
     unique_id=id_counter+1
     updated_counter=unique_id
     print("Detailed Report:")
     print(f"Name:{user_name}\nAge:{user_age}\nE-mail:{user_email}")
     return updated_counter,unique_id
id_counter=5000
id_counter,unique_id=create_detailed_report(id_counter)
def shopping_list():
    shoppinglist=[]
    Total_Cost=0
    while True:
        item_name=input("Enter the item name [or type Done]:")
        if item_name.lower()=='done':
            break
        try:
            item_price=float(input(f"Enter the item price {item_name}:"))
            shoppinglist.append((item_name,item_price))
            Total_Cost+=item_price
        except ValueError:
            print("Invalid Input.Plz Enter Numeric Value!")
    return shoppinglist,Total_Cost 
def Categorized_Request(Total_Cost):
        if Total_Cost<150:
             Category="LOW"
             Recommendation="Proceed with standard processing."
        else:
             Category="HIGH"
             Recommendation="Review for potential discounts."
        print(f"Categoty:{Category}\nRecommendation:{Recommendation}")
def main():
    shoppinglist, Total_Cost = shopping_list()
    print("\nShopping List:")
    for item_name, item_price in shoppinglist:
        print(f"{item_name}: ${item_price:.2f}")
        Categorized_Request(Total_Cost)
        print(f"Total Cost:${Total_Cost:.2f}")
main()
