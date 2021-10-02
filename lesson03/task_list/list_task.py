# 1.создайте массив, содержащий 10 первых нечетных чисел.
# Выведете элементы массива на консоль в одну строку, разделяя запятой
# 2.ввести 10 целых значений с консоли и разместить в
# 2 масива четные и нечетные
# 3.подсчитать сколько четные и нечетные
# 4.сумма елементов в каждом масиве и среднее арифметическое
# 5.поменять четные позиции в первом масиве на значения
# нечетных позиций из 2 массива
# 6.Дан массив размерности N, найти наименьший элемент массива
# и вывести на консоль (если наименьших элементов несколько —
# вывести их индексы).
# 7.Поменять наибольший и наименьший элементы массива местами.
# Пример: дан массив {4, -5, 0, 6, 8}.
# После замены будет выглядеть {4, 8, 0, 6, -5}.
import random


def get_list_odd_value_task01_v1(max_count=10):
    return list(range(1,max_count*2,2))

def get_list_odd_value_task01_v2(max_count=10):
    arr_odd = []
    x = 0
    count_odd = 0
    while count_odd<max_count:
        if x%2 == 1:
            count_odd+=1
            arr_odd.append(x)
        x+=1
    return arr_odd

def get_list_odd_value_task01_v3(max_count=10):
    arr_odd = []
    x = 1
    count_odd = 0
    while count_odd<max_count:
        count_odd+=1
        arr_odd.append(x)
        x+=2
    return arr_odd

def get_list_odd_value_task01_v4(max_count=10):
    arr_odd = []
    count_odd = 0
    while count_odd<max_count:
        x = random.randint(0, 100)
        print(x,end=", ")
        if x%2 == 1:
            count_odd+=1
            arr_odd.append(x)
    return arr_odd

def get_list_odd_value_task01_v5(max_count=10):
    arr_odd = [0]*max_count
    x = 0
    count_odd = 0
    while count_odd<max_count:
        if x%2 == 1:
            arr_odd[count_odd] = x
            count_odd+=1
        x+=1
    return arr_odd

def get_list_odd_value_task01_v6(max_count=10):
    arr_odd = []
    count_odd = 0
    while count_odd<max_count:
        x = int(input("enter int"))
#        print(x,end=", ")
        if x%2 == 1:
            count_odd+=1
            arr_odd.append(x)
    return arr_odd

if __name__ == '__main__':
    print(get_list_odd_value_task01_v6(4))