from typing import Any, Dict, Generator, Iterator, List

from src.external_api import get_converted_amount


def check_transactions_for_list(transactions_for_check: List[Any]) -> bool:
    """
    Функция проверяет, являются ли входные данные списком.
    Если да, то функция возвращает значение True.
    Если нет, то функция возвращает значение False.
    """
    is_list = isinstance(transactions_for_check, list)
    if not is_list:
        this_is_list = False
    elif not len(transactions_for_check) > 0:
        this_is_list = False
    else:
        this_is_list = True

    return this_is_list


def check_transaction_for_dict(transaction_for_check: Dict) -> bool:
    """
    Функция проверяет, являются ли входные данные словарём.
    Если да, то функция возвращает значение True.
    Если нет, то функция возвращает значение False.
    """
    is_dict = isinstance(transaction_for_check, dict)
    if not is_dict:
        this_is_dict = False
    else:
        this_is_dict = True

    return this_is_dict


def filter_by_currency(transactions: List[Any], currency: str) -> Iterator:
    """
    Функция принимает на вход список словарей, представляющих транзакции и должна
    возвращать итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной (например, USD)
    """
    if not check_transactions_for_list(transactions):
        yield
    else:
        for transaction in transactions:
            if not check_transaction_for_dict(transaction):
                yield
            else:
                my_currency: str = transaction.get("operationAmount", {}).get("currency", {}).get("code", {})
                if not my_currency == currency:
                    yield
                else:
                    yield transaction


def transaction_descriptions(transactions: List[Any]) -> Generator:
    """
    Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    if not check_transactions_for_list(transactions):
        yield
    else:
        for transaction in transactions:
            if not check_transaction_for_dict(transaction):
                yield
            else:
                my_description = transaction.get("description", {})
                if not my_description:
                    yield
                else:
                    yield my_description


def format_card_number(card_number_to_format: int | str) -> str:
    """Функция преобразовывает числовое значение карты в текстовый формат для форматированного вывода"""
    my_card_number_to_format = str(f"{int(card_number_to_format):016}")
    my_card_number = (
        f"{my_card_number_to_format[0:4]} {my_card_number_to_format[4:8]} "
        f"{my_card_number_to_format[8:12]} {my_card_number_to_format[12:]}"
    )
    return my_card_number


def card_number_generator(my_start: int, my_end: int) -> Generator:
    """
    Функция, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
    """
    my_start_is_valid = True
    my_end_is_valid = True

    # if not type(my_start) is int:
    #     my_start = my_start.replace(" ", "")
    #     if not my_start.isdigit():
    #         yield "Неверный формат для номера первой карты"
    #         my_start_is_valid = False
    #     else:
    #         my_start = int(my_start)
    if my_start > 9999999999999999:
        my_start_is_valid = False
        yield "Слишком большой номер первой карты."

    # if not type(my_end) is int:
    #     my_end = my_end.replace(" ", "")
    #     if not my_end.isdigit():
    #         yield "Неверный формат для номера последней карты"
    #         my_end_is_valid = False
    #     else:
    #         my_end = int(my_end)
    if my_end > 9999999999999999:
        my_end_is_valid = False
        yield "Слишком большой номер последней карты."

    if my_start_is_valid and my_end_is_valid:
        if my_start > my_end:
            yield "Ошибка! Номер первой карты больше номера последней карты."
        else:
            if my_start_is_valid and my_end_is_valid:
                my_end += 1
                for my_card_number in range(my_start, my_end):
                    my_card_number_formated = format_card_number(my_card_number)
                    yield my_card_number_formated


def get_amount(transactions: List) -> Generator:
    for transaction in transactions:
        my_operation_amount: Dict = transaction.get("operationAmount", {})
        my_amount = str(my_operation_amount.get("amount", {}))
        my_currency = str(my_operation_amount.get("currency", {}).get("code", {}))

        if not my_currency == "RUB":
            my_amount = get_converted_amount(my_amount, my_currency)
            # my_amount = "111111"
        yield f"{my_amount}"
