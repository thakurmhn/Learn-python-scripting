#!/usr/bin/env python3

'''
If all methods in abstract class are abstractmethods then it becomes interface for all child classes
'''

from abc import abstractmethod,ABC

class BMW(ABC):
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year

    @abstractmethod
    def start(self):
      pass

    @abstractmethod
    def stop(self):
      pass

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

# Implemented all abstract method in ThreeSeris child class

    def start(self):
        super().start()
        print("Button start")
    
    def stop(self):
        super().stop()
        print("Stop Button")
    
    def drive(self):
        print("ThreeSeris is being driven")

class FiveSeries(BMW):

    def __init__(self, parkingAssistEnabled,make,model,year):
        super().__init__(make,model,year)
        self.parkingAssistEnabled = parkingAssistEnabled

# Implemented all abstract methods

    def drive(self):
                print("FiveSeris is being driven")

    def start(self):
        super().start()
        print("Remote start")

    def stop(self):
        super().stop()
        print("Remote Button")

bmwthreeseries=ThreeSeries(True, "BMW", "328i", "2018")
print(bmwthreeseries.cruiseControlEnabled)
print(bmwthreeseries.make)
print(bmwthreeseries.model)
print(bmwthreeseries.year)
print(bmwthreeseries.start())
print(bmwthreeseries.drive())


bmwfiveseries=FiveSeries(True, "BMW", "555g", "2019")
print(bmwfiveseries.start())
print(bmwfiveseries.stop())
print(bmwfiveseries.drive())
