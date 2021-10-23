# 1. считать с консоли 6 числовых значений и записать в файл.
# 2. прочитать из файла значения и записать в список, посчитать сумму и среднее
# 3. 1 и 2 сделать для матрицы(2х3)

if __name__ == '__main__':
    # arr = [1, 2, 3, 4, 4, 3, 3, 2]
    # with open("digit.txt", "w") as file_dig:
    #     for el in arr:
    #         file_dig.write(str(el) + "\n")
    #
    # with open("digit.txt", "r") as file_dig:
    #     for el in file_dig:
    #         print(int(el))

    matrix = []
    with open("matrix.txt", "r") as file_dig:
        for row in file_dig:
            row_arr = [int(el) for el in row.split()]
            matrix.append(row_arr)

    print(matrix)
    sum= 0;
    count = 0;
    count_size_row = 0
    for row in matrix:
        for cell in row:
            sum+=cell
            count+=1
        count_size_row+=len(row)
    print(count)
    print(count_size_row)
    print(round(sum/count,2))
