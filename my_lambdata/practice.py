#Python Object-Oreinted programming
#Classes &Instances practice

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)    

#print(emp_1)
#print(emp_2)

#emp_1.first = 'Corey'
#emp_1.last = 'Schaffer'
#emp_1.email = 'Corey.Schafer@company.com'
#emp_1.pay = 50000

#emp_2.first = 'Test'
#emp_2.last = 'User'
#emp_2.email = 'Test.User@company.com'
#emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

print(emp_2.fullname)