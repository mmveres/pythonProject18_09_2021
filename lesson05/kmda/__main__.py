import csv

if __name__ == '__main__':
    # with open("lipen-2019.csv", "r") as file_dig:
    #     reader = csv.DictReader(file_dig)
    #     for row in reader:
    #       for key in row:
    #         print(key, " : ", row[key])
    with open("../../lesson07/kmda/lipen-2019.csv", "r") as file_dig:
        title = file_dig.readline()
        for row in file_dig:
            user_elem = row.split(";")
            print(user_elem[0], user_elem[4].replace(",", "."))
