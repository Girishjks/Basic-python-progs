# Write a python program by creating a class called Employee to store the details of Name, Employee_ID, Department and Salary, and implement a method to update salary of employees belonging to a given department. 
class Employee:
    def __init__(self, Ename, Eid, Edept, Esal):
        self.name = Ename
        self.id = Eid
        self.dept = Edept
        self.sal = Esal
    def display(self):
            print(self.name, self.id, self.dept, self.sal)
    def update_sal(self, dept, sal):
                if (self.dept == dept):
                    self.sal = sal
Emp = []
n = int(input("enter the number of employee"))
for i in range(n):
    name = input("Enter Employee name : ")
    eid = input("Enter Employee ID : ")
    dept = input("Enter Employee Dept : ")
    sal = int(input("Enter Employee Salary : "))
    emp1 = Employee(name, eid, dept, sal)
    Emp.append(emp1)
print("Employee Details are")
for i in range(n):
    print(Emp[i].name, " ", Emp[i].sal)
print("Update salary Particular Department")
dep = input("enter the department of the salary to be updated")
salary = int(input("Enter the salary to be upadated"))
for i in range(n):
    Emp[i].update_sal(dep, salary)
    print(Emp[i].name, " ", Emp[i].sal)
