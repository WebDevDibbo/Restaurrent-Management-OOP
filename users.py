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
        

#** employee add and employee delete er jonno ekta class
class Restaurent:
    def __init__(self,name) -> None:
        self.name = name
        self.employees = [] # eta hoche amader employees database

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



adm = Admin('karim',34345354,"karim@gmail.com","dinajpur")
adm.add_employee("sagor","sagor@gmail.com",948473,"chattogram",33,"chef",15000)
adm.view_employee()