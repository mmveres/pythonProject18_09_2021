if __name__ == '__main__':
    arr =[]
    with open("data.txt", "r") as file:
        for line in file:
           arr.append(int(line))
    print(arr)