if __name__ == '__main__':
    arr = [1, 2, 3, 4, 4, 3, 3, 2]
    with open("digit.txt", "w") as file_dig:
        for el in arr:
            file_dig.write(str(el) + "\n")

    with open("digit.txt", "r") as file_dig:
        for el in file_dig:
            print(int(el))

    matr = [
        [1, 2, 3],
        [4, 5, 6]
    ]
