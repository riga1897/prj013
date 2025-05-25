import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(test_card_number, test_card_number_masked, test_account, test_account_masked):
    assert mask_account_card(test_card_number) == test_card_number_masked
    assert mask_account_card(test_account) == test_account_masked


@pytest.mark.parametrize(
    "wrong_type", ["", "СчётСчётСчётСчёт", "СчётСчётСчётСчётСчёт", "Счёт1234СчётСчёт", "СчётСчёт1234СчётСчёт"]
)
def test_get_mask_wrong_type(wrong_type):
    with pytest.raises(TypeError):
        mask_account_card(wrong_type)


@pytest.mark.parametrize(
    "wrong_length", ["700079228960636", "70007921289606361", "7365410843013587430", "736541084301358743051"]
)
def test_get_mask_wrong_length(wrong_length):
    with pytest.raises(ValueError):
        mask_account_card(wrong_length)


def test_get_date(test_date, test_date_modified):
    assert get_date(test_date) == test_date_modified


@pytest.mark.parametrize("wrong_datetime", ["", "2024-03-11 02:26:18.671407", "2024-03-11a02:26:18.671407"])
def test_get_date_wrong_datetime(wrong_datetime):
    with pytest.raises(ValueError):
        get_date(wrong_datetime)
