from typing import Any

from src.masks import mask_card_1, mask_card_2

num_user = input("Введите номер карты или счета")
data_str = "2018-07-11T02:26:18.671407"


def mask_card_3(card_or_account: Any) -> str:
    """Функция, которая маскирует номер карты или счета"""
    # good_starts = ("Visa", "Cчет", "Maestro", "MasterCard")
    if card_or_account.startswith("Счет"):
        num_card = card_or_account[-20:]
        masks_num_account = str(card_or_account[:-20] + mask_card_2(num_card))
        return masks_num_account
    elif card_or_account.startswith("Visa"):
        num_card = card_or_account[-16:]
        masks_num_card = str(card_or_account[:-16] + mask_card_1(num_card))
        return masks_num_card
    elif card_or_account.startswith("Maestro"):
        num_card = card_or_account[-16:]
        masks_num_card = str(card_or_account[:-16] + mask_card_1(num_card))
        return masks_num_card
    elif card_or_account.startswith("MasterCard"):
        num_card = card_or_account[-16:]
        masks_num_card = str(card_or_account[:-16] + mask_card_1(num_card))
        return masks_num_card
    else:
        masks_num_card = "Введен некорректный номер карты или счета"
        return masks_num_card


def data_transformation(data_input: str) -> str:
    """Функция, которая преобразовывает строку в форматы даты 11.07.2018"""
    day = data_input[8:10]
    month = data_input[5:7]
    year = data_input[:4]
    data_format = ".".join([day, month, year])
    return data_format


print(mask_card_3(num_user))
print(data_transformation(data_str))
