import sys
sys.path.append('..')
from queue import Queue
from typing import List, Dict
from abc import ABC, abstractmethod
from car_state import CarState
from stack import Stack

class DriverlessCarSystem:
    def __init__(self):
        self.environment_data: Dict = {}
        self.sensors: List[Sensor] = []
        self.control_system: ControlSystem = None
        self.user_interface: UserInterface = None
        self.path = {}
        self.dataset = []
        self.loaded_model = False
        self.safety_system_connected = False

    def user_running_manual_mode(self):
        self.user_in_manual_mode = True

    def record_dataset(self, data):
        self.dataset.append(data)
        print(f"Recording data: {data}")
    
    def data_balancing(self, data_type):
        print("Data balancing")

    def load_model(self):
        print("Loading a model")
        self.loaded_model = True

    def apply_ml_model(self, camera_data, gps_data, environmental_data):
        print("Applying ML model")
        # Simulate applying an AI model to calculate the steering angle
        # In a real system, this would involve running a trained AI model
        # on input data to predict the steering angle.
        calculated_angle = 10.0  # Simulated value
        return calculated_angle

    def gather_environment_data(self):
        return self.environment_data

    def process_environment_data(self):
        print("Process enviroment data")
        return self.environment_data

    def plan_path(self):
        return self.path

    def execute_path(self, destination):
        return self.plan_path(self, destination)

class Sensor(DriverlessCarSystem):
    def __init__(self, sensor_id):
        super().__init__()
        self.sensor_id = sensor_id

    def read_data(self):
        print("Read sensor data")

class ControlSystem(DriverlessCarSystem):
    def __init__(self):
        super().__init__()
        self.speed = 0.0
        self.gps_data = []
        self.camera_data = []
        self.dataset = []
        self.safety_system: SafetySystem = None
        self.command_queue = Queue()
        self.user_in_manual_mode = False
        self.loaded_model = False
        self.command_stack = [] 

    def user_running_manual_mode(self):
        self.user_in_manual_mode = True

    def record_dataset(self, data):
        self.dataset.append(data)
        print(f"Recording data: {data}")
    
    def data_balancing(self, data_type):
        print("Data balancing")

    def prioritize_emergency_command(self, command):
        if command == "Emergency Stop":
            self.command_stack.append(command)
            self.emergency_signals = True
            print(f"Emergency command prioritized: {command}")
        else:
            self.command_stack.append(command)
            print(f"Command added to the stack: {command}")

    def execute_command(self):
        if self.command_queue:
            command = self.command_queue.pop()
            print(f"Executing command: {command}")
        else:
            print("No commands in the queue")

    def load_model(self):
        print("Loading a model")
        self.loaded_model = True

    def apply_ml_model(self, camera_data, gps_data, speed):
        print("Applying ML model")
        # Simulate applying an AI model to calculate the steering angle
        # In a real system, this would involve running a trained AI model
        # on input data to predict the steering angle.
        calculated_angle = 10.0  # Simulated value
        return calculated_angle

    def predict_steering_angle(self):
        return self.apply_ml_model(self.camera_data, self.gps_data, self.speed)

class SafetySystem(ControlSystem):
    def __init__(self):
        super().__init__()
        self.command_stack = Stack()
        self.car_state = CarState.DRIVE
        self.detect_collision = False

    def avoid_obstacle(self):
        pass

    def emergency_stop(self):
        if self.detect_collision:
                self.car_state = CarState.STOP
        pass

class UserInterface(ABC):
    def __init__(self):
        self.device_list = []
        self.command_queue = Queue()

    @abstractmethod
    def open_car_simulator(self):
        pass

    @abstractmethod
    def run_autonomous_mode(self):
        pass

    @abstractmethod
    def input_destination(self, device, destination):
        pass

    @abstractmethod
    def connect_device(self, device):
        pass

    @abstractmethod
    def disconnect_device(self, device):
        pass

class AndroidPhone(UserInterface):
    def __init__(self, camera, gps, compass):
        super().__init__()
        self.camera = camera
        self.gps = gps
        self.compass = compass
        self.connected = False

    def open_car_simulator(self):
        print("Open car simulator")

    def run_autonomous_mode(self):
        print("Running autonomous mode")

    def input_destination(self, destination):
        return destination

    def connect_device(self, device):
        self.connected = True

    def disconnect_device(self, device):
        self.connected = False

    def display_map(self, destination):
        if self.gps:
            location = 10
            print(f"Displaying map for destination: {destination} at location: {location}")
            return location
        else:
            print("GPS device not available. Cannot display the map.")

    def send_instructions(self, instructions):
        if self.device_list:
            for device in self.device_list:
                device.perform_action(instructions)
            print(f"Sent instructions to connected devices: {instructions}")
        else:
            print("No devices connected. Cannot send instructions.")

    def receive_status_updates(self):
        if self.device_list:
            for device in self.device_list:
                status = device.get_status()
                print(f"Received status update from device: {status}")
        else:
            print("No devices connected. Cannot receive status updates.")

    def connect_to_car(self):
        if self.device_list:
            for device in self.device_list:
                device.connect()
            print("Connected to the car.")
        else:
            print("No devices to connect. Cannot connect to the car.")

class AndroidTablet(UserInterface):
    def __init__(self, camera, gps, compass):
        super().__init__()
        self.camera = camera
        self.gps = gps
        self.compass = compass
        self.connected = False

    def open_car_simulator(self):
        print("Open car simulator")

    def run_autonomous_mode(self):
        print("Running autonomous mode")

    def input_destination(self, destination):
        return destination

    def connect_device(self, device):
        self.connected = True

    def disconnect_device(self, device):
        self.connected = False

    def display_map(self, destination):
        if self.gps:
            location = 10
            print(f"Displaying map for destination: {destination} at location: {location}")
            return location
        else:
            print("GPS device not available. Cannot display the map.")

    def send_instructions(self, instructions):
        if self.device_list:
            for device in self.device_list:
                device.perform_action(instructions)
            print(f"Sent instructions to connected devices: {instructions}")
        else:
            print("No devices connected. Cannot send instructions.")

    def receive_status_updates(self):
        if self.device_list:
            for device in self.device_list:
                status = device.get_status()
                print(f"Received status update from device: {status}")
        else:
            print("No devices connected. Cannot receive status updates.")

    def connect_to_car(self):
        if self.device_list:
            for device in self.device_list:
                device.connect()
            print("Connected to the car.")
        else:
            print("No devices to connect. Cannot connect to the car.")
