#!/usr/bin/env python3

my_student={
        "Name": "John",
        "grades": [67, 70, 78, 94, 68]
        }


def average_grade(student):
    return sum(my_student['grades']) / len(my_student['grades'])

#print(average_grade(my_student))

#print(average_grade.__doc__)


class Student:
    def __init__(self, s_name, s_grades):
        self.name = s_name
        self.grades = s_grades

    def calc_average(self):
        return sum(my_student['grades']) / len(my_student['grades'])

# Create object

student1=Student('Rolf Smith', [50, 60, 98, 90, 87])
student2=Student('John F', [80, 80, 78, 90, 69, 89])

print(student1.name)
print(student2.name)



