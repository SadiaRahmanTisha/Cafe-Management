menu = {
    'coffe':30,
    'tea':40,
    'pasta':50,
    'burger':30,
    'pizza':100,
}

print("Welcome to Python Resturant")
print("coffe: Rs30\ntea: Rs40\npasta: Rs50\nburger: Rs30\npizza: Rs100")

order_total = 0
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (yes/no) ")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added")
    else:
      print(f"Order item {item_2} is not available!")


print(f"The total amount of items is to pay {order_total}")    
