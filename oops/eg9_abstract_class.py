#!/usr/bin/env python3

'''
If one or more methods defined with @abstractmethod decorator in class that class becomes abstract class
you can define instance methods in the same class but you can create objects from that class

At least one method should be @abstractmethod in a abstract class

Using abstract classes we can define contract for our child clasess and it is mandatory to implement same methods in all Child classes. 
With abstract class abstract methods are defined in parent class but not implemented. 
Those methods must be defined and implemented in Child class

You can not create object of abstract class

If all the methods in class are @abstractmethod then the class is called Interface

'''

from abc import abstractmethod,ABC

class BMW(ABC):
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")

    @abstractmethod
    def drive(self):                # abstract method; it's mandatory to implement this method in below classes as now
        pass                        # BMW has become abstract class
        "comments here"

class ThreeSeries(BMW):
    
    def __init__(self, cruiseControlEnabled, make,model,year):
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    def start(self):
        super().start()
        print("Button start")

    def drive(self):
        print("ThreeSeris is being driven")

class FiveSeries(BMW):

    def __init__(self, parkingAssistEnabled,make,model,year):
        super().__init__(make,model,year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def drive(self):
                print("ThreeSeris is being driven")

bmwthreeseries=ThreeSeries(True, "BMW", "328i", "2018")
print(bmwthreeseries.cruiseControlEnabled)
print(bmwthreeseries.make)
print(bmwthreeseries.model)
print(bmwthreeseries.year)
print(bmwthreeseries.start())
print(bmwthreeseries.drive())


# You will get error if you try to instanciate BMW abstract class.

#B=BMW(True, "BMW", "328i", "2018")
