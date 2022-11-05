"""
This exercise continues the previous car race exercise from the last exercise set.
Write a Race class that has the following properties: name, distance in kilometers and a list of cars participating in the race.
The class has an initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding properties in the class.
The class has the following methods:

hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of speed for each car and calls their drive method.
print_status, which prints out the current information of each car as a clear, formatted table.
race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.
Write a main program that creates an 8000-kilometer race called Grand Demolition Derby.
The new race is given a list of ten cars similarly to the earlier exercise. The main program simulates the progressing of the race by calling the hour_passes in a loop,
after which it uses the race_finished method to check if the race has finished.
The current status is printed out using the print_status method every ten hours and then once more at the end of the race.
"""

import random
from prettytable import PrettyTable

class Car:

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerator(self, speed_change):

        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def distance(self, hours_number):
        new_distance = self.current_speed * hours_number
        self.travelled_distance += new_distance


class Race:
    def __init__(self, name, distance, cars_list):
        self.name = name
        self.distance = distance
        self.cars_list = cars_list

    def hour_passes(self):
        for car in self.cars_list:
            random_change_speed = random.randint(-10, 15)
            car.accelerator(random_change_speed)
            car.distance(10)

    def print_status(self):
        table = PrettyTable(['Registration number', 'Maximum speed', 'Current speed', 'Travelled distance'])

        for car in self.cars_list:
            table.add_row([car.registration_number, car.maximum_speed, car.current_speed, car.travelled_distance])
        print(table)

        #current_status = Car.distance(10)
        #print(current_status)

    def race_finished(self):
        for car in self.cars_list:
            if car.travelled_distance >= self.distance:
                return True
            else:
                return False

car_list = []

# Generate ten cars using for loop
for i in range(10):
    registration_number = ("ABC-" + "%d") % (i + 1)
    # Generate random speed for each car
    random_max_speed = random.randint(100, 200)
    car_list.append(Car(registration_number, random_max_speed))


r = Race("Grand Demolition Derby", 8000, car_list)
#print(list)

while r.race_finished() != True:
    r.hour_passes()

r.print_status()




