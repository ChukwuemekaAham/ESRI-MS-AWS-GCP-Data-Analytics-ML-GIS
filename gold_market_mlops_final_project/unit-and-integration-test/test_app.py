import unittest
import json
import numpy as np
from streamlit.testing import streamlit_test, create_test_runner
from streamlit import cli as stcli


def simulate_input():
    return json.dumps(
        {
            "input_data": [
                [1.0, 2.0, 3.0],
                [7.0, 8.0, 9.0],
            ],
            "params": {},
        }
    )


class TestApp(unittest.TestCase):
    def test_prediction(self):
        test_runner = create_test_runner()
        with streamlit_test(test_runner):
            test_runner.text_area = simulate_input()
            test_runner.button = True
            test_runner.run_script("app.py")
            self.assertIn("Predictions", test_runner.report_text)
            self.assertIn("Error", test_runner.report_text)
            self.assertNotIn("Invalid JSON format", test_runner.report_text)


if __name__ == "__main__":
    unittest.main()
