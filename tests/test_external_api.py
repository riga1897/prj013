from unittest.mock import Mock, patch

import requests

from src.external_api import get_converted_amount


def test_get_converted_amount(test_get_amount):
    """Тест корректного получения данных с сайта"""
    mocked_request = test_get_amount
    with patch("requests.request") as mocked_get:
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.text = mocked_request
        result = get_converted_amount("5", "USD")
        assert result == "3724.305775"


@patch("src.external_api.requests.request")
def test_get_user_data_failure(mocked_response):
    """Тест корректной обработки ошибки получения данных с сайта"""
    mocked_response = Mock()
    with patch("requests.request") as mocked_get:
        mocked_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
        mocked_get.return_value = mocked_response
        result = get_converted_amount("5", "USD")
        assert result == ""
