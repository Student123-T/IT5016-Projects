"""
Author:Tanmmey Arora
"""
#LAB 2
def shopping_list():
    shoplist=[]
    Total_Cost=0
    while True:
        item_name=input("Enter the item name [or type Done]:")
        if item_name.lower()=='done':
            break
        try:
            item_price=float(input(f"Enter the item price {item_name}:"))
            shoplist.append((item_name,item_price))
            Total_Cost+=item_price
        except ValueError:
            print("Invalid Input.Plz Enter Numeric Value!")
    return shoplist,Total_Cost 
def main():
        print("Welcome to the shopping ")
        shoplist, Total_Cost = shopping_list()
        if not shoplist:
            print("No items are entered")
        else:
            print("\n shopping list")
            for item_name, item_price in shoplist:
                print(f"{item_name},${item_price:.2f}")
            print(f"\n Total Price: ${Total_Cost:.2f}")
    
main()