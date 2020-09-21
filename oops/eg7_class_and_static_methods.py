#!/usr/bin/env python3


class Student:
    def __init__(self, name, school):
        self.name=name
        self.school=school
        self.marks=[]

    def average(self):
        return sum(self.marks) / len(self.marks)

'''
above two methods are called Instance method. 'self' always represent the object which gets created by the class. 

when we access method within the object python treat it as

Student.average(self) where self is object

'''

rolf=Student('Rolf Smith', 'Oxford')
rolf.marks.append(57)

# Two ways we can access average method

print(rolf.average())
print(Student.average(rolf))  # python internaly does this way where rolf is passed as first argument which is self

# There are other two methods of which one takes class as argument - called @classmethod
# another takes nothing as argument - called @staticmethod

# Example @classmethod

class Foo:
    @classmethod
    def hi(cls):  # 'cls' parameter holds value for class
        print(cls.__name__)

my_object=Foo()
print(my_object.hi())


#Example @staticmethod

class Bar:
    @staticmethod
    def hello():
        print("I don't take any parameters")

myobject=Bar()
print(myobject.hello())

 
