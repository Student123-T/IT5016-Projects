"""
Author:Tanmmey Arora
"""
#Q1[Dictionary]
def Dictionary():
    stu_reg_no1=(input("Enter your number:"))
    stu_reg_no2=(input("Enter your number:"))
    stu_reg_no3=(input("Enter your number:"))
    stu_name1=str(input("Enter your name:"))
    stu_name2=str(input("Enter your name:"))
    stu_name3=str(input("Enter your name:"))
    Dic={stu_reg_no1:stu_name1,stu_reg_no2:stu_name2,stu_reg_no3:stu_name3}
    print(Dic)
#Q2[Discounted Question]
def main():
    Dictionary()
main()

def apply_price(price):
    if price>300:
       discount_price=price*0.95
    return price
def compute_total_cost(items):
    total_cost=0
    for price in items:
        discount_price=apply_price
        total_cost+=discount_price
    return total_cost
def main():
    name=input(" name:")
    if name=="main":
        item_price=[300,455,65,544,344,55,444,645]
    else:
        print("Nothing")

        total_cost=compute_total_cost(item_price)
        print(total_cost)
main()
