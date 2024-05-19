from typing import Union

num_card = input("Введите номер карты")


def mask_card_1(card: Union[int, str]) -> str:
    """Функция, которая маскирует номер карты в формат XXXX XX** **** XXXX"""
    num_card_str = list(str(card))
    mask_card_output = list()
    mask_card_output_str = str()
    if len(num_card_str) == 16:
        for i, num in enumerate(num_card_str):
            if i <= 5:
                mask_card_output.append(num)
            if 5 < i <= 11:
                mask_card_output.append("*")
            if 11 < i <= 15:
                mask_card_output.append(num)
        mask_card_output.insert(4, " ")
        mask_card_output.insert(9, " ")
        mask_card_output.insert(14, " ")
        mask_card_output_str = "".join(mask_card_output)
    else:
        mask_card_output_str = "Вы ввели некорректный номер карты"
    return mask_card_output_str


def mask_card_2(card: Union[int, str]) -> str:
    """Функция, которая маскирует номер карты в формат **XXXX"""
    num_card_str = list(str(card))
    mask_card_output = list()
    mask_card_output_str_2 = str()
    if len(num_card_str) == 16:
        mask_card_output = num_card_str[12:]
        mask_card_output.insert(0, "**")
        mask_card_output_str_2 = "".join(mask_card_output)
    else:
        mask_card_output_str_2 = "Вы ввели некорректный номер карты"
    return mask_card_output_str_2


print(mask_card_1(num_card))
print(mask_card_2(num_card))
