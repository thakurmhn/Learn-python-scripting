from car.basic_car import Car

def main():

    my_car = Car("Ford", "Figo", "2014")

    print(f"My car is {my_car.get_car_name()}")
    print(f"My Car details as {my_car.get_car_details()}")


if __name__ == "__main__":
    main()