def print_min_value(num1, num2, num3, num4):
    min_num = num1
    if min_num > num2:
        min_num = num2
    if min_num > num3:
        min_num = num3
    if min_num > num4:
        min_num = num4
    print("min value =", min_num)

def get_min_value(num1, num2, num3, num4):
    min_num = num1
    if min_num > num2:
        min_num = num2
    if min_num > num3:
        min_num = num3
    if min_num > num4:
        min_num = num4
    return min_num

def get_max_value(n1, n2, n3, n4):
    max_num = n1
    if max_num < n2:
        max_num = n2
    if max_num < n3:
        max_num = n3
    if max_num < n4:
        max_num = n4
    return max_num

def get_count_max_value(num1, num2, num3, num4):
    max_num = get_max_value(num1, num2, num3, num4)
    count_max = 0
    if num1 == max_num:
        count_max+=1
    if num2 == max_num:
        count_max+=1
    if num3 == max_num:
        count_max+=1
    if num4 == max_num:
        count_max+=1
    return count_max

if __name__ == '__main__':
    print(get_min_value(1,2,1,2))