import pandas as pd
from typing import Any, List, Dict


def read_csv_transactions(file_path: str) -> list[dict[str, Any]]:
    """
    Считывает CSV-файл, содержащий транзакции, и возвращает их в виде списка словарей.
    """
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
        return df.to_dict('records')
    except Exception as exc:
        print(f"Ошибка при чтении CSV-файла {file_path}: {exc}")
        return []


def read_excel_transactions(file_path: str) -> list[dict[str, Any]]:
    """
    Считывает XLSX-файл, содержащий транзакции, и возвращает их в виде списка словарей.
    """
    try:
        df = pd.read_excel(file_path)
        return df.to_dict('records')
    except Exception as exc:
        print(f"Ошибка при чтении Excel-файла {file_path}: {exc}")
        return []

