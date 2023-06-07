import csv
import os


class InstantiateCSVError(Exception):
    """Класс исключения, если файл поврежден"""
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else '_Файл item.csv поврежден_'

    def __str__(self):
        return f"Ошибка: {self.message}"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    CSV_PATH = os.path.abspath(r"../src/items.csv") #нормальный файл
    #CSV_PATH = os.path.abspath(r"../src/items1.csv") #сломанный файл
    #CSV_PATH = os.path.abspath(r"../src/items0.csv") #несуществующий файл

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()

        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) >= 10:
            raise Exception("Длина наименования товара превышает 10 символов.")
        self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        """
        cls.all.clear()
        try:
            with open(cls.CSV_PATH, newline='') as file:
                reader = csv.DictReader(file)
                try:
                    for row in reader:
                        cls(row['name'], row['price'], row['quantity'])
                except KeyError:
                    print('_Файл item.csv поврежден_')
                    raise InstantiateCSVError
        except FileNotFoundError:
            print('_Отсутствует файл item.csv_')

    @staticmethod
    def string_to_number(string):
        """
        Возвращает число из числа-строки
        """
        return int(float(string))

    def __add__(self, other):
        """
        Реализует возможность сложения экземпляров класса
        (сложение по количеству товара)
        """
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity


