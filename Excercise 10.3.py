
"""
Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to the bottom floor.
Continue the main program by causing a fire alarm in your building.
"""
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current = bottom_floor
        self.elevator_num = 1

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

    def fire_alarm(self):
        for elevator in self.list_elevators:

            elevator.current = elevator.bottom_floor
            print(f"You are in {elevator.bottom_floor} floor")




build1 = Building(0, 10, 3)

build1.run_elevator(1, 5)
build1.fire_alarm()