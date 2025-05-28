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


@pytest.fixture
def test_get_file_result():
    fixture_csv_result = [
        {'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 'currency_name': 'Sol',
         'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
         'description': 'Перевод организации'},
        {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740',
         'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
         'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
        {'id': '593027', 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': '30368',
         'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097',
         'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
        {'id': '366176', 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': '29482',
         'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937',
         'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'},
        {'id': '5380041', 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': '23789',
         'currency_name': 'Peso', 'currency_code': 'UYU', 'from': '', 'to': 'Счет 23294994494356835683',
         'description': 'Открытие вклада'},
        {'id': '1962667', 'state': 'EXECUTED', 'date': '2023-10-22T09:43:32Z', 'amount': '18588',
         'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Mastercard 7286844946221431',
         'to': 'Счет 76145988629288763144', 'description': 'Перевод организации'},
        {'id': '5294458', 'state': 'EXECUTED', 'date': '2022-06-20T18:08:20Z', 'amount': '16836',
         'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Visa 2759011965877198',
         'to': 'Счет 38287443300766991082', 'description': 'Перевод с карты на карту'},
        {'id': '5429839', 'state': 'EXECUTED', 'date': '2023-06-23T19:46:34Z', 'amount': '25261',
         'currency_name': 'Hryvnia', 'currency_code': 'UAH', 'from': '', 'to': 'Счет 76768135089446747029',
         'description': 'Открытие вклада'},
        {'id': '3226899', 'state': 'EXECUTED', 'date': '2023-04-17T09:21:15Z', 'amount': '21680',
         'currency_name': 'Koruna', 'currency_code': 'CZK', 'from': '', 'to': 'Счет 88329674734590848775',
         'description': 'Открытие вклада'},
        {'id': '3176764', 'state': 'CANCELED', 'date': '2022-08-24T14:32:38Z', 'amount': '16652',
         'currency_name': 'Euro', 'currency_code': 'EUR', 'from': 'Mastercard 8387037425051294',
         'to': 'American Express 5556525473658852', 'description': 'Перевод с карты на карту'}]

    return fixture_csv_result


@pytest.fixture
def test_csv_file_content():
    fixture_test_csv_file_content = """id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту
593027;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;TZS;Visa 1959232722494097;Visa 6804119550473710;Перевод с карты на карту
366176;EXECUTED;2020-08-02T09:35:18Z;29482;Rupiah;IDR;Discover 0325955596714937;Visa 3820488829287420;Перевод с карты на карту
5380041;CANCELED;2021-02-01T11:54:58Z;23789;Peso;UYU;;Счет 23294994494356835683;Открытие вклада
1962667;EXECUTED;2023-10-22T09:43:32Z;18588;Peso;COP;Mastercard 7286844946221431;Счет 76145988629288763144;Перевод организации
5294458;EXECUTED;2022-06-20T18:08:20Z;16836;Yuan Renminbi;CNY;Visa 2759011965877198;Счет 38287443300766991082;Перевод с карты на карту
5429839;EXECUTED;2023-06-23T19:46:34Z;25261;Hryvnia;UAH;;Счет 76768135089446747029;Открытие вклада
3226899;EXECUTED;2023-04-17T09:21:15Z;21680;Koruna;CZK;;Счет 88329674734590848775;Открытие вклада
3176764;CANCELED;2022-08-24T14:32:38Z;16652;Euro;EUR;Mastercard 8387037425051294;American Express 5556525473658852;Перевод с карты на карту"""
    return fixture_test_csv_file_content
