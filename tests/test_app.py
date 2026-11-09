import base64
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd
import streamlit as st
from streamlit.testing.v1 import AppTest


PROJECT_DIR = Path(__file__).resolve().parents[1]


class AppTests(unittest.TestCase):
    def setUp(self):
        st.cache_data.clear()

    def load_app(self):
        return AppTest.from_file(
            str(PROJECT_DIR / "app.py"), default_timeout=30
        ).run()

    def test_charts_use_the_available_records(self):
        app = self.load_app()
        self.assertEqual(len(app.exception), 0)
        self.assertEqual(len(app.error), 0)
        self.assertIn("vehículos", app.header[0].value)
        charts = app.get("plotly_chart")
        self.assertEqual(len(charts), 2)
        data = pd.read_csv(PROJECT_DIR / "vehicles_us.csv")

        for chart, kind in zip(charts, ("histogram", "scattergl")):
            trace = json.loads(chart.proto.spec)["data"][0]
            self.assertEqual(trace["type"], kind)
            actual_x = np.frombuffer(
                base64.b64decode(trace["x"]["bdata"]), dtype=trace["x"]["dtype"]
            )
            expected = data.dropna(
                subset=["odometer"] if kind == "histogram" else ["odometer", "price"]
            )
            np.testing.assert_array_equal(actual_x, expected["odometer"])
            if kind == "scattergl":
                actual_y = np.frombuffer(
                    base64.b64decode(trace["y"]["bdata"]), dtype=trace["y"]["dtype"]
                )
                np.testing.assert_array_equal(actual_y, expected["price"])

    def test_checkboxes_control_each_chart_independently(self):
        app = self.load_app()
        for histogram, scatter in ((False, True), (True, False), (False, False), (True, True)):
            with self.subTest(histogram=histogram, scatter=scatter):
                app.checkbox[0].set_value(histogram)
                app.checkbox[1].set_value(scatter)
                app.run()
                self.assertEqual(len(app.exception), 0)
                types = [
                    json.loads(chart.proto.spec)["data"][0]["type"]
                    for chart in app.get("plotly_chart")
                ]
                expected = (["histogram"] if histogram else []) + (
                    ["scattergl"] if scatter else []
                )
                self.assertEqual(types, expected)

    def test_unreadable_csv_displays_a_message(self):
        with patch("pandas.read_csv", side_effect=FileNotFoundError):
            app = self.load_app()
        self.assertEqual(len(app.exception), 0)
        self.assertIn("No se pudo leer vehicles_us.csv", app.error[0].value)
        self.assertEqual(len(app.get("plotly_chart")), 0)


if __name__ == "__main__":
    unittest.main()
