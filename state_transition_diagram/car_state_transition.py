import sys
sys.path.append('..')
from car_state import CarState

class Car:
    def __init__(self):
        self.state = CarState.DRIVE

    def go_forward(self):
        if self.state == CarState.DRIVE:
            self.state = CarState.DRIVE

    def face_pedestrians(self):
        if self.state == CarState.DRIVE:
            self.state = CarState.WAIT

    def pedestrians_already_cross_road(self):
        if self.state == CarState.WAIT:
            self.state = CarState.DRIVE

    def pedestrians_are_crossing_road(self):
        if self.state == CarState.WAIT:
            self.state = CarState.WAIT

    def encounter_obstacles(self):
        if self.state == CarState.DRIVE:
            self.state = CarState.STOP

    def is_safe(self):
        if self.state == CarState.STOP:
            self.state = CarState.DRIVE
    
    def is_unsafe(self):
        if self.state == CarState.STOP:
            self.state = CarState.STOP

    def current_state(self):
        return self.state.value
