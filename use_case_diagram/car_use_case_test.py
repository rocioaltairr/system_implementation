import unittest
from car_use_case import CarSimulator, Sensor, ControlSystem, User, MyObserver

class TestCarSimulator(unittest.TestCase):
    def test_car_simulator_open(self):
        car_simulator = CarSimulator()
        car_simulator.open()
        self.assertTrue(car_simulator.is_open)

    def test_car_simulator_close(self):
        car_simulator = CarSimulator()
        car_simulator.open()
        car_simulator.close()
        self.assertFalse(car_simulator.is_open)

class TestSensor(unittest.TestCase):
    def test_sensor_add_observer(self):
        sensor = Sensor()
        observer = MyObserver()
        sensor.add_observer(observer)
        self.assertIn(observer, sensor.observers)

    def test_sensor_remove_observer(self):
        sensor = Sensor()
        observer = MyObserver()
        sensor.add_observer(observer)
        sensor.remove_observer(observer)
        self.assertNotIn(observer, sensor.observers)

    def test_sensor_record_dataset(self):
        sensor = Sensor()
        data_type = "camera"
        data = "Camera data"
        sensor.record_dataset(data, data_type)
        self.assertIn(data, sensor.camera_data)

    def test_sensor_record_unknown_data_type(self):
        sensor = Sensor()
        data_type = "unknown_type"
        data = "Some data"
        sensor.record_dataset(data, data_type)
        self.assertNotIn(data, sensor.camera_data)
        self.assertNotIn(data, sensor.gps_data)
        self.assertNotIn(data, sensor.environmental_data)

class TestControlSystem(unittest.TestCase):
    def test_control_system_user_running_manual_mode(self):
        control_system = ControlSystem()
        control_system.user_running_manual_mode()
        self.assertTrue(control_system.user_in_manual_mode)

    def test_control_system_prioritize_emergency_stop(self):
        control_system = ControlSystem()
        control_system.prioritize_emergency_command("Emergency Stop")
        self.assertTrue(control_system.emergency_signals)
        self.assertIn("Emergency Stop", control_system.command_stack)

    def test_control_system_prioritize_non_emergency_command(self):
        control_system = ControlSystem()
        control_system.prioritize_emergency_command("Another Command")
        self.assertFalse(control_system.emergency_signals)
        self.assertIn("Another Command", control_system.command_stack)

class TestUser(unittest.TestCase):
    def test_user_open_car_simulator(self):
        user = User(ControlSystem())
        user.open_car_simulator()
        self.assertTrue(user.car_simulator.is_open) 
    
    def test_user_add_and_execute_commands(self):
        user = User(ControlSystem())
        user.add_user_request("Command 1")
        user.add_user_request("Command 2")
        user.add_user_request("Command 3")

        expected_executed_commands = ["Command 1", "Command 2", "Command 3"]
        self.assertListEqual(user.command_queue, expected_executed_commands)

if __name__ == '__main__':
    unittest.main()