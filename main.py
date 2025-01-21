import os.path

from src.external_api import currency_conversion
from src.masks import mask_card_1, mask_card_2
from src.utils import read_json_transactions
from src.data_readers import read_csv_transactions, read_excel_transactions


def main():
    num_card = "1111222233334444"
    print(mask_card_1(num_card))
    print(mask_card_2(num_card))

    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_dir, "data", "operations.json")
    json_transactions = read_json_transactions(json_file_path)

    csv_file_path = os.path.join(current_dir, "data", "transactions.csv")
    csv_transactions = read_csv_transactions(csv_file_path)

    xlsx_file_path = os.path.join(current_dir, "data", "transactions_excel.xlsx")
    xlsx_transactions = read_excel_transactions(xlsx_file_path)

    print("=== JSON ===")
    for transaction in json_transactions:
        rub_amount = currency_conversion(transaction)
        print(f"Transaction amount in RUB: {rub_amount}")

    print("=== CSV ===")
    for transaction in csv_transactions:
        rub_amount = currency_conversion(transaction)
        print(f"Transaction amount in RUB: {rub_amount}")

    print("=== Excel ===")
    for transaction in xlsx_transactions:
        rub_amount = currency_conversion(transaction)
        print(f"Transaction amount in RUB: {rub_amount}")


if __name__ == "__main__":
    main()
