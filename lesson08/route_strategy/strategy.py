import abc

from lesson08.route_strategy.Bus import Bus


class Tour(abc.ABC):
    @abc.abstractmethod
    def transfer(self):
        pass

    @abc.abstractmethod
    def hotel(self):
        pass

    @abc.abstractmethod
    def eat(self):
        pass

class TourEconom(Tour):

    def __init__(self,transfer, hotel, eat):
        self.transfer = transfer
        self.hotel = hotel
        self.eat = eat

    def is_buy(self, money):
        return money >= self.tour_cost()

    def tour_cost(self):
        return self.transfer.transfer_cost() + self.hotel.hotel_cost()+ self.eat.eat_cost()

    @property
    def transfer(self):
        return self.__transfer;

    @transfer.setter
    def transfer(self, value):
        self.__transfer = value

    @property
    def hotel(self):
        return self.__hotel

    @hotel.setter
    def hotel(self, value):
        self.__hotel = value

    def eat(self):
        return self.eat


class EatStrategy:
    @abc.abstractmethod
    def eat_cost(self):
        pass

class EatAllInclude(EatStrategy):

    def eat_cost(self):
        return 100


class HotelStrategy:
    @abc.abstractmethod
    def hotel_cost(self):
        pass

class Hotel3(HotelStrategy):

    def hotel_cost(self):
        return 100

class Hotel4(HotelStrategy):

    def hotel_cost(self):
        return 200

class Hotel5(HotelStrategy):

    def hotel_cost(self):
        return 300

class TrasferStrategy:
    @abc.abstractmethod
    def transfer_cost(self):
        pass
    def __init__(self, route):
        self.route = route


class TrasferByCar(TrasferStrategy):

    def transfer_cost(self):
        return 200

class TrasferByPlane(TrasferStrategy):

    def transfer_cost(self):
        return 1000

class TrasferByBus(TrasferStrategy):

    def transfer_cost(self):
        return Bus("Ikarus", 40, 500).price * self.route/100 + 10

if __name__ == '__main__':
    tour = TourEconom(TrasferByBus(400),Hotel5(),EatAllInclude())
    print(tour.tour_cost())
    print(tour.is_buy(500))
