from lesson07.inheritance.human import Human


class Fighter(Human):
    def __init__(self, name, age, power, defence, weight):
        super(Fighter,self).__init__(name, age, weight)
        self.power = power
        self.defence = defence

    def fight(self, power):
        self.defence-=power

    def __str__(self):
        return f"Fighter: {super().__str__()}, {self.power}, {self.defence}"