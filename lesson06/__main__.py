from lesson06.controll.doctor_controller import DoctorController
from lesson06.controll.grandma_controller import GrandmaController
from lesson06.model.animals.classes import Cat, Mouse
from lesson06.model.keppers.grandma import Grandma
from lesson06.model.medic.doctor import Doctor


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
    cat1 = Cat("Tom", 5, 7);
    while(True):
        print("1. Grandma")
        print("2. Doctor")
        choise = input("enter choice")
        if choise == "1":
            try:
                cat1.print_info()
                grandma_controll = GrandmaController(Grandma("GrandBa"))
                grandma_controll.feed_cat(cat1)
                cat1.print_info()

            except Exception as e:
                print(e)
        elif choise == "2":
            doc_controll = DoctorController(Doctor("AyBolit"))
            doc_controll.diagnose(cat1)
        else:
            print("Exit")
            break