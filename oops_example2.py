#!/usr/bin/env python3.7


class Employee: 
	count=0		# This is class attribute; outside of all class methods but inside of class
	
	def get_emp_details(self,ename,eage,esal):	# self referes to Object name
		self.name=ename
		self.age=eage
		self.salary=esal
		self.employee_counter()	# You can call display method here also using self.display_emp_details()
	def display_emp_details(self):
		print(f"Employee Name: {self.name}\nEmployee Age: {self.age}\nEmployee Salary: {self.salary}")

	def employee_counter(self):
		Employee.count=Employee.count+1
		

# outside of class

emp1=Employee()		# Create object emp1
emp2=Employee()		# Create object emp2

emp1.get_emp_details('John',45,30000)
emp2.get_emp_details('Mike',33,20000)

emp1.display_emp_details()
emp2.display_emp_details()

print("Total Number of Employees:",Employee.count)
