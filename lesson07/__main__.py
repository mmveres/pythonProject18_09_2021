from lesson07.customer import Customer
from lesson07.order import Order
from lesson07.product import Product

if __name__ == '__main__':
    p1 = Product("Apple", 1,20)
  #  p1.price = -10
    print(p1)
    cust1 = Customer("Tom", 20, 0.10)
    order1 = Order(1,"06.11.2021", cust1)
    order1.add(p1)
    order1.add(Product("Banana",1,30))
    print(order1.total_price())
