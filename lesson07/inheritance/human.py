from lesson07 import validator


class Human:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = validator.get_positive_value(value)

    def eat(self, food):
        self.weight+=food

    def __str__(self):
        return f"{self.name}, {self.age}, {self.weight}"