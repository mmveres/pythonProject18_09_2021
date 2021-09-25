# 5. Дано число месяца (тип int). Необходимо определить время года
# (зима, весна, лето, осень) и вывести на консоль.


def print_season(month_number):
    season1 = "зима"
    season2 = "весна"
    season3 = "лето"
    season4 = "осень"
    if month_number == 12:
        print("Время года :", season1)
    elif month_number == 1:
        print("Время года :", season1)
    elif month_number == 2:
        print("Время года :", season1)
    elif month_number == 3:
        print("Время года :", season2)
    elif month_number == 4:
        print("Время года :", season2)
    elif month_number == 5:
        print("Время года :", season2)
    elif month_number == 6:
        print("Время года :", season3)
    elif month_number == 7:
        print("Время года :", season3)
    elif month_number == 8:
        print("Время года :", season3)
    elif month_number == 9:
        print("Время года :", season4)
    elif month_number == 10:
        print("Время года :", season4)
    elif month_number == 11:
        print("Время года :", season4)
    else:
        print("error month")


if __name__ == '__main__':
    month_number = int(input("Введите номер месяца : "))
    print_season(month_number)