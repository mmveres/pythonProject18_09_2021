if __name__ == '__main__':
    while True:
        try:
            value_from_con = input("enter int")
            int_value = int(value_from_con)
            print("int value = ", int_value)
            if 2<=int_value<=12:
                print("mark value = ", int_value)
            else:
                raise Exception("not mark")
            break
        except ValueError as e:
            print("error not int, ", e.__str__())
        except Exception as e:
            print("error not mark, ", e.__str__())