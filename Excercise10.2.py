"""
Extend the previous program by creating a Building class.
The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building.
When a building is created, the building creates the required number of elevators.
The list of elevators is stored as a property of the building.
Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters.
In the main program, write the statements for creating a new building and running the elevators of the building.
"""

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current = bottom_floor
        self.elevator_number = 1



    def floor_up(self):
        self.current += 1
        print(f"You are in {self.current}th floor")

    def floor_down(self):
        self.current -= 1
        print(f"You are in {self.current}th floor")

    def go_to_floor(self, floor_number):
        while self.current < floor_number:
            self.floor_up()

        while floor_number < self.current:
            self.floor_down()


class Building:
    def __init__(self, bottom, top, elevator_numbers):
        self.bottom = bottom
        self.top = top
        self.elevator_numbers = elevator_numbers
        self.list_elevators = []

        for i in range(self.elevator_numbers):
            self.list_elevators.append(Elevator(bottom, top))
            print("Elevator number", self.list_elevators[i])

    def run_elevator(self, elevator_number, destination_floor):
        elevator_index = elevator_number - 1
        self.list_elevators[elevator_index].go_to_floor(destination_floor)



build1 = Building(0, 10, 3)

build1.run_elevator(1, 5)


