class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def calculate_salary(self):
        return self.salary

class Manager(Employee):
    def calculate_salary(self):
        return self.salary + 15000

class Developer(Employee):
    def calculate_salary(self):
        return self.salary + 8000


m= Manager("Karan", 80000)
d= Developer("Aditya",40000)
print(f"{m.name} Salary: {m.calculate_salary()}")
print(f"{d.name} Salary: {d.calculate_salary()}")
