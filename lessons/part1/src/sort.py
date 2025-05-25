import os
from datetime import datetime

import pandas as pd

def read_transactions_excel_and_output(file_path: str, date: str) -> list[dict[str, str]]:
    """Функция для считывания финансовых операций из Excel"""

    bas_dir = os.path.dirname(__file__)
    full_path = os.path.join(bas_dir, file_path)

    excel_data = pd.read_excel(full_path)
    excel_data = excel_data.fillna(value='')

    # Преобразуем строки в datetime
    excel_data['Дата операции'] = pd.to_datetime(excel_data['Дата операции'],
                                                 format='%d.%m.%Y %H:%M:%S')

    # Преобразуем входную дату в datetime
    date_obj = datetime.strptime(date, '%d.%m.%Y').date()

    # Получаем первый день месяца
    first_day = date_obj.replace(day=1)

    # Фильтруем по диапазону дат
    date_df = excel_data[
        (excel_data['Дата операции'].dt.date >= first_day) &
        (excel_data['Дата операции'].dt.date <= date_obj)
        ]

    return date_df