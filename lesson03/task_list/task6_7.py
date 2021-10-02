# 6.Дан массив размерности N, найти наименьший элемент массива
# и вывести на консоль (если наименьших элементов несколько —
# вывести их индексы).
# 7.Поменять наибольший и наименьший элементы массива местами.
# Пример: дан массив {4, -5, 0, 6, 8}.
# После замены будет выглядеть {4, 8, 0, 6, -5}.

def print_min_elem_with_index(list_elem):
    min_elem = min(list_elem)
    print(min_elem)
    for i in range(len(list_elem)):
        if list_elem[i] == min_elem:
            print(i,end=", ")


def change_min_max_elem(list_elem):
    min_elem = min(list_elem)
    max_elem = max(list_elem)
    ind_min_elem = list_elem.index(min_elem)
    ind_max_elem = list_elem.index(max_elem)
    for i in range(len(list_elem)):
        if list_elem[i] == min_elem:
            list_elem[i] = max_elem
        elif list_elem[i] == max_elem:
            list_elem[i] = min_elem

if __name__ == '__main__':
    list_elem = [4, -5, 0, 6, 8, -5]
    change_min_max_elem(list_elem)
    print(list_elem)

    matrix = [
        [1,2,3],
        [4,5,6]
    ]
    for row in matrix:
        for cell in row:
            print(cell,end = " ")
        print()

    print(len(matrix))
    print(matrix)
    print(len(matrix[0]))
    print(len(matrix[1]))
    print(matrix[0])
    print(matrix[1])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end = " ")
        print()
