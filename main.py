import os.path

from src.external_api import currency_conversion
from src.masks import mask_card_1, mask_card_2
from src.utils import transaction_amount

num_card = "1111222233334444"
print(mask_card_1(num_card))
print(mask_card_2(num_card))

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "data", "operations.json")
transactions = transaction_amount(file_path)

for transaction in transactions:
    rub_amount = currency_conversion(transaction)
    print(f"Transaction amount in RUB: {rub_amount}")
