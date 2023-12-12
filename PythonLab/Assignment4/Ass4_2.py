import random

class Bills:
    
    def calculate_bill_amount(consultation_fees, quantity_list, price_list):
        bill_amount = 0
        for i in range(len(quantity_list)):
            bill_amount += quantity_list[i] * price_list[i]
        bill_amount += consultation_fees
        return bill_amount
    
    def display(name, bill_id, total_amount):
        print("\nBill for",name, "\nRef Id",bill_id, "\nTotal Amount",total_amount)
        

obj = Bills

c_fees = int(input("Enter Consultaion fees: "))

n = int(input("Enter number of medicines: "))
quantity_list = []
price_list = []

for i in range(n):
    print("\nFor medicine",i+1)
    q = int(input("Enter quantity: "))
    p = int(input("Enter price: "))
    quantity_list.append(q)
    price_list.append(p)

id = random.randint(1000, 9999)
name = input("Enter name: ")
total_amount = obj.calculate_bill_amount(c_fees, quantity_list, price_list)
obj.display(name, id, total_amount)