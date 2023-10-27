class Citizen():
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status

    def getName(self):return self.name

    def getCity(self):return self.city

    def getStatus(self):return self.status


class Employee(Citizen):
    def __init__(self, name, city, status, salary):
        self.annual_salary = salary
        Citizen.__init__(self, name, city, status)

    def getSalary(self): return self.annual_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, city, status, annual_salary, fraction:bool, union:bool):
        Employee.__init__(self, name, city, status, annual_salary)
        self.fraction = fraction
        self.union = union


a = Citizen("Bob", "Tokyo", "Alive")
b = Employee("Alice", "Kyoto", "Alive", 100000)
c = PartTimeEmployee("Joe", "Nagano", "Alive", 100000, 0.5, False)

print(a.getName())
print(b.getSalary())
