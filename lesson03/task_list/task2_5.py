# 2.ввести 10 целых значений с консоли и разместить в
#           2 масива четные и нечетные
# 3.подсчитать сколько четные и нечетные
# 4.сумма елементов в каждом масиве и среднее арифметическое
# 5.поменять четные позиции в первом масиве на значения
# нечетных позиций из 2 массива

def is_even(value):
    return value % 2 == 0

def get_list_from_console():
    list_elem = []
    count_num = int(input(f'Введите количество чисел '))
    for i in range(0, count_num):
        num = int(input(f'Введите {i} число '))
        list_elem.append(num)
    return list_elem

def get_list_even_odd(list_elem):
    arr_even = []
    arr_odd = []
    for num in list_elem:
        if is_even(num):
            arr_even.append(num)
        else:
            arr_odd.append(num)
    return arr_odd, arr_even

def get_sum(list_elem):
    arr_sum = 0
    for item in list_elem:
        arr_sum += item
    return arr_sum

def get_average(list_elem):
    return round(get_sum(list_elem) / len(list_elem), 2)

def change_elem(arr_even, arr_odd):
    for i in range(0,len(arr_even),2):
        if i+1 < len(arr_odd):
            temp = arr_odd[i+1]
            arr_odd[i+1] = arr_even[i]
            arr_even[i] = temp

if __name__ == '__main__':

    l_odd =  [1,3,5,7,9]
    l_even = [0,2,4,6,8]
    change_elem(l_even,l_odd)
    print(l_odd)
    print(l_even)


# arr_even_len = len(arr_even)
# arr_odd_len = len(arr_odd)
#
# arr_even_sum = 0
# arr_odd_sum = 0
#
# for item in arr_even:
#     arr_even_sum += item
#
# for item in arr_odd:
#     arr_odd_sum += item
#
# arr_even_average = round(arr_even_sum / arr_even_len, 2)
# arr_odd_average = round(arr_odd_sum / arr_odd_len, 2)
#
# print(f'Четный массив {arr_even}, его длинна: {arr_even_len}, сумма элементов: {arr_even_sum}, среднее значение : {arr_even_average}')
# print(f'Нечетный массив {arr_odd}, его длинна: {arr_odd_len}, сумма элементов: {arr_odd_sum}, среднее значение : {arr_odd_average}')
#
# for i in range(arr_even_len):
#     if not is_even(i):
#         arr_even[i] = arr_odd[i - 1]
#
# print(f'Четный массив после преображения {arr_even}')