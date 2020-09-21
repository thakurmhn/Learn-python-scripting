#!/usr/bin/env python3

# Problem statement

'''
class Student:
    def __init__(self, name, school, marks):
        self.name=name
        self.school=school
        self.marks=[]

    def average(self):
        return sum(self.marks) / len(self.marks)

# Below clas has duplicate properties as above class
class WorkingStudent:
    def __init__(self, name, school, marks, salary):
        self.name=name
        self.school=school
        self.marks=marks
        self.salary=salary

    def average(self):
                return sum(self.marks) / len(self.marks)

# create instance 
student1=Student('John', 'SBPPS', [70, 56, 78, 87])
student2=WorkingStudent('Rolf', 'SNDT', [98, 86, 77, 55], 25)

print(dir(student1))
print(dir(student2))
'''

## Inherit properties and methods from another class

class Student:
    def __init__(self, name, school):
        self.name=name
        self.school=school
        self.marks=[]
    
    def average(self):
        return sum(self.marks) / len(self.marks)

# Create a Child class WorkingStudent that will inherit some properties from Student class

class WorkingStudent(Student):  # Created child class WorkingStudent whose parent is Student class
    def __init__(self, name, school, salary):
        super().__init__(name, school) ## Get properties from Student (parent) class
        self.salary=salary

    def weekly_salary(self):
       return  self.salary * 40.0

# Create objenct using child class

rolf=WorkingStudent('Rolf', 'SBPPS', 25.0)
rolf.marks.append(55)
rolf.marks.append(66)

print(rolf.name)
print(rolf.school)
print(rolf.average())
print(rolf.weekly_salary())

# Create instance from Student class

john=Student('John Conner', 'Oxford')

print(john.name)
print(john.school)
