from typing import List

list_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


# Выход функции со статусом по умолчанию EXECUTED
def filter_dict(input_dict: List[dict], key_filter: str = "EXECUTED") -> List[dict]:
    """Функция, которая фильтрует словарь, у которых ключ state
    cодержит переданное в функцию значение"""
    filtered_dict = []
    if len(input_dict) > 0:
        for i in input_dict:
            if i["state"] == key_filter:
                filtered_dict.append(i)
    return filtered_dict


def sorted_dict(input_dict: List[dict], sorting_order: bool = True) -> List[dict]:
    """Функция, которая сортирует список словарей по дате, по умолчанию: по убыванию"""
    return sorted(input_dict, key=lambda x: x["date"], reverse=sorting_order)


if __name__ == "__main__":
    print(filter_dict(list_dict))
    print(sorted_dict(list_dict))
