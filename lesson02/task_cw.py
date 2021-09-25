# 3. Даны 5 чисел (тип int). Вывести вначале наименьшее,
# а затем наибольшее из данных чисел.
# 4. Даны имена 2х человек (тип string). Если имена равны,
# то вывести сообщение о том, что люди являются тезками.
# 5. Дано число месяца (тип int). Необходимо определить время года
# (зима, весна, лето, осень) и вывести на консоль.

def task03_print_5_min_max(a,b,c,d,e):
    pass


def task04_compare_2_human(name1, name2):
    if name1 == name2:
        return "the same name"
    else:
        return "not same name"

def task05_print_season(month_number):
    pass

if __name__ == '__main__':
    print(task04_compare_2_human("tom1","tom1"))
    print(task04_compare_2_human("tom1","tom2"))