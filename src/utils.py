import json
import logging
from typing import Any, List, Dict

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logs/log_utils.log",
    filemode="w",
)

utils_logger = logging.getLogger("utils")


def read_json_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает JSON-файл, содержащий транзакции, и возвращает их в виде списка словарей.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Предположим, что структура в файле — список объектов-транзакций
            if isinstance(data, list):
                return data
            else:
                utils_logger.warning(f"JSON-файл {file_path} содержит не список, возвращаем пустой список.")
                return []
    except FileNotFoundError as e:
        utils_logger.error(f"Файл {file_path} не найден: {e}")
        return []
    except json.JSONDecodeError as e:
        utils_logger.error(f"Некорректный формат JSON в файле {file_path}: {e}")
        return []
    except Exception as exc:
        utils_logger.error(f"Неизвестная ошибка при чтении {file_path}: {exc}")
        return []
