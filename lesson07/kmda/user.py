class User:
    def __init__(self, name, position, salary, total):
        self.name = name
        self.position = position
        self.salary = salary
        self.total = total

    def __str__(self):
        return f"User : ({self.name},{self.position}, {self.salary}, {self.total})"

    def __repr__(self):
        return f"*{self.name},{self.position}, {self.salary}, {self.total}*\n"