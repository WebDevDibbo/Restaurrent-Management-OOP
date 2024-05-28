from food_item import FoodItem
from menu import Menu
from users import Customer,Admin,Employee
from restaurent import Restaurant
from orders import Order


mamar_restaurant = Restaurant("Mamar Restaurant")
def customer_menu():
    name = input("Enter your Name : ")
    email = input("Enter your Email : ")
    phone = input("Enter your Phone : ")
    address = input("Enter your Address : ")
    customer = Customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {customer.name}!!")
        print("1. View Menu")
        print("2. Add item to Cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            customer.view_menu(mamar_restaurant)

        elif choice == 2:
            item_name = input("Enter item name : ")
            item_quantity = int(input("Enter item quantity : "))
            customer.add_to_cart(mamar_restaurant,item_name,item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        else:
            break