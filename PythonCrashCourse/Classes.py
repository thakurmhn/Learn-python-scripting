class Dog():
        # init method will be automatically called while creating instance from this class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name.title()} is now siting")

    def roll_over(self):
        print(f"{self.name.title()} is now rolling over")


# my_dog = Dog('Moti', 4)
# print(f"My Dog name is {my_dog.name}")
# print(f"My Dog age is {my_dog.age}")
#
# #print(dir(my_dog))
# my_dog.sit()
# my_dog.roll_over()

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurent_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name is {self.restaurent_name}")
        print(f"{self.restaurent_name} serves {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"{self.restaurent_name} opens in the Evening")

# # Create an instance from Class
# restaurant1 = Restaurant("Konkan Swad", "Malvani")
#
# # Access an Instance and Instance attributes
# print(f"The best nearby restaurant is {restaurant1.restaurent_name}")
# print(f"{restaurant1.restaurent_name} popular to serve {restaurant1.cuisine_type} food")
#
# # Access Instance Methods
# restaurant1.describe_restaurant()
# restaurant1.open_restaurant()


class User():
    def __init__(self, first_name, last_name, userid, user_role, is_active):
        self.first_name = first_name
        self.last_name = last_name
        self.userid = userid
        self.user_role = user_role
        self.is_active = is_active

    def describe_user(self):
        print(f"User First Name: {self.first_name.title()}")
        print(f"User Last Name: {self.last_name.title()}")
        print(f"User ID: {self.userid}")
        print(f"User Role: {self.user_role.title()}")
        print(f"Is Active User: {self.is_active}")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}")

# user1 = User('Dipesh', 'Thakur', 'dipesht', 'Admin', 'yes')
#
# print(f"User's first name is {user1.first_name}")
# print(f"User's last name is {user1.last_name}")
# print(f"User's userid is {user1.userid}")
# print(f"User's role is {user1.user_role}")
# print(f"Is this an active user?", user1.is_active)
#
# user1.describe_user()
# user1.greet_user()

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = self.make + ' ' + self.model + ' ' + self.year
        return long_name

#my_new_car = Car('Ford', 'Figo', '2014')
#print(my_new_car.get_descriptive_name())


'''
Working with Classes -
Once you wrote a class you might need to update instance attributes 
1. Setting a default value to the attribute
'''
#eg.
# set default value to the attribute

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # set default value to zero

    def get_descriptive_name(self):
        long_name = self.make + ' ' + self.model + ' ' + self.year
        return long_name

    def read_odometer(self):
        print(f"This Car has {self.odometer_reading} milege on it")
        return None


new_audi=Car('Audi', 'A4', 2021)

#print(f"My Audi is {new_audi.model}")
#print(new_audi.read_odometer())

'''
2. Modifying Attribute Values -
You can change an attribute’s value in three ways: you can change the value
directly through an instance, set the value through a method, or increment
the value (add a certain amount to it) through a method.
'''
'''
# Modify attribute value directly
'''

#print(f"My Audi is {new_audi.model}")
#new_audi.odometer_reading = 800             # directly modified attribute value
#print(new_audi.read_odometer())

