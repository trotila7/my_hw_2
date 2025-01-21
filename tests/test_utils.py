import json
from unittest.mock import ANY, mock_open, patch

import pandas as pd

from src.utils import read_json_transactions


def test_transaction_in_rub():
    with patch('src.external_api.currency_conversion') as mock_conversion:
        mock_conversion.side_effect = AssertionError("Should not be called")
        transactions = [{"operationAmount": {"currency": {"code": "RUB"}, "amount": "100"}}]
        result = read_json_transactions(transactions)
        assert result == 100.0


def test_transaction_not_in_rub():
    with patch('src.external_api.currency_conversion') as mock_conversion:
        mock_conversion.return_value = 120.0
        transactions = [{"operationAmount": {"currency": {"code": "USD"}, "amount": "100"}}]
        result = read_json_transactions(transactions)
        assert result is None


def test_multiple_transactions():
    with patch('src.external_api.currency_conversion') as mock_conversion:
        mock_conversion.side_effect = [120.0, 150.0]
        transactions = [
            {"operationAmount": {"currency": {"code": "USD"}, "amount": "100"}},
            {"operationAmount": {"currency": {"code": "EUR"}, "amount": "120"}}
        ]
        result = read_json_transactions(transactions)
        assert result is None
