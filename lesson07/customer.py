from lesson07 import validator


class Customer:
    def __init__(self, name, age, discount):
        self.name = name
        self.age = age
        self.discount = discount

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = validator.get_positive_value(value)

    def __str__(self):
        return f"{self.name}, {self.age}, {self.discount}"
