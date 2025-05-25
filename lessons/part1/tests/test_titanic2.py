import pytest
import pandas as pd

from lessons.part1.src.titanic2 import filter_passengers


# Здесь фикстура из теста предыдущего задания

def test_filter_passengers(titanic_df):
    expected_result = titanic_df.iloc[1:4].to_json(orient='records')
    assert filter_passengers(titanic_df) == expected_result