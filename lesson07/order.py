class Order:
    def __init__(self, id, date, customer):
        self.id = id
        self.date = date
        self.customer = customer
        self.products = list()

    def add(self, product):
        self.products.append(product)

    def total_price(self):
        sum = 0
        for product in self.products:
            sum+=product.price
        return sum*(1-self.customer.discount)
