from src.keyboard import KeyBoard
import pytest


@pytest.fixture
def kb_1():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_kb_init(kb_1):
    assert kb_1.name == "Dark Project KD87A"
    assert kb_1.price == 9600
    assert kb_1.quantity == 5
    assert kb_1.language == "EN"


def test_repr(kb_1):
    assert repr(kb_1) == "KeyBoard('Dark Project KD87A', 9600, 5)"


def test_str(kb_1):
    assert str(kb_1) == 'Dark Project KD87A'
    assert str(kb_1.language) == 'EN'


def test_change_lang(kb_1):
    kb_1.change_lang()
    assert kb_1.language == "RU"
    kb_1.change_lang().change_lang()
    assert kb_1.language == "RU"
    kb_1.change_lang().change_lang().change_lang()
    assert kb_1.language == "EN"



