from typing import Iterable, Iterator


def filter_by_currency(input_list: Iterable[dict], code: str = "USD") -> Iterator[dict]:
    """ Функция, которая принимает список словарей с банковскими операциями и возвращает
    итератор, который выдает по очереди операции, в которых указана заданная валюта """
    for transaction in input_list:
        if transaction["operationAmount"]["currency"]["code"] == code:
            yield transaction


def transaction_descriptions(input_list: Iterable[dict]) -> Iterator[dict]:
    """ Функция принимает список словарей и возвращает описание каждой операции по очереди """
    for transaction in input_list:
        yield transaction["description"]


def card_number_generator(a, b):
    """ Функция, которая генерирует номера банковских карт, в формате XXXX XXXX XXXX XXXX
    (диапазоны передаются как параметры генератора) """
    for number in range(a, b + 1):
        new_card_number = list(str(number))
        while len(new_card_number) < 16:
            new_card_number.insert(0, "0")
        new_card_number.insert(4, " ")
        new_card_number.insert(9, " ")
        new_card_number.insert(14, " ")
        yield "".join(new_card_number)


# descriptions = transaction_descriptions(transactions)
# usd_transactions = filter_by_currency(transactions, "USD")
#
# if __name__ == "__main__":
#     for num in range(3):
#         print(next(usd_transactions)["id"])
#
#     for num in range(5):
#         print(next(descriptions))
#
#     for card_number in card_number_generator(1, 5):
#         print(card_number)
