from unittest.mock import patch, mock_open

from src.getfile import read_from_csv, data_path, read_from_xlsx


#@patch("builtins.open")
def test_read_valid_csv(test_csv_file_content, test_get_file_result):
    """Тест корректного получения списка из CSV файла"""
    csv_data = test_csv_file_content
    result_data = test_get_file_result

    with patch("builtins.open", mock_open(read_data=csv_data)):
        result = read_from_csv("dummy_path.csv")
        assert result == result_data


@patch("builtins.open")
def test_file_csv_not_found(mock_open_csv):
    """Тест возвращения пустого списка, если файл не найден"""
    # with patch ("builtins.open"):
    mock_open_csv.side_effect = FileNotFoundError
    result = read_from_csv("nonexistent.csv")
    assert result == "[]"

@patch("src.getfile.csv.DictReader")
def test_file_invalid_format_csv(mock_open_csv):

        my_csv_file = data_path / "transactions_excel_test.xlsx"
        mock_open_csv.side_effect = TypeError
        result = read_from_csv(my_csv_file)
        assert result == "[]"


