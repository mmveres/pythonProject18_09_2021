class OrderList:
    def __init__(self, name ):
        self.__orders = list()

    def add(self, order):
        self.__orders.append(order)

    def get_orders_by_customer(self, customer):
        pass

    def get_order_with_max_price(self):
        pass

    def get_order_with_max_discount(self):
        pass