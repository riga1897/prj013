import logging

from src.decorate_logs import logged
from utilities.utilities import get_project_root

logfile = get_project_root() / "logs" / "masks.log"
masks_logger = logging.getLogger("masks")
file_handler = logging.FileHandler(logfile, encoding="utf-8")
time_format = "%Y-%m-%d %H:%M:%S"
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt=time_format)
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)


@logged(module_name="masks")
def get_mask_card_number(card_number: str) -> str:
    """
    Функция маскировки номера банковской карты
    """

    if not card_number.isdigit():
        raise TypeError("Неверный тип данных")
    elif not 15 < len(card_number) < 17:
        raise ValueError("Неверная длина номера карты")
    else:
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


@logged(module_name="masks")
def get_mask_account(account: str) -> str:
    """
    Функция маскировки номера банковского счета
    """
    if not account.isdigit():
        raise TypeError("Неверный тип данных")
    elif not 19 < len(account) < 21:
        raise ValueError("Неверная длина номера счета")
    else:
        return f"**{account[-4:]}"


# if __name__ == "__main__":
#    my_card_number = "7000179228960636" #"СчётСчётСчётСчёт"
#    my_account = "73654108413013574305"
#    # print(len(my_card_number))
#    # print(len(my_account))
#    print(get_mask_card_number(my_card_number))
#    print(get_mask_account(my_account))
