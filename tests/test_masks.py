import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(test_card_number, test_card_number_masked):
    assert get_mask_card_number(test_card_number) == test_card_number_masked


@pytest.mark.parametrize("wrong_card_type", ["", "СчётСчётСчётСчёт"])
def test_get_mask_card_wrong_type(wrong_card_type):
    assert get_mask_card_number(wrong_card_type) == "Error, Неверный тип данных"


#     with pytest.raises(TypeError):
#         get_mask_card_number(wrong_card_type)


@pytest.mark.parametrize("wrong_card_length", ["700079228960636", "70007921289606361"])
def test_get_mask_card_number_wrong_length(wrong_card_length):
    assert get_mask_card_number(wrong_card_length) == "Error, Неверная длина номера карты"


#     with pytest.raises(ValueError):
#         get_mask_card_number(wrong_card_length)


def test_get_mask_account(test_account, test_account_masked):
    assert get_mask_account(test_account) == test_account_masked


@pytest.mark.parametrize("wrong_account_type", ["", "СчётСчётСчётСчётСчёт"])
def test_get_mask_account_wrong_type(wrong_account_type):
    assert get_mask_account(wrong_account_type) == "Error, Неверный тип данных"


#     with pytest.raises(TypeError):
#         get_mask_account(wrong_account_type)
#
#
@pytest.mark.parametrize("wrong_account_length", ["7365410843013587430", "736541084301358743051"])
def test_get_mask_account_wrong_length(wrong_account_length):
    assert get_mask_account(wrong_account_length) == "Error, Неверная длина номера счета"


#     with pytest.raises(ValueError):
#         get_mask_account(wrong_account_length)
