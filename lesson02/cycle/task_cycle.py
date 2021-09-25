def print_inc_value(start=0, end=100, delta=1):
    i = start
    while i < end:
        print(i)
        i = i + delta


def print_dec_value(start, end, delta):
    i = start
    while i >= end:
        print(i)
        i = i - delta


def print_power_value(x = 2,n = 10):
    i = 0
    xn = 1;
    while i < n:
        xn *= x
        i += 1
        print(xn)


def get_power_value(x = 2, n = 10):
    xn = 1;
    for i in range(n):
        xn *= x
    return xn
