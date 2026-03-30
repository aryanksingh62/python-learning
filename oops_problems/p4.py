class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def calculate_salary(self):
        return f" salary of {self.name} of {self.salary}"

class Full_Employee(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)

class part_Employee(Employee):
    def __init__(self,name,hour,rate):
        super().__init__(name,rate*hour)
        self.rate=rate
        self.hour=hour

    def calculate_salary(self):
        return f"salary of {self.name} is {self.rate*self.hour}"
    
# Create full time employee
e1 = Full_Employee("John", 50000)
print(e1.calculate_salary())   

# Create part time employee
e2 = part_Employee("Sara", 40, 500)
print(e2.calculate_salary())  

# Create another part time employee
e3 = part_Employee("Mike", 20, 300)
print(e3.calculate_salary())   

# Test inheritance
print(isinstance(e1, Employee))  
print(isinstance(e2, Employee))  

# Test names
print(e1.name)  
print(e2.name)  

# Test full time salary never changes
print(e1.salary)  