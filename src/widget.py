from typing import Union
import masks

num_user = input("Введите номер карты или счета")


def mask_card_3(card_or_account):
    '''Функция, которая маскирует номер карты или счета '''
    good_starts = ("Visa", "Cчет", "Maestro", "MasterCard")
    if card_or_account.startswith(good_starts):
        if card_or_account.startswith("Счет"):
            masks.mask_card_2(card_or_account)
        else:
            num_card = card_or_account[-16:]
            masks.mask_card_1(num_card)
    else:
        return "Некорректно введен номер карты или счета"


print(mask_card_3(num_user))
