from time import strftime, strptime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(string_to_mask: str) -> str:
    """
    Функция маскировки номера банковской карты или номера банковского счета
    """
    string_list = string_to_mask.split()

    if not len(string_list) > 0:
        raise TypeError("Пустая строка")
    else:
        account_or_card = string_list[-1]

        if not account_or_card.isdigit():
            raise TypeError("Неверный тип данных")
        if len(account_or_card) == 16:
            account_or_card = get_mask_card_number(account_or_card)
            string_list[-1] = account_or_card
        elif len(account_or_card) == 20:
            account_or_card = get_mask_account(account_or_card)
            string_list[-1] = account_or_card
        else:
            raise ValueError("Неверная длина номера карты или счета")

    # result = str(string_list)[1:-1]

    return " ".join(string_list)


def get_date(date_to_modify: str) -> str:
    """
    Функция преобразования даты из одного формата в другой
    """
    # modified_day = ".".join(list(reversed(date_to_modify.split("T")[0].split("-"))))

    try:
        modified_day = strftime("%d.%m.%Y", strptime(date_to_modify, "%Y-%m-%dT%H:%M:%S.%f"))
    except ValueError:
        raise ValueError("Неверный формат даты")
    else:
        return modified_day


# if __name__ == "__main__":
#    my_card_number = "70007922896061361"
#    my_account = "736541084601358741305"
#    print(get_mask_card_number(my_card_number))
#    print(get_mask_account(my_account))
