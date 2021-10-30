from lesson06.classes import Cat, Mouse


def test_class_cat():
    cat1 = Cat("Tom", 5, 7);
    cat1.print_info()
    cat1.eat(10.5)
    cat1.set_name("abc567")
    cat1.print_info()
    m1 = Mouse("Jerry", 0.35)
    cat1.eat(m1.get_weight())
    cat1.print_info()
    m1.print_info()
    cat2 = Cat(name="Bob", age=10, weight=11);
    cat2.print_info()
    cat3 = Cat();
    cat3.print_info()
    cat4 = Cat(name="Alice", age=1)
    cat4.print_info()


if __name__ == '__main__':
    try:
        cat1 = Cat("Tom", 5, 7);
        cat1.print_info()
        m1 = Mouse("Jerry1", 0.35)
        cat1.eat_mouse(m1)
        m2 = Mouse("Jerry2", 0.35)
        cat1.eat_mouse(m2)
        for i in range(0,30):
            cat1.eat_mouse(Mouse("BigJerry"+str(i), 0.5))
        cat1.print_info()
        m1.print_info()
    except Exception as e:
        print(e)
