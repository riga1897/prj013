from unittest.mock import patch

import pytest

from src.generators import (card_number_generator, check_transaction_for_dict, check_transactions_for_list,
                            filter_by_currency, format_card_number, get_amount, transaction_descriptions)


def test_check_transactions_for_list(test_transactions, test_one_dictionary):
    is_list = check_transactions_for_list(test_transactions)
    assert is_list
    is_list = check_transactions_for_list(test_one_dictionary)
    assert not is_list
    is_list = check_transactions_for_list([])
    assert not is_list


def test_check_transaction_for_dict(test_one_dictionary):
    is_dict = check_transaction_for_dict(test_one_dictionary)
    assert is_dict
    is_dict = check_transaction_for_dict({})
    assert is_dict


def test_filter_by_currency(test_transactions, test_currency):
    usd_transactions = filter_by_currency(test_transactions, test_currency)
    assert next(usd_transactions) == test_transactions[0]
    assert next(usd_transactions) == test_transactions[1]


def test_filter_by_currency_one_write(test_transactions, test_transactions_one_write, test_currency):
    usd_transactions = filter_by_currency(test_transactions_one_write, test_currency)
    assert next(usd_transactions) == test_transactions[0]
    assert next(usd_transactions) is None


def test_filter_by_currency_no_write(test_transactions_no_write, test_currency):
    usd_transactions = filter_by_currency(test_transactions_no_write, test_currency)
    assert next(usd_transactions) is None
    assert next(usd_transactions) is None


@pytest.mark.parametrize(
    "wrong_transactions",
    [
        None,
        "",
        "q1w2",
        [],
        ["qwer"],
        ["a", "b"],
        dict(),
        [
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ],
    ],
)
def test_filter_by_currency_with_wrong_transactions(wrong_transactions, test_currency):
    usd_transactions = filter_by_currency(wrong_transactions, test_currency)
    assert next(usd_transactions) is None


def test_transaction_descriptions(test_transactions, test_descriptions):
    my_test_description = transaction_descriptions(test_transactions)
    assert next(my_test_description) == test_descriptions[0]
    assert next(my_test_description) == test_descriptions[1]


def test_transaction_one_descriptions(test_one_transaction, test_descriptions):
    my_test_description = transaction_descriptions(test_one_transaction)
    assert next(my_test_description) == test_descriptions[0]


@pytest.mark.parametrize(
    "test_wrong_transactions",
    [
        None,
        "",
        "q1w2",
        [],
        ["qwer"],
        ["a", "b"],
        dict(),
        [
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ],
    ],
)
def test_wrong_transaction_descriptions(test_wrong_transactions, test_descriptions):
    my_test_description = transaction_descriptions(test_wrong_transactions)
    assert next(my_test_description) is None


@pytest.mark.parametrize("test_card_format", [1, "1"])
def test_format_card_number(test_card_format, test_card_numbers):
    test_write_card_number = format_card_number(test_card_format)
    assert test_write_card_number == test_card_numbers[0]


def test_card_number_generator(test_card_numbers, test_card_number_start, test_card_number_end):
    my_test_card_number = list(
        card_number for card_number in card_number_generator(test_card_number_start, test_card_number_end)
    )
    my_test_card_start_number = card_number_generator(test_card_number_start, test_card_number_start)
    my_test_card_end_number = card_number_generator(test_card_number_end, test_card_number_end)
    assert test_card_numbers[0] == next(my_test_card_start_number)
    assert test_card_numbers[4] == next(my_test_card_end_number)
    assert my_test_card_number == test_card_numbers


def test_card_number_generator_big_number(
    test_card_number_big,
    test_card_number_start,
    test_card_number_end,
    test_wrong_range_first,
    test_wrong_range_last,
    test_wrong_range_last_start,
):
    my_test_big_card_number_start = card_number_generator(test_card_number_big, test_card_number_big)
    my_test_big_card_number_last = card_number_generator(test_card_number_start, test_card_number_big)
    my_test_big_card_number_last_start = card_number_generator(test_card_number_end, test_card_number_start)
    assert next(my_test_big_card_number_start) == test_wrong_range_first
    assert next(my_test_big_card_number_last) == test_wrong_range_last
    assert next(my_test_big_card_number_last_start) == test_wrong_range_last_start


@patch("src.external_api.requests.request")
def test_get_user_data_failure(mocked_get, test_transactions_one_write, test_get_amount):
    mocked_request = test_get_amount
    with patch("requests.request") as mocked_get:
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.text = mocked_request
        test_amounts = get_amount(test_transactions_one_write)
        assert next(test_amounts) == "3724.305775"
        assert next(test_amounts) == "79114.93"
