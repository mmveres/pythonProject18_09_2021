# 1. считать с консоли 6 числовых значений и записать в файл.
# 2. прочитать из файла значения и записать в список, посчитать сумму и среднее
# 3. 1 и 2 сделать для матрицы(2х3)

# ------------------1------------------
def task1():
    numbers = []

    for i in range(6):
        while True:
            num = input(f'Enter a {i} number ')
            if num.isdigit():
                numbers.append(num)
                break;


    with open('numbers.txt', 'w') as num_file:
        for value in numbers:
            num_file.write(value + '\n')


# ----------------2--------------
def task2():
    # nums_list = []
    # with open('numbers.txt', 'r') as num_file:
    #     for line in num_file:
    #         nums_list.append(int(line))


    with open('numbers.txt', 'r') as num_file:
        nums_list = [int(line) for line in num_file]


    nums_sum = sum(nums_list)
    nums_avg = round(nums_sum / len(nums_list), 2)

    print(nums_list, nums_sum, nums_avg)



# --------------------3----------------
def task3():
    matrix = []

    num_file = open('numbers.txt', 'r')

    row = []
    i = 0
    for line in num_file:
        row.append(int(line))
        i += 1
        if i % 3 == 0:
            matrix.append(row)
            row = []

    num_file.close()

    summa = 0
    count = 0

    for item in matrix:
        for j in item:
            summa += j
            count += 1


    avg = summa / count

    print(matrix, summa, avg)

if __name__ == '__main__':
    task1()