import os
from dotenv import load_dotenv
import requests

load_dotenv(os.path.join("..", ".env"))

API_KEY = os.getenv('API_KEY')
API_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={currency}&amount={amount}"


def currency_conversion(transaction: dict) -> float:
    """ Функция, которая получает актуальный курс валют и конвертирует их в RUB """
    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if currency == "RUB":
        return amount
    elif currency in ["USD", "EUR"]:
        try:
            response = requests.get(API_URL.format(to="RUB", currency=currency, amount=amount),
                                    headers={"apikey": API_KEY})
            if response.status_code == 200:
                data = response.json()
                return data["result"]
            else:
                print(f'Ошибка при конвертации валюты: {response.status_code}')
                return 0.0
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при конвертации валюты: {e}')
            return 0.0
    else:
        return 0.0
