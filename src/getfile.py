import csv
import pandas as pd

from utilities.utilities import get_project_root

data_path = get_project_root() / "data"

csv_file = data_path / "transactions_test.csv"
excel_file = data_path / "transactions_excel_test.xlsx"

with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    result = list(reader)

    print(len(result))


df = pd.read_excel(excel_file, )
result = df.to_dict(orient='records')

print(len(result))

