from typing import Iterable, Iterator

transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)


def filter_by_currency(input_list: Iterable[dict], code: str) -> Iterator[dict]:
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


descriptions = transaction_descriptions(transactions)
usd_transactions = filter_by_currency(transactions, "USD")

if __name__ == "__main__":
    for num in range(3):
        print(next(usd_transactions)["id"])

    for num in range(5):
        print(next(descriptions))

    for card_number in card_number_generator(1, 5):
        print(card_number)
