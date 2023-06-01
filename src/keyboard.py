from src.item import Item


class Language:
    """
    Класс для реализации дополнительного функционала по хранению
    и изменению раскладки клавиатуры в отдельном классе-миксине
    ”"""

    def __init__(self, language='EN'):
        self.__language = language

    def __str__(self):
        return f"{self.__language}"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Метод для изменения языка (раскладки клавиатуры)"""

        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")
        return self


class KeyBoard(Item, Language):
    """Класс для товара “клавиатура”"""
    pass
