#!/usr/bin/env python3.7

'''
With polymorphism we can use same method names in differrent classes

'''

class Appserver():
	def __init__(self,name,version):
		self.name=name
		self.version=version
		self.display()
		return None

	def display(self):
		print(f"Appserver Name is: {self.name}\nAppserver Version is: {self.version}")

class Webserver():
	def __init__(self,name,version):
		self.name=name
		self.version=version
		self.display()
		return None

	def display(self):
		print(f"Webserver Name is: {self.name}\nWebserver Version is: {self.version}")

appobj=Appserver('Tomcat','7.9')
webopj=Webserver('Apache','2.4')
