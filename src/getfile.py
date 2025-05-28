import csv
from pathlib import Path
from typing import Any, List

import pandas as pd

from utilities.utilities import get_project_root

data_path: Path = get_project_root() / "data"


def read_from_csv(csv_file: Path, result: List[Any] = []):
    """Функция для считывания финансовых операций из файла CSV.
    Принимают путь к файлу в качестве аргумента.
    Выдаёт список словарей с транзакциями."""

    try:
        with open(csv_file, "r", encoding="UTF-8") as file:
            try:
                reader = csv.DictReader(file, delimiter=";")
                result = list(reader)
            except TypeError as err_type:
                print("Неверный тип данных")
                print(err_type)
    except FileNotFoundError:
        print("Файл не найден")

    return result


def read_from_xlsx(xlsx_file: Path, result: List[Any] = []):
    """Функция для считывания финансовых операций из файла XLSX.
    Принимают путь к файлу в качестве аргумента.
    Выдаёт список словарей с транзакциями."""

    try:
        result = pd.read_excel(xlsx_file, na_filter=False).astype(str).to_dict(orient="records")
    except ValueError as err_value:
        print("Неверный формат данных")
        print(err_value)
    except FileNotFoundError:
        print("Файл не найден")

    return result


# if __name__ == '__main__':
#
#     my_csv_file = data_path / "transactions_test.csv"
#     my_xlsx_file = data_path / "transactions_excel_test.xlsx"
#
#     #print(read_from_csv(my_csv_file))
#     #print(read_from_xlsx(my_xlsx_file))
