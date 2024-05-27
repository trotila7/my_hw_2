import pytest

from src.masks import mask_card_1, mask_card_2


@pytest.fixture
def number_card():
    return "1234123412341234"


def test_mask_card_1(number_card):
    assert mask_card_1(number_card) == "1234 12** **** 1234"


def test_mask_card_2(number_card):
    assert mask_card_2(number_card) == "**1234"


def test_mask_card_1_1():
    assert mask_card_1("123412341234123") == "Вы ввели некорректный номер карты"


@pytest.mark.parametrize(
    "card, mask_card",
    [
        ("1111222233334444", "**4444"),
        ("1234567812345678", "**5678"),
        ("1234", "Вы ввели некорректный номер карты"),
        ("1234567812345678123", "Вы ввели некорректный номер карты"),
    ],
)
def test_mask_card_2_2(card, mask_card):
    assert mask_card_2(card) == mask_card