'''
Modifying an Attribute’s Value Through a Method
'''

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # set default value to zero

    def get_descriptive_name(self):
        long_name = self.make + ' ' + self.model + ' ' + self.year
        return long_name

    def read_odometer(self):
        print(f"This Car has {self.odometer_reading} milege on it")
        return None

    def update_odometer(self, milage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = milage

#your_car=Car('Audi', 'A3', 2020)

#print(f"Your car is {your_car.make}")
#your_car.update_odometer(400)
#print(your_car.read_odometer())

'''
Incrementing an Attribute’s Value Through a Method
'''
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # set default value to zero

    def get_descriptive_name(self):
        long_name = self.make + ' ' + self.model + ' ' + self.year
        return long_name

    def read_odometer(self):
        print(f"This Car has {self.odometer_reading} milege on it")
        return None

    def update_odometer(self, milage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = milage

    def increament_odometer(self, milage):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += milage  # increment

    def fill_gas_tank(self):
        print("Filling Gas Tank ...")

# my_used_car = Car('subaru', 'outback', '2013')
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
# my_used_car.increament_odometer(100)
# my_used_car.read_odometer()read_odometer

"""MOdify Class Attributes"""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurent_name = restaurant_name
        self.cuisine_type = cuisine_type
        """set default attribute value"""
        self.number_served = 0

    def describe_restaurant(self):

        print(f"Restaurant Name is {self.restaurent_name}")
        print(f"{self.restaurent_name} serves {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"{self.restaurent_name} opens in the Evening")

    def set_served_number(self, served_number):
        """method to modify default attribute value"""
        self.number_served = served_number

    def increament_number_served(self, served_number):
        """Method to increament served number"""
        self.number_served += served_number

# birdvally=Restaurant('Bird Vally', 'Panjabi')
# '''modify default attribute value directly'''
# birdvally.number_served = 30
#
# print(birdvally.restaurent_name)
# print(birdvally.cuisine_type)
# print(birdvally.number_served)
#
# '''call method to modify default attribute value'''
# birdvally.set_served_number(50)
# birdvally.increament_number_served(2)
# print(birdvally.number_served)

class User():
    def __init__(self, first_name, last_name, userid, user_role, is_active):
        self.first_name = first_name
        self.last_name = last_name
        self.userid = userid
        self.user_role = user_role
        self.is_active = is_active
        self.login_attempts_count = 1  # modified default attribute value

    def describe_user(self):
        print(f"User First Name: {self.first_name.title()}")
        print(f"User Last Name: {self.last_name.title()}")
        print(f"User ID: {self.userid}")
        print(f"User Role: {self.user_role.title()}")
        print(f"Is Active User: {self.is_active}")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}")
        return None

    def increament_login_attempts(self):
        """Method to increament login attempts attribute value"""
        self.login_attempts_count +=  1
        print(self.login_attempts_count)

    def reset_login_attempt(self):
        """method to reset login attempt"""
        self.login_attempts_count = 0


# foo=User('foo', 'bar', 1001, 'testuser', 'active')
#
# foo.increament_login_attempts()
# print(foo.login_attempts_count)
# geeko.reset_login_attempt()
# #print(geeko.login_attempts_count)

""" Inheritance """

"""
You don’t always have to start from scratch when writing a class. If the class
you’re writing is a specialized version of another class you wrote, you can
use inheritance. When one class inherits from another, it automatically takes
on all the attributes and methods of the first class. The original class is
called the parent class, and the new class is the child class. The child class
inherits every attribute and method from its parent class but is also free to
define new attributes and methods of its own.
The __init__() Method for a Child Class
The first task Python has when creating an instance from a child class is to
assign values to all attributes in the parent class. To do this, the __init__()
method for a child class needs help from its parent class.
As an example, let’s model an electric car. An electric car is just a specific
kind of car, so we can base our new ElectricCar class on the Car class
we wrote earlier. Then we’ll only have to write code for the attributes and
behavior specific to electric cars.
Let’s start by making a simple version of the ElectricCar class, which
does everything the Car class does:
"""
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self,make,model,year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)



# My_Tesla=ElectricCar('Tesla', 'Model S', '2016')
# My_Tesla.increament_odometer(500)
# print(My_Tesla.odometer_reading)

class ElectricCarTesla(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        """Attribute specific to Tesla Car"""
        self.battery_size = 70

        """Override method from parent class"""
        """To override method from parent class define same method name in child class as parent class """
        """and python will ignore that method"""
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")



# new_tesla=ElectricCarTesla('Tesla', 'Model V', '2020')
# print(f"Battery Size in new tesla is {new_tesla.battery_size} kWH")
# new_tesla.fill_gas_tank()
"""
Instances as Attributes
When modeling something from the real world in code, you may find that
you’re adding more and more detail to a class. You’ll find that you have a
growing list of attributes and methods and that your files are becoming
lengthy. In these situations, you might recognize that part of one class can
be written as a separate class. You can break your large class into smaller
classes that work together.
For example, if we continue adding detail to the ElectricCar class, we
might notice that we’re adding many attributes and methods specific to
the car’s battery. When we see this happening, we can stop and move those
attributes and methods to a separate class called Battery. Then we can use a
Battery instance as an attribute in the ElectricCar class:
"""

class Battery():
    def __init__(self, battery_size=100):
        self.battery_size = battery_size
        self.range = ''

    def describe_battery(self):
        self.battery_description = f"Battery Size is {self.battery_size} kWH"
        return self.battery_description

    """Adding more methods without touching ElectricCar class"""
    def get_range(self):
        if self.battery_size == 100:
            self.range = 300
        elif self.battery_size == 85:
            self.range = 240
        message=f"This Car can go approx {self.range} miles"
        message += "miles on full charge"
        return message

class ElectricCarToyota(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        """Initialize class instance as Attribute"""
        self.battery = Battery()

        """ Override method from parent class 
        To do so write the same method name in parent class
        e.g to override method fill_gas_tank() which is not required for Electric Car
        """

    def fill_gas_tank(self):
        is_gas_tank = f"Electric Car does't require to fill gas"
        return is_gas_tank

# new_toyota = ElectricCarToyota('Toyota', 'Model GT', '2020')
# print(new_toyota.battery.describe_battery())
# print(new_toyota.battery.get_range())
# print(new_toyota.fill_gas_tank())

""" Exercise"""

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type ):
        super().__init__(restaurant_name, cuisine_type)
        self.icecream_flavors = ['vanila', 'fruity', 'butter-schoch', 'mango', 'pineapple']


    def get_icecreame_flavors(self):
        return self.icecream_flavors


# favorite_restaurent = IceCreamStand("Panjabi Rasoi", "Panjabi")
# print(f"{favorite_restaurent.describe_restaurant()}")
# print(f" Available Icecream flavors {favorite_restaurent.get_icecreame_flavors()}")


class AdminUser(User):
    def __init__(self, first_name, last_name, userid, user_role, is_active):
        super().__init__(first_name, last_name, userid, user_role, is_active)

        self.is_admin = True
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can delete user']

    def show_previleges(self):
        return self.privileges


# mohan = AdminUser('Mohan', 'Thakur', 'thakurm', 'admin', 'yes')
# print(f" Is User is Admin? {mohan.is_admin}")
# print(f"Admin user has following previleges {mohan.show_previleges()}")
# mohan.describe_user()

class AdminPrevileges():
    def __init__(self):
        self.admin_privileges = ['add post', 'read post', 'ban user', 'delete user', 'delete post']

    def show_admin_privilegs(self):
        return self.admin_privileges


class NewAdmin(User):
    def __init__(self, first_name, last_name, userid, user_role, is_active):
        super().__init__(first_name, last_name, userid, user_role, is_active)

        self.new_privileges = AdminPrevileges() # Creating instance of another class


    def show_new_admin_privileges(self):
        return self.new_privileges.show_admin_privilegs()

new_admin = NewAdmin('Geeko', 'Sam', 'geekos', '1001', 'admin')
print(new_admin.greet_user())
print(new_admin.show_new_admin_privileges())

