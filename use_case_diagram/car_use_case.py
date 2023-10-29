class CarSimulator:
    def __init__(self):
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

class Sensor:
    def __init__(self):
        self.camera_data = []
        self.gps_data = []
        self.environmental_data = []
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, data):
        for observer in self.observers:
            observer.update(data)

    def record_dataset(self, data, data_type):
        if data_type == 'camera':
            self.camera_data.append(data)
            print(f"Recording camera data: {data}")
        elif data_type == 'gps':
            self.gps_data.append(data)
            print(f"Recording GPS data: {data}")
        elif data_type == 'environmental':
            self.environmental_data.append(data)
            print(f"Recording environmental data: {data}")
        else:
            print(f"Unknown data type: {data_type}")

    def data_balancing(self, data_type):
        if data_type == 'camera':
            print("Balancing camera data")
        elif data_type == 'gps':
            print("Balancing GPS data")
        elif data_type == 'environmental':
            print("Balancing environmental data")
        else:
            print(f"Unknown data type: {data_type}")

    def open_sensor(self):
        print("Opening a sensor")

        # Check for new data and notify the observers.
        for data_type in ['camera', 'gps', 'environmental']:
            if data_type == 'camera' and self.camera_data:
                self.notify_observers(self.camera_data[-1])
            elif data_type == 'gps' and self.gps_data:
                self.notify_observers(self.gps_data[-1])
            elif data_type == 'environmental' and self.environmental_data:
                self.notify_observers(self.environmental_data[-1])

class ControlSystem:
    def __init__(self):
        self.speed = 0
        self.steering_angle = 0
        self.dataset = []
        self.emergency_signals = False
        self.command_stack = []  # Stack for handling commands
        self.user_in_manual_mode = False  
        self.loaded_model = False

    def user_running_manual_mode(self):
        self.user_in_manual_mode = True

    def record_dataset(self, data):
        self.dataset.append(data)
        print(f"Recording data: {data}")

    def open_safety_system(self):
        print("Opening the safety system")

    def prioritize_emergency_command(self, command):
        if command == "Emergency Stop":
            self.command_stack.append(command)
            self.emergency_signals = True  
            print(f"Emergency command prioritized: {command}")
        else:
            self.command_stack.append(command)
            print(f"Command added to the stack: {command}")

    def execute_command(self):
        if self.command_stack:
            command = self.command_stack.pop()
            print(f"Executing command: {command}")
        else:
            print("No commands in the stack")

    def load_model(self):
        print("Loading a model")
        self.loaded_model = True

    def apply_cgp_model(self, camera_data, gps_data, environmental_data):
        print("Applying CGP model")
        # Simulate applying an AI model to calculate the steering angle
        # In a real system, this would involve running a trained AI model
        # on input data to predict the steering angle.
        calculated_angle = 10  # Simulated value
        return calculated_angle

    def predict_steering_angle(self, sensor):
        if self.loaded_model:
            return self.apply_cgp_model(
                sensor.camera_data[-1], sensor.gps_data[-1], sensor.environmental_data[-1]
            )
        else:
            print("Model not loaded. Cannot predict steering angle.")
            return None
        
class Observer:
    def update(self, data):
        pass  

class MyObserver(Observer):
    def __init__(self):
        self.was_notified = False
        self.received_data = None

    def update(self, data):
        self.was_notified = True
        self.received_data = data
        print(f"Received new data: {data}")

class User:
    def __init__(self, control_system: ControlSystem):
        self.car_simulator = CarSimulator()
        self.command_queue = []  # Queue for handling user requests
        self.control_system = control_system

    def open_car_simulator(self):
        self.car_simulator.open()
        print("Opened the car simulator")

    def run_manual_mode(self):
        self.control_system.user_running_manual_mode()
        print("Running manual mode")

    def run_autonomous_mode(self):
        print("Running autonomous mode")

    def run_driver_script(self):
        while self.command_queue:
            command = self.command_queue.pop(0)
            print(f"Executing user request: {command}")

    def add_user_request(self, request):
        self.command_queue.append(request)
        print(f"Added user request to the queue: {request}")

if __name__ == "__main__":
    control_system = ControlSystem() 
    user = User(control_system)  
    sensor = Sensor()  

    user.open_car_simulator()

    sensor.add_observer(MyObserver())
    sensor.record_dataset("Camera data 1", "camera")
    sensor.record_dataset("GPS data 1", "gps")
    sensor.record_dataset("Environmental data 1", "environmental")

    sensor.data_balancing('camera')
    sensor.data_balancing('gps')   
    sensor.data_balancing('environmental') 
    sensor.open_sensor()

    control_system.record_dataset("Speed: 100 km/h")
    control_system.record_dataset("Temperature: 25°C")

    user.open_car_simulator()
    user.add_user_request("Stop the car")
    user.add_user_request("Drop off passengers") 
    user.add_user_request("Change destination to the airport")
    user.run_driver_script()

    control_system.open_safety_system()
    control_system.load_model()
    control_system.apply_cgp_model("Camera data", "Gps data", "Environmental data")
    control_system.predict_steering_angle(sensor)
    
    
