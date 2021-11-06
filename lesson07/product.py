from lesson07 import validator

class Product:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = validator.get_positive_value(value)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = validator.get_positive_value(value)

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.price}"