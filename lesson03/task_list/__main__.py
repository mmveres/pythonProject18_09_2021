from lesson03.task_list.list_task import get_list_odd_value_task01_v1
from lesson03.task_list.task2_5 import *

if __name__ == '__main__':
    list_elem =[]
    print("*************MENU**************")
    print("0.ввести 10 целых значений с консоли")
    print(""" 1.создайте массив, содержащий 10 первых нечетных чисел.
          Выведете элементы массива на консоль в одну строку, разделяя запятой""")
    print("2.разместить в 2 масива четные и нечетные вывести значение")
    print("""3.разместить в 2 масива четные и нечетные,
    подсчитать сколько четные и нечетные""")
    print("""4.разместить в 2 масива четные и нечетные, вывести
    сумма елементов в каждом масиве и среднее арифметическое""")
    choice = input("enter menu number")
    if choice == 0:
        list_elem = get_list_from_console()
    elif choice == 1:
        print(get_list_odd_value_task01_v1())
    elif choice == 2:
        l_odd, l_even = get_list_even_odd(list_elem)
        print(l_odd)
        print(l_even)
    elif choice == 3:
        l_odd, l_even = get_list_even_odd(list_elem)
        print(len(l_odd))
        print(len(l_even))
    elif choice == 4:
        l_odd, l_even = get_list_even_odd(list_elem)
        print(get_sum(l_odd))
        print(get_sum(l_even))
        print(get_average(l_even))
        print(get_average(l_odd))