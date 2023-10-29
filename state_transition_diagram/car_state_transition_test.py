import unittest
from car_state_transition import Car, CarState

class TestCarState(unittest.TestCase):
    def test_state_transitions(self):
        car = Car()

        self.assertEqual(car.current_state(), CarState.DRIVE.value)

        car.go_forward()
        self.assertEqual(car.current_state(), CarState.DRIVE.value)

        car.face_pedestrians()
        self.assertEqual(car.current_state(), CarState.WAIT.value)

        car.pedestrians_already_cross_road()
        self.assertEqual(car.current_state(), CarState.DRIVE.value)

        car.face_pedestrians()
        car.pedestrians_are_crossing_road()
        self.assertEqual(car.current_state(), CarState.WAIT.value)

        # Set state to Drive
        car.state = CarState.DRIVE
        car.encounter_obstacles()
        self.assertEqual(car.current_state(), CarState.STOP.value)

        car.is_safe()
        self.assertEqual(car.current_state(), CarState.DRIVE.value)

        car.encounter_obstacles()
        self.assertEqual(car.current_state(), CarState.STOP.value)

        car.is_unsafe()
        self.assertEqual(car.current_state(), CarState.STOP.value)

if __name__ == '__main__':
    unittest.main()
