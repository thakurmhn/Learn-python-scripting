#!/usr/bin/env python3

## Dunder methods (__method__()) are called automatically when objects are accessed; they are magic methods
## Below are examples of few dunder methods


class Garage:
    def __init__(self):
        self.cars=[]     # Self is refered to object and cars will be a list created within the object


    def __len__(self):      ## by default print(len()) does not print length of cars 
                            ## so we have defined magic function len() to calculate length of cars
        return len(self.cars)

# Returns index of cars list
    def __getitem__(self, i):
        return self.cars[i]

# Returns string about object; 
    def __repr__(self):
        return f'<Garage with two cars {self.cars}'

# __str__ is same as above; you can use either but prefered is  __repr_
    def __str__(self):
        return f'<Garage with two cars {self.cars}'


ford=Garage()
ford.cars.append('Feista')
ford.cars.append('Figo')


print(ford.cars)
print(len(ford.cars))
print(ford.cars[0])
print(ford[1]) # this is another way of calling Garage.__getitem__(ford, 0)


# when you have __len__() and __getitem__() methods you can iterate over ford object

for car in ford: 
    print(car)


# access repr method
print(ford)
