import json
import logging
from pathlib import Path
from typing import Any

from src.decorate_logs import logged
from src.generators import check_transactions_for_list
from utilities.utilities import get_project_root

logfile = get_project_root() / "logs" / "utils.log"
utils_logger = logging.getLogger("utils")
file_handler = logging.FileHandler(logfile, encoding="utf-8")
time_format = "%Y-%m-%d %H:%M:%S"
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt=time_format)
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)


@logged(module_name="utils")
def read_json_list(file_path: Path) -> Any:
    """
    Функция, которая принимает на вход путь до JSON-файла.
    Возвращает список словарей с данными о финансовых транзакциях
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = "[]"
    except FileNotFoundError:
        data = "[]"
    else:
        if not check_transactions_for_list(data):
            data = "[]"
    return data


#
# if __name__ == '__main__':
#     my_file = get_project_root() / "data" / "operations.json"
#     operations = read_json_list(my_file)
#     print(operations)
