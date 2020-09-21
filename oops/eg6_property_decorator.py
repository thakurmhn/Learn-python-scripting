#!/usr/bin/env python3

'''
In normal case we access methods within object using below syntax
print(rolf.weekly_salary())

However if we wanted to access the same method as we access other properties like

print(rolf.weekly_salary)

we should use @property decorator.

We can use @property decorator if method only accepr self parameter and does not do any action but just return some values

Do not use properties if method does any actions like

connecting database
opening files
calling web server etc

'''


class Student:
    def __init__(self, name, school):
        self.name=name
        self.school=school
        self.marks=[]
    
    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):  
    def __init__(self, name, school, salary):
        super().__init__(name, school) 
        self.salary=salary

    @property                 # defining method to use as property
    def weekly_salary(self):
       return  self.salary * 40.0

# Create object using child class

rolf=WorkingStudent('Rolf', 'SBPPS', 25.0)

#print(rolf.weekly_salary())

# Calling method weekly_salary() as normal property

print(rolf.weekly_salary)
