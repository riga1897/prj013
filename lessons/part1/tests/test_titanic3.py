import json
import pytest
import pandas as pd

# Здесь фикстура из теста предыдущего задания

def test_fare_per_passenger_by_class(titanic_df):
    expected_result = {'1': 62.2, '3': 7.3}
    assert fare_per_passenger_by_class(titanic_df) == json.dumps(expected_result)