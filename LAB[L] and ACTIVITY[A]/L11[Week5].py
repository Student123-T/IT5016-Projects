"""
Author:Tanmmey Arora
"""
#LAB 3
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
        print(f"Categoty:{Category}\nRecommendation:{Recommendation}\nTotal Cost:${Total_Cost:.2f}")
def main():
    shoppinglist, Total_Cost = shopping_list()
    print("\nShopping List:")
    for  item_name,item_price in shoppinglist:
        print(f"{item_name}:${item_price:.2f}")
        Categorized_Request(Total_Cost)
main()
