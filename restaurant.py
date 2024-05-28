from menu import Menu


#** employee add and employee delete er jonno ekta class
class Restaurant:
    def __init__(self,name) -> None:
        self.name = name
        self.employees = [] # eta hoche amader employees database
        self.menu = Menu()

    def add_employee(self,employee): #employee object pass korchi 
        self.employees.append(employee) 
        print(f'{employee.name} is added!!')

    def view_employee(self):
        print('*****Employee list*****')
        print("Name\tEmail\tPhone\taddress")
        for emp in self.employees:
            print(emp.name,emp.email,emp.phone,emp.address)
