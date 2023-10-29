import unittest
from unittest.mock import patch
from io import StringIO
from car_route_planning import CarStimulator, DriverScript, MLModel, simulate_sequence

class TestSequenceSimulation(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, sequence_function, expected_output, mock_stdout):
        sequence_function()
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_sequence_simulation(self):
        expected_output = "1.Open the car->2.Connection established->3.Run Autonomous->4.Pass sensor data and Load GCP ML Model->5.Model analyzes data->6.Predict path->7.Send Control"

        self.assertEqual(simulate_sequence(), expected_output)

if __name__ == '__main__':
    unittest.main()
