#!/usr/bin/env python3.7

class Emp: 
	def display(self):
		print("This is employee")

emp1=Emp()
emp2=Emp()

emp1.display()

'''
In above example when objects are created display method is not being called by default. we have to call display method emp1.dispaly()
where as with __init_() method (class constructor) no need to call the display method; __init_() method will be called upon creation of objects

'''


class Employee:
	def __init__(self):
		print("This is init method")
emp3=Employee()
emp4=Employee()

## Use Case

class student():
	def __init__(self,sname,sage,smarks):
		self.name=sname
		self.age=sage
		self.marks=smarks
		self.display_details()
	def display_details(self):
		print(f"Sudent Name: {self.name}\nStudent Age: {self.age}\nStudent Marks: {self.marks}")
s1=student('john',12,49)
s2=student('jane',11,40)

#s1.display_details()
#s2.display_details()
