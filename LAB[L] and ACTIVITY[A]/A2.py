"""
Author:Tanmmey Arora
"""
Cover_Price= float(input("Enter the Cover Price:"));
Discounted_Cover_Price= Cover_Price-((Cover_Price*40)/100)
Shipping_Cost_First_Copy= int(input("Enter the cost for firt copy:"));
Adittional_Shipping_Cost= (59*0.75)
Total_Wholesale_Cost= ((Discounted_Cover_Price*60) + Shipping_Cost_First_Copy + Adittional_Shipping_Cost) 
print(Total_Wholesale_Cost)