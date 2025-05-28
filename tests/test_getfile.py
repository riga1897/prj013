from unittest.mock import patch

import pandas as pd

from src.getfile import data_path, read_from_csv, read_from_xlsx


def test_read_valid_csv(test_get_file_result, my_csv_file=data_path / "transactions_test.csv"):
    """Тестирование корректного получения списка из CSV файла"""

    csv_data = read_from_csv(my_csv_file)
    result = list(csv_data)

    result_data = test_get_file_result
    assert result == result_data


@patch("builtins.open")
def test_file_csv_not_found(mock_open_csv):
    """Тестирование возвращения пустого списка, если файл CSV не найден"""
    # with patch ("builtins.open"):
    mock_open_csv.side_effect = FileNotFoundError
    result = read_from_csv("nonexistent.csv")
    assert result == []


@patch("src.getfile.csv.DictReader")
def test_file_invalid_format_csv(mock_open_csv, my_xlsx_file=data_path / "transactions_excel_test.xlsx"):
    """Тест возвращения пустого списка, если файл CSV содержит неверные данные"""
    mock_open_csv.side_effect = TypeError
    result = read_from_csv(my_xlsx_file)
    assert result == []


def test_read_valid_xlsx(test_get_file_result, my_xlsx_file=data_path / "transactions_excel_test.xlsx"):
    """Тестирование корректного получения списка из XLSX файла"""
    df = pd.read_excel(my_xlsx_file, na_filter=False)
    result = df.astype(str).to_dict(orient="records")
    result_data = test_get_file_result
    assert result == result_data


@patch("src.getfile.pd.read_excel")
def test_file_xlsx_not_found(mock_open_xlsx):
    """Тестирование возвращения пустого списка, если файл не найден"""
    # with patch ("builtins.open"):
    mock_open_xlsx.side_effect = FileNotFoundError
    result = read_from_xlsx("nonexistent.csv")
    assert result == []


@patch("src.getfile.csv.DictReader")
def test_file_invalid_format_xlsx(mock_open_xlsx, my_csv_file=data_path / "transactions_test.csv"):
    """Тестирование возвращения пустого списка, если файл XSLX содержит неверные данные"""
    mock_open_xlsx.side_effect = ValueError
    result = read_from_xlsx(my_csv_file)
    assert result == []
