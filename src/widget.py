from typing import Any

from src.masks import mask_card_1, mask_card_2

num_user = input("Введите номер карты или счета")


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


print(mask_card_3(num_user))
