import csv
import pandas as pd

from utilities.utilities import get_project_root

data_path = get_project_root() / "data"

def read_from_csv(csv_file, result="[]"):

    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            try:
                reader = csv.DictReader(file, delimiter=';')
                result = list(reader)
            except TypeError as err_type:
                print('Неверный тип данных')
                print(err_type)
    except FileNotFoundError:
        print('Файл не найден')

    return result


def read_from_xlsx(xlsx_file, result="[]"):
    try:
        df = pd.read_excel(xlsx_file, na_filter=False)
        result = df.to_dict(orient='records')
    except ValueError as err_value:
        print('Неверный формат данных')
        print(err_value)
    except FileNotFoundError:
        print('Файл не найден')

    return result

#
# df = pd.read_excel(excel_file, na_filter=False)
# my_result = df.to_dict(orient='records')

#print(my_result)


if __name__ == '__main__':

    my_csv_file = data_path / "transactions_test.csv"
    my_xlsx_file = data_path / "transactions_excel_test.xlsx"


    print(read_from_csv(my_csv_file))
    print(read_from_xlsx(my_xlsx_file))