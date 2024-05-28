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



def admin_menu():
    name = input("Enter your Name : ")
    email = input("Enter your Email : ")
    phone = input("Enter your Phone : ")
    address = input("Enter your Address : ")
    admin = Admin(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {admin.name}!!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Items")
        print("6. Exit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            item_name = input("Enter item name : ")
            item_price = int(input("Enter item price : "))
            item_quantity = int(input("Enter item quantity : "))
            item = FoodItem(item_name, item_price,item_quantity)
            admin.add_new_item(mamar_restaurant,item)

        elif choice == 2:
            name = input("Enter employee name : ")
            phone = input("Enter employee phone : ")
            email = input("Enter employee email : ")
            designation = input("Enter employee designation : ")
            age = input("Enter employee age : ")
            salary = input("Enter employee salary : ")
            address = input("Enter employee address : ")
            employee = Employee(name,email,phone,address,age,designation,salary)
            admin.add_employee(mamar_restaurant,employee)
            
        elif choice == 3:
            admin.view_employee(mamar_restaurant)
        elif choice == 4:
            admin.view_menu(mamar_restaurant)
        elif choice == 5:
            item_name = input("Enter item name : ")
            admin.delete_item(mamar_restaurant,item_name)
        elif choice == 6:
            break
        else:
            print("Invalid input")