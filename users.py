# CUSTOMER
# EMPLOYEE
# ADMIN

from abc import ABC

class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        self.cart = None

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self,restaurent,item_name):
        item = restaurent.menu.find_item(item_name)
        if item:
            pass
        else:
            print("item not found")
    
    def view_cart(self):
        print("**view cart**")
        print("Name\tPrice\tQuantity")
        

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
        

#** employee add and employee delete er jonno ekta class
class Restaurent:
    def __init__(self,name) -> None:
        self.name = name
        self.employees = [] # eta hoche amader employees database
        self.menu = FoodItem()

    def add_employee(self,employee): #employee object pass korchi 
        self.employees.append(employee) 
        print(f'{employee.name} is added!!')

    def view_employee(self):
        print('Employee list!!')
        for emp in self.employees:
            print(emp.name,emp.email,emp.phone,emp.address)



#** product add and product delete er jonno ekta class
class Menu:
    def __init__(self):
        self.items = []  #items er database

    def add_menu_item(self,item):
        self.items.append(item)

    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("item deleted successfully")
        else:
            print("item not found")

    def show_menu(self):
        print("********Menu************")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

 

class FoodItem:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

adm = Admin('karim',34345354,"karim@gmail.com","dinajpur")
mn = Menu()
item = FoodItem("Pizza",12.45,10)
mn.add_menu_item(item)
mn.show_menu()
