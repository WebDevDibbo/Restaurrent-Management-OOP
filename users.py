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
        self.employees = [] # eta hoche amader database

    def add_employee(self,name,email,phone,address,age,designation,salary):
        employee = Employee(name,email,phone,address,age,designation,salary) # Employee class er ekta object toiri hoye jabe
        self.employees.append(employee)
        print(f'{name} is added!!')

    def view_employee(self):
        print('Employee list!!')
        for emp in self.employees:
            print(emp.name,emp.email,emp.phone,emp.address)


adm = Admin('karim',34345354,"karim@gmail.com","dinajpur")
adm.add_employee("sagor","sagor@gmail.com",948473,"chattogram",33,"chef",15000)

adm.view_employee()