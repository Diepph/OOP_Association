
"""
Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor.
If you make elevator h for example the method call h.go_to_floor(5),
the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor.
The methods run the elevator one floor up or down and tell what floor the elevator is after each move.
Test the class by creating an elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.
"""

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

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



elevator = Elevator(0, 10)

elevator.go_to_floor(3)
elevator.go_to_floor(1)
elevator.go_to_floor(10)
elevator.go_to_floor(0)


