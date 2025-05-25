import pytest


@pytest.fixture
def test_card_number():
    my_card_number = "7000792289606361"
    return my_card_number


@pytest.fixture
def test_card_number_masked():
    my_card_number_masked = "7000 79** **** 6361"
    return my_card_number_masked


@pytest.fixture
def test_account():
    my_test_account = "73654108430135874305"
    return my_test_account


@pytest.fixture
def test_account_masked():
    my_test_account_masked = "**4305"
    return my_test_account_masked


@pytest.fixture()
def test_date():
    my_test_date = "2024-03-11T02:26:18.671407"
    return my_test_date


@pytest.fixture()
def test_date_modified():
    my_test_date_modified = "11.03.2024"
    return my_test_date_modified


@pytest.fixture()
def test_state_executed():
    get_test_state = "EXECUTED"
    return get_test_state


@pytest.fixture()
def test_state_canceled():
    get_test_state = "CANCELED"
    return get_test_state


@pytest.fixture()
def test_filter_input_list():
    get_test_input_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    return get_test_input_list


@pytest.fixture()
def test_filtered_by_state_executed():
    get_test_filtered_by_state_executed = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    return get_test_filtered_by_state_executed


@pytest.fixture()
def test_filtered_by_state_canceled():
    get_test_filtered_by_state_canceled = [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    return get_test_filtered_by_state_canceled


@pytest.fixture()
def test_my_reverse_true():
    my_descending = True
    return my_descending


@pytest.fixture()
def test_my_reverse_false():
    my_descending = False
    return my_descending


@pytest.fixture()
def test_sort_by_date_result_rt():
    rt_result = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    return rt_result


@pytest.fixture()
def test_sort_by_date_result_rf():
    rf_result = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    return rf_result


@pytest.fixture()
def test_transactions():
    fixture_test_transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    return fixture_test_transactions


@pytest.fixture()
def test_currency():
    fixture_test_currency = "USD"
    return fixture_test_currency


@pytest.fixture()
def test_transactions_one_write():
    fixture_test_transactions_one_write = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    return fixture_test_transactions_one_write


@pytest.fixture()
def test_transactions_no_write():
    fixture_test_transactions_no_write = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    return fixture_test_transactions_no_write


@pytest.fixture()
def test_descriptions():
    fixture_test_descriptions = ["Перевод организации", "Перевод со счета на счет"]
    return fixture_test_descriptions


@pytest.fixture()
def test_one_transaction():
    fixture_test_one_transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]
    return fixture_test_one_transactions


@pytest.fixture()
def test_card_numbers():
    fixture_test_card_numbers = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    return fixture_test_card_numbers


@pytest.fixture()
def test_card_number_start():
    fixture_test_card_start = 1
    return fixture_test_card_start


@pytest.fixture()
def test_card_number_end():
    fixture_test_card_end = 5
    return fixture_test_card_end


@pytest.fixture()
def test_one_dictionary():
    fixture_test_one_dictionary = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    return fixture_test_one_dictionary


@pytest.fixture()
def test_card_number_big():
    fixture_test_card_big = 99999999999999999
    return fixture_test_card_big


@pytest.fixture()
def test_wrong_range_first():
    fixture_test_wrong_range_first = "Слишком большой номер первой карты."
    return fixture_test_wrong_range_first


@pytest.fixture()
def test_wrong_range_last():
    fixture_test_wrong_range_last = "Слишком большой номер последней карты."
    return fixture_test_wrong_range_last


@pytest.fixture()
def test_wrong_range_last_start():
    fixture_test_wrong_range_last_start = "Ошибка! Номер первой карты больше номера последней карты."
    return fixture_test_wrong_range_last_start


@pytest.fixture()
def test_get_amount():
    fixture_test_from_site = """
    {
        "date": "2018-02-22",
          "historical": "",
          "info":
              {
                  "rate": 148.972231,
                  "timestamp": 1519328414
              },
        "query":
            {
                "amount": 25,
                "from": "GBP",
                "to": "JPY"
            },
        "result": 3724.305775,
        "success": true
    }
    """
    return fixture_test_from_site
