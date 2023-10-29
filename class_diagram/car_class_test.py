import unittest
from car_class import DriverlessCarSystem, Sensor, ControlSystem, SafetySystem, AndroidPhone, AndroidTablet

class TestDriverlessCarSystem(unittest.TestCase):

    def setUp(self):
        self.car_system = DriverlessCarSystem()
        self.sensor = Sensor(sensor_id="123")
        self.control_system = ControlSystem()
        self.safety_system = SafetySystem()
        self.android_phone = AndroidPhone(camera=[1,4,5], gps=[35,102], compass=[1,34])
        self.android_tablet = AndroidTablet(camera=[3,6,], gps=[22,134], compass=[1,45])

    def test_record_dataset(self):
        data = "Sample data"
        self.car_system.record_dataset(data)
        self.assertIn(data, self.car_system.dataset)

    def test_gather_environment_data(self):
        data = {"temperature": 25, "humidity": 50}
        self.car_system.environment_data = data
        result = self.car_system.gather_environment_data()
        self.assertEqual(result, data)

    def test_load_model(self):
        self.car_system.load_model()
        self.assertTrue(self.car_system.loaded_model)

    def test_apply_ml_model(self):
        camera_data = [1, 2, 3]
        gps_data = [4, 5, 6]
        speed = 50  # Simulated speed
        result = self.control_system.apply_ml_model(camera_data, gps_data, speed)
        self.assertTrue(isinstance(result, float))


    def test_connect_device(self):
        self.android_phone.connect_device(self.sensor)
        self.assertTrue(self.android_phone.connected)

    def test_disconnect_device(self):
        self.android_phone.disconnect_device(self.sensor)
        self.assertFalse(self.android_phone.connected)

    def test_display_map_exit(self):
        destination = "Sample Destination"
        result = self.android_phone.display_map(destination)
        self.assertIsNotNone(result, "The result of display_map should not be None")

if __name__ == '__main__':
    unittest.main()
