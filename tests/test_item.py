from src.item import Item
import pytest


@pytest.fixture
def item_1():
    return Item("Смартфон", 10000, 20)


def test_item_init(item_1):
    assert item_1.name == "Смартфон"
    assert item_1.price == 10000
    assert item_1.quantity == 20


def test_calculate_total_price(item_1):
    assert item_1.calculate_total_price() == 200000


def test_apply_discount(item_1):
    item_1.pay_rate = 0.5
    assert item_1.apply_discount() == 5000

