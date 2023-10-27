# Quiz 85

## Python Solution 
```.py
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
        Citizen.__init__(name, city, status)

    def getSalary(self): return self.annual_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, city, status, annual_salary, fraction:bool, union:bool):
        Employee.__init__(name, city, status, annual_salary)
        self.fraction = fraction
        self.union = union
```

### Evidence
![](/Assets/Quiz_085_evidence.png)

**Fig.1:** Evidence for Quiz Num

## Paper Programming
![](/Assets/Quiz_085_papercode.jpeg)

**Fig.2:** Paper Programming for Quiz Num