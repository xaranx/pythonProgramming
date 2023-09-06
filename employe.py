class Employee:
    raise_amount = 1.05
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@' + 'company.com'

    #method to get the full_name
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    #Method to raise the pay
  
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    #Method to creat new user -->cls
    @classmethod
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)
    
    #static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
       
        return False

import datetime
my_date = datetime.date(2023, 9, 3)

emp_1 = Employee('James', 'Muller', 1200)
emp_2 = Employee('Daniel', 'smith', 2000)

emp_str_3 = 'John-Doe-3000'

new_emp_1 = Employee.from_string(emp_str_3)

print(emp_1.fullname())
print(emp_2.fullname())
print(emp_1.pay)
print(new_emp_1.fullname())
print(new_emp_1.pay)


print(Employee.is_workday(my_date))
