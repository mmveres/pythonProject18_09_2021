import math
from lesson02.task_lib import print_min_value, get_min_value, get_max_value, get_count_max_value
def main():
    # Даны 4 числа типа int.
    num1 = int(input('Введите первое число '))
    num2 = int(input('Введите второе число '))
    num3 = int(input('Введите третье число '))
    num4 = int(input('Введите четвертое число '))

    #===math
    min_value = min(num1, num2, num3, num4)
    print("lib min=",min_value)

    # Сравнить их и вывести наименьшее на консоль.
    print_min_value(num1,num2,num3,num4)
    min_num = get_min_value(num1,num2,num3,num4)
    print("min num=", min_num)

    # 2. Вывести на консоль количество максимальных чисел среди этих четырех.
    max_num = get_max_value(n1=num1, n4=num4, n3=num3, n2=num2)
    max_num = get_max_value(10, 1, 2, 3)
    max_num = get_max_value(100, 100, 200, 300)

    count_max = get_count_max_value(num1=2,num2=4, num3=4,num4=1)
    print("count max=", count_max)

main()