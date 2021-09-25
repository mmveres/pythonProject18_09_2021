# 3. Даны 5 чисел (тип int). Вывести вначале наименьшее,
def get_min_num(a, b, c, d, e):
    min_num = a
    if min_num > b:
        min_num = b
    if min_num > c:
        min_num = c
    if min_num > d:
        min_num = d
    if min_num > e:
        min_num = e
    return min_num


a = int(input("Enter first number!"))
b = int(input("Enter second number!"))
c = int(input("Enter third number!"))
d = int(input("Enter fourth number!"))
e = int(input("Enter fifth number!"))

x = get_min_num(a,b,c,d,e)
x = get_min_num(1,2,3,2,1)
print("min_num=", x)