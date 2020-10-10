#!/usr/bin/env python3


class BMW:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")

class ThreeSeries(BMW):
    
    def __init__(self, cruiseControlEnabled, make,model,year):
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    def start(self):
        super().start()
        print("Button start")

class FiveSeries(BMW):

    def __init__(self, parkingAssistEnabled,make,model,year):
        super().__init__(make,model,year)
        self.parkingAssistEnabled = parkingAssistEnabled



bmwthreeseries=ThreeSeries(True, "BMW", "328i", "2018")
print(bmwthreeseries.cruiseControlEnabled)
print(bmwthreeseries.make)
print(bmwthreeseries.model)
print(bmwthreeseries.year)
print(bmwthreeseries.start())
