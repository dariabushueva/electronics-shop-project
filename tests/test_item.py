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


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item3 = Item.all[2]
    assert item3.name == 'Кабель'
    assert item3.price == '10'
    assert item3.quantity == '5'


def test_string_to_number():
    assert Item.string_to_number('3') == 3
    assert Item.string_to_number('3.0') == 3
    assert Item.string_to_number('3.5') == 3

