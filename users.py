# CUSTOMER
# EMPLOYEE
# ADMIN

from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()

    # *!!bujinai restaurent kivabe asche
    def add_to_cart(self,restaurent,item_name,quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("----->item quantity exceeded<-----")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("item added")
        else:
            print("----->item not found<-----")
    
    def view_cart(self):
        print("********VIEW CART************")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price : {self.cart.total_price}")


    def pay_bill(self):
        print(f"Totol {self.card.total_price} paid successfully")
        self.cart.clear()


class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name,phone,email,address)
        self.age = age
        self.designation = designation
        self.salary = salary

# emp = Employee("rahim",34535345,"rahim@gmail.com","dhaka",23,"Chef",12000)
# print(emp.name)

class Admin(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name,phone,email,address)

    #* admin just func call korbe kaj hoye jabe behind the scene ki hoche seta amra abstract kore raktesi mane admin dekte parbe na kivabe object toiri hoche print hoche 
    def add_employee(self,restaurent,employee): #Restaurent class er ekta object restaurent
        restaurent.add_employee(employee)

    def view_employee(self,restaurent):
        restaurent.view_employee()

    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)

    def delete_item(self,restaurent,item):
        restaurent.menu.remove_item(item)

    def view_menu(self,restaurant):
        restaurant.menu.show_menu()



# mama_res = Restaurent("mama restaurent")
# admin = Admin('karim',34345354,"karim@gmail.com","dinajpur")
# mn = Menu()
# item = FoodItem("Pizza",12.45,10)
# item1 = FoodItem("Burger",10,30)
# admin.add_new_item(mama_res,item)
# admin.add_new_item(mama_res,item1)


# customer = Customer("Rahim",9874538945,"rahim@gmail.com","barishal")
# customer.view_menu(mama_res)

# item_name = input("Enter item Name : ")
# item_quantity = int(input("Enter Item quantity : ")
# )
# customer.add_to_cart(mama_res,item_name,item_quantity)
# customer.view_cart()