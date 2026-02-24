#Paras Chaudhary_202501100700103_ECE-B
items = int(input("Enter the number of items : "))
print("\n")
prices = []
quantity = []

if items == 0:
    print("No items purchased.")
else:
    for i in range(items):
        price = float(input(f"Enter the price of item{i+1}: "))
        prices.append(price)
        quan = int(input(f"Enter the quantity of item{i+1}: "))
        quantity.append(quan)
        print("\n")


    amount = 0

    for i in range(items):
        amount += prices[i]*quantity[i]

    discount = 0

    if amount > 100:
        discount = (10/100)*amount

    FinalAmount = amount - discount

    print(f"Amount = {amount}")
    print(f"Discount = {discount}")
    print(f"Final Amount = {FinalAmount}")


