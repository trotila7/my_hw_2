import logging
from typing import Union

masks_logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/log_masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.INFO)


def mask_card_1(card: Union[int, str]) -> str:
    masks_logger.info("Пользователь ввел номер карты")
    """Функция, которая маскирует номер карты в формат XXXX XX** **** XXXX"""
    num_card_str = list(str(card))
    mask_card_output = list()
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
        masks_logger.info("Карта замаскирована успешно")
    else:
        mask_card_output_str = "Вы ввели некорректный номер карты"
        masks_logger.debug("Пользователь некорректно ввел номер карты")
    return mask_card_output_str


def mask_card_2(card: Union[int, str]) -> str:
    """Функция, которая маскирует номер карты в формат **XXXX"""
    num_card_str = list(str(card))
    if len(num_card_str) == 16 or len(num_card_str) == 20:
        mask_card_output = num_card_str[-4:]
        mask_card_output.insert(0, "**")
        mask_card_output_str_2 = "".join(mask_card_output)
        masks_logger.info("Карта замаскирована успешно")
    else:
        mask_card_output_str_2 = "Вы ввели некорректный номер карты"
        masks_logger.debug("Пользователь некорректно ввел номер карты")
    return mask_card_output_str_2
