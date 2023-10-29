import unittest
from unittest.mock import patch
from io import StringIO
from car_autonomous_mode_intersection import IntersectionLogic

class TestIntersectionLogic(unittest.TestCase):
    def setUp(self):
        self.intersection = IntersectionLogic()

    @patch('sys.stdout', new_callable=StringIO)
    def test_intersection_action_all_not(self, mock_stdout):
        self.intersection.reached_other_side = False
        self.intersection.at_stop_sign = False
        self.intersection.others_at_intersection = False

        expected_output = "Drive forward\n"
        max_cycles = 5

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.intersection.get_intersection_action()
            actual_output = mock_stdout.getvalue()
        expected_output *= max_cycles 
        expected_output += "Finish Cycle\n"

        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_intersection_action_at_stop_sign(self, mock_stdout):
        self.intersection.reached_other_side = False
        self.intersection.at_stop_sign = True
        self.intersection.others_at_intersection = False

        expected_output = "Stop\nWait\n"
        max_cycles = 5

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.intersection.get_intersection_action()
            actual_output = mock_stdout.getvalue()
        expected_output *= max_cycles 
        expected_output += "Finish Cycle\n"

        self.assertEqual(actual_output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_intersection_action_at_stop_sign_and_others_at_intersection(self, mock_stdout):
        self.intersection.reached_other_side = False
        self.intersection.at_stop_sign = True
        self.intersection.others_at_intersection = True

        expected_output = "Stop\nDrive forward\n"
        max_cycles = 5

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.intersection.get_intersection_action()
            actual_output = mock_stdout.getvalue()
        expected_output *= max_cycles 
        expected_output += "Finish Cycle\n"

        self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()
