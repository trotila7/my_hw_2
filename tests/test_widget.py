import pytest

from src.widget import data_transformation, mask_card_3


@pytest.mark.parametrize(
    "card, mask_card",
    [
        ("Visa 1234123412341234", "Visa 1234 12** **** 1234"),
        ("Kisa 1234123412341234", "Введен некорректный номер карты или счета"),
        ("12", "Введен некорректный номер карты или счета"),
    ],
)
def test_mask_card_3(card, mask_card):
    assert mask_card_3(card) == mask_card


@pytest.mark.parametrize(
    "data_input, data_trans",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2018-07-11", "11.07.2018"),
    ],
)
def test_data_transformation(data_input, data_trans):
    assert data_transformation(data_input) == data_trans
