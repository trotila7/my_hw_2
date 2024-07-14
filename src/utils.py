import json
import logging
from typing import Any

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logs/log_utils.log",
    filemode="w",
)

utils_logger = logging.getLogger("utils")


def transaction_amount(file_path: str) -> Any:
    try:
        utils_logger.info("Открытие json-файла")
        with open(file_path, "r", encoding="utf-8") as file:
            repository = json.load(file)
        if isinstance(repository, (list, dict)):
            utils_logger.info("Файл открыт успешно")
            return repository
        else:
            utils_logger.debug("Файл не содержит необходимые данные")
            return []
    except Exception as e:
        utils_logger.error(f"Ошибка при открытии файла {e}")
        print(f"Ошибка {e}")
        return []
