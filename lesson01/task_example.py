x = 0
x = x + 10
x += 10
x +=1
f1 = 1.0203
f2 = 1.0205
is_equal = abs(f1 - f2) < 0.001
print(is_equal)

x = 16
print(f"{x}")
print("{0} in binary {0:08b}   in hex {0:02x} in octal {0:02o}".format(x))

print(str(x)+"in binary ")

age = 18
a = 10 + 1
b = 20 + 2
if age >= 21:
    print("Доступ разрешен", a)
else:
    if age >= 18:
        print("Доступ частично разрешен", b)
    else:
        print("Доступ запрещен")