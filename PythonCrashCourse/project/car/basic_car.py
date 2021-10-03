class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.oddometer_reading = 0

    def get_car_details(self):
        details = f" This Car is of {self.make} make, Model is {self.model} and manufactured in {str(self.year)}"
        return details

    def get_car_name(self):

        car_name = f"{self.make} {self.model}"
        return car_name

    def read_oddometer(self):

        print(f"This Car has {str(self.oddometer_reading)} on it")

    def update_oddometer(self, mileage):
        if mileage >= self.oddometer_reading:
            self.oddometer_reading = mileage
        else:
            print(f"You can't roll back an oddometer")

    def increament_oddometer(self, miles):
        self.oddometer_reading += miles


