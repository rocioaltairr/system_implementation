class CarStimulator:
    def open_car(self):
        return "1.Open the car"
    
    def run_autonomous(self):
        return "3.Run Autonomous"

class DriverScript:
    def connection_established(self):
        return "2.Connection established"

    def pass_sensor_data_and_load_ml_model(self):
        return "4.Pass sensor data and Load GCP ML Model"

    def send_control(self):
        return "7.Send Control"

class MLModel:
    def predict_path(self):
        return "6.Predict path"
    
    def analyze_data(self):
        return "5.Model analyzes data"

def simulate_sequence():
    car_stimulator = CarStimulator()
    driver_script = DriverScript()
    ml_model = MLModel()

    sequence = []

    message = car_stimulator.open_car()
    sequence.append(message)

    message = driver_script.connection_established()
    sequence.append(message)

    message = car_stimulator.run_autonomous()
    sequence.append(message)

    message = driver_script.pass_sensor_data_and_load_ml_model()
    sequence.append(message)

    message = ml_model.analyze_data()
    sequence.append(message)

    message = ml_model.predict_path()
    sequence.append(message)

    message = driver_script.send_control()
    sequence.append(message)

    return "->".join(sequence)

if __name__ == "__main__":
    result = simulate_sequence()
    print(result)
