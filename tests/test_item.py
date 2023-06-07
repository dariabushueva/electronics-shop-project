from src.item import Item
import pytest


@pytest.fixture
def item_1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item_2():
    return Item("Кабель", 10, 5)


def test_item_init(item_1):
    assert item_1.name == "Смартфон"
    assert item_1.price == 10000
    assert item_1.quantity == 20


def test_repr(item_2):
    assert repr(item_2) == "Item('Кабель', 10, 5)"


def test_str(item_2):
    assert str(item_2) == 'Кабель'


def test_calculate_total_price(item_1):
    assert item_1.calculate_total_price() == 200000


def test_apply_discount(item_1):
    item_1.pay_rate = 0.5
    assert item_1.apply_discount() == 5000


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item3 = Item.all[1]
    assert item3.name == 'Ноутбук'
    assert item3.price == '1000'
    assert item3.quantity == '3'


def test_instantiate_from_csv_error():
    Item.instantiate_from_csv()
    assert Item.instantiate_from_csv() is None


def test_string_to_number():
    assert Item.string_to_number('3') == 3
    assert Item.string_to_number('3.0') == 3
    assert Item.string_to_number('3.5') == 3


def test__add__(item_1, item_2):
    assert item_1 + item_2 == 25

