import unittest
import json
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        """Set up the test client."""
        self.app = app.test_client()
        self.app.testing = True

    def test_predict_success(self):
        """Test the /predict endpoint for a valid request."""
        payload = {
            "bowling_type": "Bouncer",
            "shot_type": "Straight",
            "shot_timing": "Perfect"
        }
        response = self.app.post('/predict', 
                                 data=json.dumps(payload),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['outcome'], "6 runs")
        self.assertEqual(data['commentary'], "Thats massive and out of the ground.")

    def test_predict_invalid_input(self):
        """Test the /predict endpoint for invalid input."""
        payload = {
            "bowling_type": "Bouncer",
            "shot_type": "Straight"
        }
        response = self.app.post('/predict', 
                                 data=json.dumps(payload),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], "Invalid input. Required fields: bowling_type, shot_type, shot_timing.")

    def test_superover_success(self):
        """Test the /superover endpoint for a valid request."""
        payload = {
            "shots": [
                ["Straight", "Perfect"],
                ["Flick", "Good"],
                ["CoverDrive", "Late"],
                ["Pull", "Early"],
                ["SquareCut", "Perfect"],
                ["UpperCut", "Good"]
            ]
        }
        response = self.app.post('/superover', 
                                 data=json.dumps(payload),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('runs', data)
        self.assertIn('wickets', data)
        self.assertIn('commentary', data)
        self.assertIn('result', data)

    def test_superover_invalid_shots(self):
        """Test the /superover endpoint for invalid shots input."""
        payload = {
            "shots": [
                ["Straight", "Perfect"],
                ["Flick", "Good"],
                ["CoverDrive", "Late"],
                ["Pull", "Early"],
                ["SquareCut", "Perfect"],
                ["UpperCut"]
            ]
        }
        response = self.app.post('/superover', 
                                 data=json.dumps(payload),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], "Invalid shot input: ['UpperCut']. Each shot must be a tuple of (shot_name, shot_timing).")

    def test_superover_missing_shots_field(self):
        """Test the /superover endpoint for missing 'shots' field."""
        payload = {}
        response = self.app.post('/superover', 
                                 data=json.dumps(payload),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], "Invalid input. Shots field is required.")

    def test_superover_invalid_shots_length(self):
        """Test the /superover endpoint for incorrect number of shots."""
        payload = {
            "shots": [
                ["Straight", "Perfect"],
                ["Flick", "Good"]
            ]
        }
        response = self.app.post('/superover', 
                                 data=json.dumps(payload),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['error'], "Invalid input. Exactly 6 shots are required.")

if __name__ == '__main__':
    unittest.main()
