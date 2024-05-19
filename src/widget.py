from typing import Union
import masks

num_user = input("Введите номер карты или счета")


def mask_card_3(card_or_account):
    '''Функция, которая маскирует номер карты или счета '''
    good_starts = ("Visa", "Cчет", "Maestro", "MasterCard")
    if card_or_account.startswith(good_starts):

    else:
        print("Некорректно введен номер карты или счета")




print(mask_card_3(num_user))
