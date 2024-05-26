from typing import List


# Выход функции со статусом по умолчанию EXECUTED
def filter_dict(input_dict: List[dict], key_filter: str = "EXECUTED") -> List[dict]:
    """Функция, которая фильтрует словарь, у которых ключ state
    cодержит переданное в функцию значение"""
    filtered_dict = []
    for i in input_dict:
        if i["state"] == key_filter:
            filtered_dict.append(i)
    return filtered_dict


def sorted_dict(input_dict: List[dict], sorting_order: bool = True) -> List[dict]:
    """Функция, которая сортирует список словарей по дате, по умолчанию: по убыванию"""
    return sorted(input_dict, key=lambda x: x["date"], reverse=sorting_order)
