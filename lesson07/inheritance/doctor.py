from lesson07.inheritance.human import Human


class Doctor(Human):
    def __init__(self, name, age, licence, weight):
        Human.__init__(self, name, age, weight)
        self.licence = licence

    def cure(self):
        print("go to analise")

    def __str__(self):
        return f"Doctor: {Human.__str__(self)}, {self.licence}"