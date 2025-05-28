import json
from unittest.mock import mock_open, patch

from src.utils import read_json_list


def test_read_valid_list_json(test_transactions):
    """Тест корректного получения списка из JSON файла"""
    test_data = test_transactions
    json_data = json.dumps(test_data)

    with patch("builtins.open", mock_open(read_data=json_data)):
        result = read_json_list("dummy_path.json")
        assert result == test_data


def test_read_non_list_json_raises_error(test_one_dictionary):
    """Тест корректного получения данных из JSON файла, не являющихся списком"""
    test_data = test_one_dictionary
    json_data = json.dumps(test_data)
    with patch("builtins.open", mock_open(read_data=json_data)):
        result = read_json_list("dummy_path.json")
        assert result == "[]"


def test_invalid_json_raises_error() -> None:
    """Тест возвращения пустого списка, если файл содержит неверно сформированные данные"""
    invalid_json = "{not valid json}"
    with patch("builtins.open", mock_open(read_data=invalid_json)):
        result = read_json_list("dummy_path.json")
        assert result == "[]"


@patch("src.utils.json.load")
def test_file_not_found(mock_json_load):
    """Тест возвращения пустого списка, если файл не найден"""
    mock_json_load.side_effect = FileNotFoundError
    result = read_json_list("nonexistent.json")
    assert result == "[]"
