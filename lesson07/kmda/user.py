class User:
    def __init__(self, name, position, salary, total):
        self.name = name
        self.position = position
        self.salary = salary
        self.total = total

    def to_dict(self):
        user_dict = dict()
        user_dict["name"] = self.name
        user_dict["position"]  =self.position
        user_dict["salary"] =self.salary
        user_dict["total"] = self.total
        return user_dict

    def __str__(self):
        return f"User : ({self.name},{self.position}, {self.salary}, {self.total})"

    def __repr__(self):
        return f"*{self.name},{self.position}, {self.salary}, {self.total}*\n"