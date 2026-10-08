import pytest

from app.calculator import (
    add_expense,
    add_income,
    calculate_balance,
)


def test_add_income():
    assert add_income(1000, 500) == 1500


def test_add_expense():
    assert add_expense(1000, 300) == 700


def test_calculate_balance():
    assert calculate_balance(
        [1000, 2000],
        [500, 300],
    ) == 2200


def test_negative_income():
    with pytest.raises(ValueError):
        add_income(1000, -500)


def test_negative_expense():
    with pytest.raises(ValueError):
        add_expense(1000, -300)


def test_negative_values_in_balance():
    with pytest.raises(ValueError):
        calculate_balance([1000], [-500])
