import unittest
import numpy as np
import joblib
import os


class TestModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        model_path = os.path.join(
            os.path.dirname(__file__), "../model/random_forest_model.pkl"
        )
        cls.model = joblib.load(model_path)

    def test_model_load(self):
        self.assertIsNotNone(self.model, "Model should be loaded")

    def test_prediction(self):
        input_data = np.array(
            [[1.0, 2.0, 3.0], [7.0, 8.0, 9.0]]
        )
        predictions = self.model.predict(input_data)
        self.assertEqual(
            len(predictions), 2, "Should return predictions for each input row"
        )
        self.assertIsInstance(predictions[0], float, "Prediction should be a float")


if __name__ == "__main__":
    unittest.main()
