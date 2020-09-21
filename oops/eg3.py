#!/usr/bin/env python3


class Student:

# A function to define object properties

    def __init__(self, s_name, s_grades):
        self.name = s_name
        self.grades = s_grades


# An Action method
    def calc_average(self):
        return sum(self.grades) / len(self.grades)

# Create object

student1=Student('Rolf Smith', [50, 60, 98, 90, 87])
student2=Student('John F', [80, 80, 78, 90, 69, 89])

# Call object property 
print(student1.grades)

# Call object Action method
print(student1.calc_average())

# above syntax can be written like below as well

print(Student.calc_average(student1))

