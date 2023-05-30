from src.phone import Phone
import pytest


@pytest.fixture
def phone_1():
    return Phone("Смартфон", 10000, 20, 1)


@pytest.fixture
def phone_2():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_init(phone_1):
    assert phone_1.name == "Смартфон"
    assert phone_1.price == 10000
    assert phone_1.quantity == 20


def test_repr(phone_2):
    assert repr(phone_2) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone_2):
    assert str(phone_2) == 'iPhone 14'


def test_set_number_of_sim(phone_2):
    phone_2.number_of_sim = 2
    assert phone_2.number_of_sim == 2


def test__add__(phone_1, phone_2):
    assert phone_1 + phone_2 == 25

