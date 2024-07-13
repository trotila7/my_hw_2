import json
from typing import Any


def transaction_amount(file_path: str) -> Any:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            repository = json.load(file)
        if isinstance(repository, (list, dict)):
            return repository
        else:
            return []
    except Exception as e:
        print(f"Ошибка {e}")
        return []
