#!/usr/bin/env python3.7

'''
With inheritance we can use methods from one class to another class

'''

class Appserver():
	def __init__(self,name,version):
		self.name=name
		self.version=version
		return None

	def display(self):
		print(f"Name is: {self.name}\nVersion is: {self.version}")

class Webserver(Appserver):	# Inherited Appserver class 
	def __init__(self,name,version):
		self.name=name
		self.version=version
		return None


appobj=Appserver('Tomcat','7.9')
webobj=Webserver('Apache','2.4')


webobj.display()	# there is no display() method in Appserver class but we inherited display() from tomcat class
