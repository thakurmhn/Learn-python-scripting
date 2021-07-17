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

my_new_car = Car('Ford', 'Figo', '2014')
print(my_new_car.get_descriptive_name())