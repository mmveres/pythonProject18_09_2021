from lesson07 import validator
from lesson07.inheritance.human import Human


class Student(Human):
    def __init__(self, name, age, group, weight):
        super().__init__(name, age, weight)
        self.group = group

    def study(self):
        print("i'm study")

    def __str__(self):
        return f"Student: {self.name}, {self.age}, {self.weight}, {self.group}"