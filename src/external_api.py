import json
import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv("../.env")
API_KEY = os.getenv("API_KEY")

# status_code = 200
# result = '''{
#     "date": "2018-02-22",
#       "historical": "",
#       "info":
#           {
#               "rate": 148.972231,
#               "timestamp": 1519328414
#           },
#     "query":
#         {
#             "amount": 25,
#             "from": "GBP",
#             "to": "JPY"
#         },
#     "result": 3724.305775,
#     "success": true
# }'''


def get_converted_amount(my_amount: str, my_currency: str) -> str:
    """
    Функция принимает сумму и символ валюты из которой требуется конвертации в рубли.
    Возвращает сумму в рублях, эквивалентную принятой, в указанной валюте, сумме.
    """
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={my_currency}&amount={my_amount}"
    payload: Dict[str, str] = {}
    headers = {"apikey": API_KEY}
    response_from_site = requests.request("GET", url, headers=headers, data=payload)
    status_code = response_from_site.status_code

    if status_code != 200:
        amount = ""
    else:
        result = response_from_site.text  # response.text
        result_json = json.loads(result)
        amount = str(result_json.get("result"))

    return amount


# if __name__ == "__main__":
#     amount_rub = get_converted_amount('5', 'USD')
#     print(type(amount_rub))
#     print(amount_rub)
