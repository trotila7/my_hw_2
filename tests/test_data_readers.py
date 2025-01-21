import pytest
from unittest.mock import patch, MagicMock
from src.data_readers import read_csv_transactions, read_excel_transactions


@patch('src.data_readers.pd.read_csv')
def test_read_csv_transactions(mock_read_csv):
    # Создадим мок DataFrame
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {"amount": 100, "currency": "USD"},
        {"amount": 200, "currency": "RUB"}
    ]
    mock_read_csv.return_value = mock_df

    result = read_csv_transactions("dummy.csv")
    assert len(result) == 2
    assert result[0]["currency"] == "USD"
    assert result[1]["amount"] == 200


@patch('src.data_readers.pd.read_excel')
def test_read_excel_transactions(mock_read_excel):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {"amount": 999, "currency": "USD"}
    ]
    mock_read_excel.return_value = mock_df

    result = read_excel_transactions("dummy.xlsx")
    assert len(result) == 1
    assert result[0]["amount"] == 999
