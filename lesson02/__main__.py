from lesson02.task05 import print_season
import task_lib, task_cw

if __name__ == '__main__':
    while True:
        print("-----------------Menu-------------------")
        print("1. Даны 4 числа типа int. Сравнить их и вывести наименьшее на консоль.")
        print("2. Вывести на консоль количество максимальных чисел среди этих четырех.")
        print("3. Даны 5 чисел (тип int). Вывести вначале наименьшее, а затем наибольшее из данных чисел.")
        print("""4. Даны имена 2х человек (тип string). 
            Если имена равны,то вывести сообщение о том, что люди являются тезками. """)
        print("""5. Дано число месяца (тип int). 
            Необходимо определить время года (зима, весна, лето, осень) и вывести на консоль.  """)
        print("0. Exit")
        answer = int(input("Enter choice: "))
        if answer == 0:
            break;
        elif answer == 1:
            a = 1
            b = 2
            c = 3
            d = 4
            print(task_lib.get_min_value(a,b,c,d))
        elif answer == 2:
            a = 1
            b = 2
            c = 3
            d = 4
            print(task_lib.get_count_max_value(a,b,c,d))
        elif answer == 3:
            a = 1
            b = 2
            c = 3
            d = 4
            e = 5
            print(min(a,b,c,d,e))
            print(max(a,b,c,d,e))
        elif answer == 4:
            name1 = input("enter name1 ")
            name2 = input("enter name2 ")
            print(task_cw.task04_compare_2_human(name1, name2))
        elif answer == 5:
            season_num = int(input("enter num season"))
            print_season(season_num)
